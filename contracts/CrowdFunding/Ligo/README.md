# LIGO [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/Ligo/CrowdFunding.jsligo)
In the Ligo version we find only one Smart Contract:
* [CrowdFunding](#CrowdFunding).

    The reason is that the language in question does not allow us a [map management](#main-issues) like the other two and therefore it is not possible to complete our Use Case.

## CrowdFunding

### Type
* `holder = map <address, list<tez>` = type used to track `contributors`.
    In Ligo it is highly convenient to use *type-alias* to make easier to understand the use of *nested* types as in this case.

### Attributes
* `startDate : timestamp = Tezos.get_now()` = start date
* `endDate : timestamp = startDate + 5` = end date given in days
* `minAmount : tez  = 10 as mutez` = minimum donation
* `maxAmount : tez = 1000 as mutez` = maximum donation
* `ceiling : tez = 100000 as mutez` = financial goal
* `floorPrice : tez = 200 as mutez` = minimum target to be reached

    As you can see there is no map of *contributors* since the language does not allow us to manage global variables. In fact `contributors` will be declared within the [Main](#Main).

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
    Invoked at the time of donation, verify that the amount is correct and:
    * if the donor is new add it to the map;
    * if the donor already exists -theoretically- it should update the donation list, actually this [is not possible](#main-issues).


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
    Check that `floorPrice` is reached, if positive updates `isSuccess` otherwise refunds the `contributors`. The function returns the list of transactions that will be returned at the end of the [Main](#Main) so that they are actually recorded on the chain.

### Main Issues
Unlike other programs Ligo does not allow a convenient management of maps and lists.
Specifically I found difficult and without solution:
* Iterate a map to find a specific element, as in case you need to check whether a *address* is already present or not.
* Manipulate lists to extract an item, get the *tail* or concatenate two different items. The main problem I found in the transition from type `option<list<>>` to `list<>` required when using the function `List.tail_opt()` to get a substring to join with another later.
* Access `contributors` from any function or entrypoints via global variable.
* Ligo requires that you always return a list of operations at the end of the [Main](#Main) in order to save them on chain, which means you have to call the main function *x* times in *y* different ways. If you want to donate, [Main](#Main) will return the updated map of contributors, if you want to check the status of crowdfunding it will have to return either the [list of transactions for the refund](#checkending) or the call to the SC that takes care of the new Airdrop etc...