# ARCHETYPE [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/CrowdFunding.arl)

Also in the version of Archetype we find two SCs:
* [CrowdFunding](#CrowdFunding);
* [TokenGen](#TokenGen).

### CrowdFunding
#### States:
* `funding` : initial state in which donations are allowed. It ends in two cases: either the time expires or the economic objective is reached.
* `airdorp` : final successful state in which the [SC](#TokenGen) , that deals with the Airdrop, is invoked.
* `refund` : final state of failure in which all donors are refunded.

Through the *states* you can check the progress of crowdfunding. 
In addition, certain actions can only be performed in certain *states* and this avoids problems or bugs related to improper use of functions.

#### Constant and Variables:
*  `startDate : date = now` : start date

*  `endDate : date = now + 5s` : end date given in days

*  `contributors : map<address, list<tez>> = []` : map of donors

*  `minAmount : tez = 10utz` : minimum donation

*  `maxAmount : tez = 1000utz` : maximum donation

*  `ceiling : tez = 100000utz` : financial goal

*  `floorPrice : tez = 200utz` : minimum target to be reached

*  `isSuccess : bool = false` : success indicator at the end of the fundraising

#### Transition
* `airdrop_ (funding -> airdrop)` : is invoked by the function ***contribute** and **checkTime**. This ensures that the status is changed to **Airdrop**.
* `refund_ (funding -> refund)` : is invoked by the **checkTime*** function. Ensures the status switch **refund**.

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
    Invoked at the time of donation, verify that the amount is correct and update `contributors`.

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
    Check whether the expiration date has been reached and whether or not CrowdFunding has been successful.

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
    It is responsible for calling up the [SC](#TokenGen) that deals with the Airdrop.

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
    Calculate the total donations of each contributor.

<br><br>

### TokenGen
#### Constant and Variable
* `supply : int = 12000` :indicate the total supply of the token.
* `contributors : map<address, tez> = []` :  keep track of contributors and the number of tokens they will receive.

### EntryPoint
*   ``` 
    entry airdrop(mapDon : map<address, tez>){
    //add to contributors
    for (x,y) in mapDon do
        contributors.put(x, y*1200)
    done
    }
    ```
    Simulate the sending of tokens to donators by inserting the corresponding amount in `contributors`.

