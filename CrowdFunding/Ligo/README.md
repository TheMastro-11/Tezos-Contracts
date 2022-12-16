# LIGO [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/Ligo/CrowdFunding.jsligo)
Nella versione di Ligo troviamo solamente uno Smart Contract:
* [CrowdFunding](#CrowdFunding).

    La ragione è che il linguaggio in questione non ci permette una [gestione della mappa](#main-issues) come gli altri due e quindi non risulta possibile realizzare completamente il nostro Use Case. 

## CrowdFunding

### Type
* `holder = map <address, list<tez>` = type utilizzato per tenere traccia dei **contributors**. 
    In Ligo è altamente comodo l'utilizzo dei *type-alias* in modo da rendere più agevole e comprensibile l'utilizzo di tipi *annidati* come in questo caso.   

### Attributes
* `startDate : timestamp = Tezos.get_now()` = data di inizio
* `endDate : timestamp = startDate + 5` =data di fine espressa in giorni
* `minAmount : tez  = 10 as mutez` = minima donazione
* `maxAmount : tez = 1000 as mutez` = massima donazione
* `ceiling : tez = 100000 as mutez` = obiettivo economico
* `floorPrice : tez = 200 as mutez` = tetto minimo da raggiungere

    Come si può notare non è presente la mappa dei *contributors* dal momento che il linguaggio non ci permette di gestire delle variabili globali. Di fatto **contributors** verrà dichiarata all'interno del [Main](#Main).

### EntryPoints
*   #### Main
    ``` 
    const main = ([_parameter, contractStorage] : [int, holder]) : [list<operation> , holder] => {
        //define contributors map and isSuccess condition
        let contributors : holder = Map.empty;
        let isSuccess : bool = false;
        let txs = list([]);

        //first Contribute
        contributors = contribute(contractStorage);
        //check if time is over
        if (Tezos.get_now() > endDate){
            let [a, b, c] =  checkEnding(contributors);
            isSuccess = a;
            contributors = b;
            txs = c;
        };

        return [txs, contributors]
    }; 
    ```
    Main access point that dispatches to the entrypoints according to the smart contract parameter.

*   #### Contribute
    ``` 
    const contribute = (contributors : holder)  => {
        //check if amount is between min and max
        assert_with_error( Tezos.get_amount() >= minAmount, "Amount too Low");
        assert_with_error( (Tezos.get_amount() <= maxAmount), "Amount too High");

        //add donator on map
        let checkContains = (contributors : holder ) => {
            return match(Map.find_opt (Tezos.get_sender(), contributors), {
            Some : _list_tez => 1,
            None : () => 2
            });
        };
        let checkResult : int = checkContains(contributors);
        
        let newMap : holder = Map.empty; //map to return after update
        let oldList : option<list<tez>> = None(); //old list of previous donation(s), if exist
        let total : tez = 0 as tez; //total sum of previous donation(s), if exist
        
        switch (checkResult) { //check result of checkContains
            case 1: //already donated
            //check if it will reach the max amount with other donation
            oldList = Map.find_opt(Tezos.get_sender(), contributors);
            for (const i of oldList) {
                total = total + i
            };
            assert_with_error((total <= maxAmount), "Max amount reached");

            //add new donation to oldList
            oldList = Map.find_opt(Tezos.get_sender(), contributors);
            newMap = Map.update(Tezos.get_sender(), Some(list([Tezos.get_amount(), oldList])), contributors);
            break;
            case 2: //new bidder  
            newMap = Map.add(Tezos.get_sender(), list([Tezos.get_amount()]), contributors);
            break;
        };

        return newMap
    };
    ```
    Invocata al momento della donazione, verifica che al cifra sia corretta e:
    * se il donatore è nuovo lo aggiunge alla mappa;
    * se il donatore esiste già -teoricamente- dovrebbe aggiornare la lista di donazione, in realtà questo [non è possibile](#main-issues).


*   #### CheckEnding
    ``` 
    const checkEnding = (contributors : holder) : [bool, holder] => {
        if (Tezos.get_balance() > floorPrice) { //if balance is over than the crowdfunding had reached the goal
            return [true, contributors, list([])]
        }; else { //otherwise the contract has to refund all the donators
            for (const i of contributors){
            let total : tez = 0 as tez;
            let [key, value] = i;  
            for (const j of value) {
                total += j;
            };
            let refundAddr = Tezos.get_contract_with_error(key, "Contract not found");
            let txs = Tezos.transaction(unit, total, refundAddr); //refund
            };
            return [false, Map.empty as holder, tx];
        };
        };
    };
    ```
    Verifica che **floorPrice** sia raggiunto, in caso positivo aggiorna **isSuccess** altrimenti rimborsa i **contributors**. La funzione restituisce l'elenco di transazioni che andranno poi restituite alla fine del [Main](#Main) in modo tale che vengano effettivamente registrate sulla chain.

### Main Issues
    A differenza di altri programmi Ligo non permette una gestione comoda delle mappe e delle liste.
    Nello specifico ho trovato difficile e senza soluzione: 
    * Iterare una mappa per trovare uno specifico elemento, come nel caso in cui sia necessario verificare se un *address* sia già presente o meno.
    * Manipolare le liste per estrarre un elemento, ottenere la *tail* o concatenarne due diverse. Il problema principale l'ho riscontrato nel passaggio da tipo 'option<list<>>' a 'list<>' obbligatorio nel momento in cui si usa la funzione **List.tail_opt()** per ottenere una sottostringa da unire con un'altra successivamente.
    * Accedere a **contributors** da qualsiasi funzione o entrypoints tramite variabile globale.
    * Ligo richiede di restituire sempre una lista di operazioni al termine della chiamata del [Main](#Main) per poterle salvare sulla chain, il che significa dover richiamare la funzione principale *x* volte in *y* modi diversi. Se infatti si vuole donare, [Main](#Main) avrà come ritorno la mappa aggiornata dei contributors, se invece si vuole verificare lo stato del CrowdFunding esso dovrà resituire o la [lista di transazioni per il refund](#checkending) o la chiamata al SC che si occupa del nuovo airdrop etc...