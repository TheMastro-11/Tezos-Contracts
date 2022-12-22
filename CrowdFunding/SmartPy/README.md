# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/SmartPy/CrowdFunding.py)
In this version of SmartPy, there are two smart contracts and one scenario:
* [CrowdFunding](#CrowdFunding);
* [TokenGen](#TokenGen);
* [Test Scenario](#Test-Scenario).


## CrowdFunding:

### Attributes:

*  `startDate = sp.timestamp(0)` : start date

*  `endDate = x` : end date given in days

*  `contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TList(sp.TMutez) )` : map of donors

*  `minAmount = sp.mutez(10)` : minimum donation

*  `maxAmount = sp.mutez(1000)` : maximum donation

*  `ceiling = sp.mutez(100000)` : financial goal

*  `floor = sp.mutez(200)` : minimum target to be reached

*  `isSuccess = sp.bool()` : success indicator at the end of the fundraising

### EntryPoints:

* ```

    @sp.entry_point

    def checkTime(self, time):

    diffTime = time - self.data.startDate

    sp.verify(diffTime <= self.getHours(), message = "The time is over")

    ```
    Checks if the deadline has been reached and returns an error message if it has.


*   ```

    @sp.entry_point

    def contribute(self):

    #check if ceiling is reached

    sp.verify(sp.balance + sp.amount <= self.data.ceiling, message = "Ceiling reached")

    #check if amount is between min and max

    sp.verify(sp.amount >= self.data.minAmount, message = "Amount too low")

    sp.verify(sp.amount <= self.data.maxAmount, message = "Amount too high")

    #add on list

    sp.if (self.data.contributors.contains(sp.sender)):

    #check if it will reach the max amount with other donation

    prvDons = sp.local("prvDons", sp.mutez(0))

    prvDons = self.checkTotal(self.data.contributors[sp.sender])

    sp.verify( prvDons + sp.amount < self.data.maxAmount, message = "Max Amount Reached")

    self.data.contributors[sp.sender].push(sp.amount) #se esiste già

    sp.else:

    self.data.contributors[sp.sender] = sp.list([sp.amount], t = sp.TMutez) #inserisco indirizzo contribuente

    ```
    Called at the time of donation, checks that the amount is correct and updates `contributors`.

* ```

    @sp.entry_point

    def checkFloor(self):

    #check if floor is reached

    sp.if sp.balance < self.data.floor:

    #if not refund all donators

    addressList = sp.local("addressList", self.data.contributors.keys())

    sp.for i in addressList.value:

    with sp.match_cons(addressList.value) as x1:

    address = x1.head

    addressList.value = x1.tail

    sp.send(address, self.checkTotal(self.data.contributors[address]))

    sp.else:

    #otherwise crowdfunding is finished successfully

    self.data.isSuccess = True

    ```
    Checks if `floorPrice` has been reached, if so updates `isSuccess` otherwise it refunds `contributors`.
  

* ```

    @sp.entry_point

    def endFunding(self, cAddress):

    #airdrop new token

    c = sp.contract(sp.TMap(sp.TAddress, sp.TList(sp.TMutez)), cAddress, entry_point = "airdrop").open_some()

    sp.transfer(self.data.contributors, sp.balance, c)

    ```
    Finalizes the crowdfunding sending the funds to the [SC](#TokenGen) for the airdrop.



 
### Methods:

*  ```

    def getHours(self):

    return sp.compute(self.data.endDate * 24)

    ```

    Convert x days into the corresponding number of hours.

  

*   ```

    def checkTotal(self, list_):

    total = sp.local("totale", sp.mutez(0))

    sp.for j in list_:

    with sp.match_cons(list_) as x1:

    total.value += x1.head

    list_ = x1.tail

    return total.value

    ```

    Calculate the total donations of each contributor.

<br><br>

## TokenGen:

### Attributes:

*  `supply = 120000000` : indicate the total supply of the token.

*  `contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TNat` : keep track of donors and the number of tokens they will receive.
<br>

### EntryPoints:
*   ```
    @sp.entry_point

    def airdrop(self, adMap):

    adList = sp.local("adList", adMap.keys())

    sp.for i in adList.value:

    with sp.match_cons(adList.value) as x1:

    address = x1.head

    adList.value = x1.tail

    self.data.contributors[address] = sp.utils.mutez_to_nat(self.checkTotal(adMap[address])) * 1200

    ```
    Simulate the sending of tokens to donators by inserting the corresponding amount in `contributors`.

  
  

## Test Scenario
The SP [scenario](https://smartpy.io/docs/scenarios/testing/) allows us to test the entry points and classes we have created before actual publication on the chain.


## Notes
In the SmartPy version, it is not possible to use *states* as they are intended in Archetype, so they are not present and therefore it is not possible to check the invocation of entry points.