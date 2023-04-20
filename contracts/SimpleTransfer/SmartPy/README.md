# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/SimpleTransfer/SmartPy/SimpleTransfer.py)
In this version of SmartPy, there are one smart contract and one scenario:
* [SimpleTransfer](#SimpleTransfer);


## SimpleTransfer:

### Attributes:

*  `receiver` : the only address who can withdraw money

### EntryPoints:

#### Deposit
* ```
   @sp.entry_point
    def deposit(self, receiver):
        #update data
        self.data.receiver = sp.some(receiver)

    ```
    The caller can deposit money and indicates the `receiver`.


#### Withdraw
*   ```
    @sp.entry_point
    def withdraw(self):
        #check receiver
        sp.verify(self.data.receiver == sp.some(sp.sender), "Wrong Address")

        #withdraw
        sp.send(self.data.receiver.open_some(), sp.balance)

    ```
    The `receiver` can withdraw money.


## Test Scenario
The SP [scenario](https://smartpy.io/docs/scenarios/testing/) allows us to test the entry points and classes we have created before actual publication on the chain.

