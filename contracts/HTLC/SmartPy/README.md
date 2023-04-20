# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/HTLC/SmartPy/HTLC.py)
In this version of SmartPy, there are one smart contract and one scenario:
* [HashedTimeLockContract](#HashedTimeLockContract);


## HashedTimeLockContract:

### Attributes:

*  `collateral` : amount used as collateral

*  `deadline` : end date given in block level

*  `commiter` : contract caller

*  `receiver` : receiver

*  `hash` : keccak hash from a bitstring used for reveal
  

### EntryPoints:

#### Commission
* ```
   @sp.entry_point
    def commission(self, deadline, receiver, hash):
        #save into data
        self.data.collateral = sp.some(sp.amount)
        self.data.deadline = sp.some(sp.level + deadline)
        self.data.receiver = sp.some(receiver)
        self.data.hash = sp.some(hash)
        
        self.data.commiter = sp.some(sp.sender)

    ```
    First call for contract, used to set the collateral, deadline, receiver and hash


#### Reveal
*   ```
    @sp.entry_point
    def reveal(self, word):
        #hash
        bytes = sp.pack(word) 
        hash = sp.keccak(bytes) #created
        sp.verify(self.data.hash == sp.some(hash), "Wrong word") #checked

        #check receiver
        sp.verify(self.data.receiver == sp.some(sp.sender), "Wrong Address")
        #transfer collateral to receiver
        sp.send(self.data.receiver.open_some(), self.data.collateral.open_some())

    ```
    Action called by receiver to withdraw the `collateral`.


#### Timeout
*  ```
    @sp.entry_point
    def timeout(self):
        #check if deadline is reached and if sender is the commiter
        sp.verify(self.data.deadline == sp.some(sp.level), "Deadline not reached")
        sp.verify(self.data.commiter == sp.some(sp.sender), "You are not the commiter")

        #transfer collateral to commiter
        sp.send(self.data.commiter.open_some(), self.data.collateral.open_some())

    ```
    Action called by `commiter` when time is up to retake the money used as `collateral`.
    

## Test Scenario
The SP [scenario](https://smartpy.io/docs/scenarios/testing/) allows us to test the entry points and classes we have created before actual publication on the chain.

