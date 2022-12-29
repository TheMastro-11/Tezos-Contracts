# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/KingOfTezos/SmartPy/King Of Tezos.py)
In this version of SmartPy, there's one contract:
* [BlindAuction](#blindauction).


## KING OF TEZOS:

### ATTRIBUTES:

*  `king = admin` : the realtime king, the default is the admin

*  `history = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TRecord(value = sp.TMutez, data = sp.TTimestamp))` : full history of all kings who bought the throne.

*  `floorPrice = sp.mutez(5000)` : start price to be king.

### EntryPoints:

* ```
    @sp.entry_point
    def newKing(self):
        #verify amount
        sp.verify(sp.amount == self.data.floorPrice, message = "Amount incorrect")
        #refund previous king
        #sp.if self.data.king != self.data.admin: with # send to admin the revenue
        sp.send(self.data.king, sp.amount)
        #update history
        self.data.history[sp.sender] = sp.record(value = sp.amount, data = sp.now)
        self.data.king = sp.sender
        #update price -> plus 10%
        self.data.floorPrice += sp.fst(sp.ediv(self.data.floorPrice, sp.nat(10)).open_some()) 
    ```
    Check if the amount is correct,then replaces the king and increases the price.


*   ```
    @sp.entry_point
    def killKing(self):
        #reset king
        self.data.king = sp.sender
        #reset floorPrice
        self.data.floorPrice = sp.mutez(5000)
    ```
    The timer ended and the king has to be 'killed'. The price is resetted.

