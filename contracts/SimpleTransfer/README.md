# Simple transfer
The contract SimpleTransfer allows a user to
deposit an amount of native cryptocurrency in the contract,
and to specify a recipient.
At any later time, the recipient can withdraw any fraction of the funds
available in the contract.
 
## State Variables
- `receiver` 

## EntryPoints
- `deposit()` 
- `withdraw()` 

## Use Case
1. Pippo wants to send 100tz to Sofia as a gift.
2. He sends money to the contract and knows she will withdraw that on her birthday.
