# Token Transfer
The contract TokenTransfer allows a user to
transfer a FA2 token to an other address.

There will be three actors:
- Token Contract, that contains in its storage all the Token(s) Metadata and owner(s).
- First Owner, who mint a token *x*.
- Second Owner, who receive the token *x* from the First Owner.

## State Variables
- `Last_token_id` : last id used for mint a token
- `Ledger` : The map of token(s) minted and their current owner(s)
- `Metadata` : Token Contract Metadata
- `Operators` : Other address(es) that can operate with a token in addition to owner
- `Token_metadata` : Metadata for each token minted

## EntryPoints
- `mint()` : mint a new token
- `transfer()` : transfer a token from old to new owner

All Variables and EntryPoints(except **mint**) are imported from the [FA2 Library](https://legacy.smartpy.io/ide?template=fa2_lib.py).

## Use Case
1. Mario mint a token and give as input a metadata created by himself.
2. Then he decides to sell to Pippo privately.
3. After the **transfer** entrypoint is called Pippo became the new owner.