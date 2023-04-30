# SMARTPY [Link](https://github.com/TheMastro-11/LearningTezos/blob/contracts/TokenTransfer/SmartPy/TokenTransfer.py)
In this version of SmartPy, there are one smart contract and one scenario:
* [TokenTransfer](#TokenTransfer);


## TokenTransfer:

### Attributes:

*  `owner` : The owner for the new token
*  `token_info` : the token information

### EntryPoints:

#### Mint
* ```
   @sp.entry_point
    def mint(self, owner, token_info):
        #get token_id
        token_id = self.data.last_token_id
        #mint new NFT
        self.data.ledger[token_id] = owner
        self.data.token_metadata[token_id] = sp.record(token_id = token_id, token_info = token_info)
        self.data.last_token_id =+ 1

    ```
    The creation of a new unique token.



## Test Scenario
The SP [scenario](https://smartpy.io/docs/scenarios/testing/) allows us to test the entry points and classes we have created before actual publication on chain.