# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/SmartPy/CrowdFunding.py)
Nella versione di SmartPy troviamo due SC e uno scenario:
* [CrowdFunding](#CrowdFunding);
* [TokenGen](#TokenGen);
* [Test Scenario](#Test-Scenario).


## CrowdFunding:

### Attributes:

*  #### startDate `= sp.timestamp(0)` : data di inizio

*  `endDate = x` : data di fine espressa in giorni

*  (#### contributors) `= sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TList(sp.TMutez) )` : mappa dei donatori

*  `minAmount = sp.mutez(10)` : minima donazione

*  `maxAmount = sp.mutez(1000)` : massima donazione

*  `ceiling = sp.mutez(100000)` : obiettivo economico

*  `floor = sp.mutez(200)` : tetto minimo da raggiungere

*  `isSuccess = sp.bool()` : indicatore successo al termine della raccolta

### EntryPoints:

* ```

    @sp.entry_point

    def checkTime(self, time):

    diffTime = time - self.data.startDate

    sp.verify(diffTime <= self.getHours(), message = "The time is over")

    ```

    Verifica se la scadenza sia stata raggiunta e nel caso restituisce un messaggio di errore.


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

    Invocata al momento della donazione, verifica che al cifra sia corretta e aggiorna [contributors](#contributors)

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

    verifica che `floor` sia raggiunto, in caso positivo aggiorna `isSuccess` altrimenti rimborsa i `contributors`
  

* ```

    @sp.entry_point

    def endFunding(self, cAddress):

    #airdrop new token

    c = sp.contract(sp.TMap(sp.TAddress, sp.TList(sp.TMutez)), cAddress, entry_point = "airdrop").open_some()

    sp.transfer(self.data.contributors, sp.balance, c)

    ```

    si occupa di richiamare lo [SC](#TokenGen) che si occupa dell'airdrop



 
### Methods:

*  ```

    def getHours(self):

    return sp.compute(self.data.endDate * 24)

    ```

    trasforma x giorni nel numero di ore corrispondenti

  

*   ```

    def checkTotal(self, list_):

    total = sp.local("totale", sp.mutez(0))

    sp.for j in list_:

    with sp.match_cons(list_) as x1:

    total.value += x1.head

    list_ = x1.tail

    return total.value

    ```

    calcola il totale delle donazioni di ogni contribuente

<br><br>

## TokenGen:

### Attributes:

*  `supply = 120000000` : indica la totale supply del token

*  `contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TNat` : tiene conto dei donatori e del numero di token che riceveranno
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

    Simula l'invio dei token ai contribuenti inserendo l'ammontare corrispondente in **contributors**.

  
  

## Test Scenario

Lo scenario in SP ci permette di testare gli entry_points e le classi da noi realizzate prima di un'effettiva pubblicazione sulla chain.

[Link](https://smartpy.io/docs/scenarios/testing/)


## Notes
Nella versione di SmartPy non è possibile l'utilizzo degli *states* così come sono intesi in *Archetype* quindi non sono presenti e di conseguenza non è possibile effettuare un controllo sull'invocazione degli entrypoints.
