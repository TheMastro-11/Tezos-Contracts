# Calculation Fees
A part of the work in this project also consists in the study of calculation fees on the Texos's Blockchain.

### The formula
On the official documentation can be found a formula that describes how much costs a transaction.
The minimal unit is the *mutez*, 1 tez = 1.000.000 mutez. 

Let: 
* Minimal Fees: minFminF​
* Size of the operation (in bytes "BB"): ss 
  (The size "ss" is the number of bytes in the complete serialized operation).
* Gas used for the operation (in gas unit "gugu​"): gg
* Minimal nano-tez per byte: min(nꜩ/B)min(nꜩ/B)
* Minimal nano-tez per gas unit: min(nꜩ/gu)min(nꜩ/gu​)
* Gas unit cost in Tez is defined by the protocol. It does not depend on the fee market; it does not depend on arbitrary defaults in config files; etc 
  
Then:
$$Fees≥minF​+min(nꜩ/B)×s+min(nꜩ/gu​)×g$$

The transaction default values are:
* minF=100 µꜩminF​=100 µꜩ
* min(nꜩ/B)=250,000 nꜩ/B (250 µꜩ/B)min(nꜩ/B)=250,000 nꜩ/B (250 µꜩ/B)
* min(nꜩ/gu)=100 nꜩ/gumin(nꜩ/gu​)=100 nꜩ/gu​ [1](####References)

### Testnet
For concenience all the tests made are on the testnet, specifically the *GhostNet*.
This gives the opportunity to do unlimited tests whitout spending money or risk any cyber-attack from outside.
The testnets are widely used in all of SC's Blockchains (like Ethereum).

### Contracts
Three differents contracts from this repository are used for these experiments:
* [Simple Transfer](https://github.com/TheMastro-11/LearningTezos/blob/main/contracts/SimpleTransfer)
* [HTLC](https://github.com/TheMastro-11/LearningTezos/blob/main/contracts/SimpleTransfer)
* Token Transfer (NOT DEVELOPED YET)




#### References
[1 - Economics and Rewards](https://opentezos.com/tezos-basics/economics-and-rewards/)