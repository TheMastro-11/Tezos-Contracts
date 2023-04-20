# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/BlindAuction/SmartPy/BlindAuction.py)
In this version of SmartPy, there's one smart contract:
* [BlindAuction](#blindauction).


## BLIND AUCTION:

### ATTRIBUTES:

*  `bidders = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TMutez)` : map of donors

*  `top = sp.record(winning = sp.list(l = [], t = sp.TAddress), amount = sp.mutez(0))` : list of winning alongside the biggest amount

*  `minBid = sp.mutez(0)` : minimum donation

### ENTRYPOINTS:

* ```
    @sp.entry_point
        def bid(self):
            #check if a bidder has already partecipated
            sp.verify(self.data.bidders.contains(sp.sender) == False, message = "This address is already registered")
            #add to bidder
            self.data.bidders[sp.sender] = sp.amount

            #check if is top bid
            sp.if sp.amount >= self.data.top.amount:
                sp.if sp.amount > self.data.top.amount:
                    self.data.top = sp.record(winning = [sp.sender], amount = sp.amount)
                sp.else:
                    newList = sp.cons(sp.sender, self.data.top.winning)
                    self.data.top = sp.record(winning = newList, amount = sp.amount)

    ```
    Check if the sender already exists and if his amount is valid. After that it adds bidder on map.


*   ```
    @sp.entry_point
    def getWinner(self):
        #check how many winners
        listTemp = sp.local("listTemp", self.data.top.winning)
        #remove temporarily winners from map
        sp.for i in listTemp.value:
            with sp.match_cons(listTemp.value) as x1:
                adTemp = x1.head
                listTemp.value = x1.tail
                #delete winner from map
                del self.data.bidders[adTemp]
        
        #rimborso 
        addressList = sp.local("addressList", self.data.bidders.keys())
        sp.for i in addressList.value:
            with sp.match_cons(addressList.value) as x1:
                address = x1.head
                addressList.value = x1.tail
                sp.send(address, self.data.bidders[address])
                del self.data.bidders[address]
                
        #re-list
        listTemp.value = self.data.top.winning
        sp.for j in listTemp.value:
            with sp.match_cons(listTemp.value) as x1:
                address = x1.head
                listTemp.value = x1.tail
                self.data.bidders[address] = self.data.top.amount

        #case: more then 1 winners
        sp.if sp.len(self.data.bidders) > 1:
            self.data.minBid = self.data.top.amount
            self.data.top = sp.record(winning = [], amount = sp.mutez(0))
            adList = sp.local("adList",self.data.bidders.keys())
            sp.for k in adList.value:
                with sp.match_cons(adList.value) as x1:
                    address = x1.head
                    adList.value = x1.tail
                    sp.send(address, self.data.minBid)

    ```
    Removes all the loosers from the map and refunds them. Only the winner/s remain/s.


