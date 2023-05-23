# HTLC
The Hash Timed Locked Contract (HTLC) involves two users
and allows one participant to commit to a secret and reveal it afterward.
The commit is the SHA256 digest of the secret (a bitstring).
Upon contract creation, the committer:
- deposits collateral (in native cryptocurrency) in the contract;
- specifies a deadline for the secret revelation;
- specifies the receiver of the collateral, 
in case the deposit is not revealed within the deadline.
 .

## State Variables
- `deadline` : deadline to perform **timeout**
- `committer` : who creates the contract a can call **reveal**
- `receiver` : who can call **timeout**
- `hash` : secret between the two users

## EntryPoints
- `commit()` : to commit the secret
- `reveal()` : which requires the caller to provide a preimage of the commit,
and transfers the whole contract balance to the committer
- `timeout()` : which can be called only after the deadline, and
and transfers the whole contract balance to the receiver

## Use Cases
### Trace 1
1. The committer creates the contract, setting a deadline of 100 rounds;
1. After 50 rounds, A performs the **reveal** action.
### Trace 2

1. The committer creates the contract, setting a deadline of 100 rounds;
1. After 100 rounds, the receiver performs the **timeout** action.