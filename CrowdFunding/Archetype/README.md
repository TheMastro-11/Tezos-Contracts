# ARCHETYPE [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/CrowdFunding.arl)

Anche nella versione di Archetype troviamo due SC:
* [CrowdFunding](#CrowdFunding);
* [TokenGen](#TokenGen).

### CrowdFunding
#### States:
* `funding` : stato iniziale nel quale è consentito effettuare le donazioni. Termina in due casi: o scade il tempo o si raggiunge l'obiettivo economico. 
* `airdorp` : stato finale di successo nel quale viene invocato l'[SC](#TokenGen) che si occupa dell'airdrop.
* `refund` : stato finale di fallimento nel quale viene effettuato il rimborso di tutti i donatori.

Tramite gli *states* è possibile controllare lo stato di avanzamento del CrowdFunding. 
Inoltre determinate azioni potranno essere eseguite solo in determinati *states* e in questo modo si evitano problemi o bug legati ad un uso improprio delle funzioni.

#### Constant and Variables:
*  `startDate : date = now` : data di inizio

*  `endDate : date = now + 5s` : data di fine espressa in giorni

*  `contributors : map<address, list<tez>> = []` : mappa dei donatori

*  `minAmount : tez = 10utz` : minima donazione

*  `maxAmount : tez = 1000utz` : massima donazione

*  `ceiling : tez = 100000utz` : obiettivo economico

*  `floorPrice : tez = 200utz` : tetto minimo da raggiungere

*  `isSuccess : bool = false` : indicatore successo al termine della raccolta

#### Transition
* `airdrop_ (funding -> airdrop)` : viene invocata dalla funzione **contribute** e **checkTime**. Garantisce il passaggio allo stato **airdrop**.
* `refund_ (funding -> refund)` : viene invocata dalla funzione **checkTime**. Garantisce il passaggio allo stato **refund**.

#### EntryPoints
*   ```
    entry contribute () {
        if state = funding then begin
            //check if amount is between min and max
            if transferred < minAmount or transferred > maxAmount then
                fail("Amount incorrect");

            //add donator on map
            var tmp : list<tez> =  [0utz]; //local variable 
            if contributors.contains(caller) then begin
                //check if it will reach the max amount with other donation
                tmp ?:= contributors[caller] : "Error";
                if checkTotal(tmp) + transferred > maxAmount then
                    fail("Reached max Amount");
                
                tmp.prepend(transferred); //add new donation with the other
                contributors.put(caller, tmp) //update value
            end
            else
                contributors.put(caller, [transferred]) //add new donator
            end
        else
            fail("At this state you can't call this entry");
        
        //check if ceiling is reached
        if balance + transferred >= ceiling then
            //call transition
            transfer 0tz to entry self.airdrop_()
        
    }
    ```
    invocata al momento della donazione, verifica che al cifra sia corretta e aggiorna `contributors`

*   ```
    entry checkTime(){
    //check if time is over
    if now > endDate then
        if balance > floorPrice then begin
            isSuccess := true;
            transfer 0tz to entry self.airdrop_() //state change to airdrop
            end
        else 
            for (x,y) in contributors do
                transfer checkTotal(y) to x //start refund 
            done;
            transfer 0tz to entry self.refund_() //otherwise change to refund
    }
    ```
    Verifica se la scadenza sia stata raggiunta e nel caso se il CrowfFunding abbia avuto o meno successo.

* ```
    entry dropToken(addr : address){
    var mapDon : map<address, tez> = [];
    if state = airdrop then begin
        //airdrop newToken
        for (x,y) in contributors do
            mapDon.put(x, checkTotal(y))
        done;
        //transfer balance to addr call airdrop<
        transfer balance to addr call airdrop<map<address, tez>>(mapDon)
        end
    else
        fail("At this state you can't call this entry")
    }
    ```
    Si occupa di richiamare lo [SC](#TokenGen) che si occupa dell'airdrop.

#### Function

*   ``` 
    function checkTotal(lst : list<tez>) : tez {
    var total : tez = 0utz;
    
    //sum all the elements of list
    for e in lst do
        total += e
    done;

    return total
    }   
    ```
    Calcola il totale delle donazioni di ogni contribuente.

<br><br>

### TokenGen
#### Constant and Variable
* `supply : int = 12000` : stabilisce la supply totale del nuovo token.
* `contributors : map<address, tez> = []` : tiene conto dei donatori e del numero di token che riceveranno.

### EntryPoint
*   ``` 
    entry airdrop(mapDon : map<address, tez>){
    //add to contributors
    for (x,y) in mapDon do
        contributors.put(x, y*1200)
    done
    }
    ```
    Simula l'invio dei token ai contribuenti inserendo l'ammontare corrispondente in **contributors**.

