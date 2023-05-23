# Calculation Fees
A part of the work in this project also consists in the study of calculation fees on the Texos's Blockchain.

### The formula
On the official [documentation](https://opentezos.com/tezos-basics/economics-and-rewards/) can be found a formula that describes how much costs a transaction.
The standard unit is the **mutez**, 1 tez = 1.000.000 mutez.
The minimal unit is the **nano-tez**, 1 mutez = 1000 nano-tez 

Let: 
* Minimal Fees: minF
* Storage Fee (in bytes "BB"): ss 
  (The size "ss" is the number of bytes in the complete serialized operation).
* Gas used for the operation (in gas unit "gugu​"): gg
* Minimal nano-tez per byte: min(nꜩ/B)
* Minimal nano-tez per gas unit: min(nꜩ/gu)
* Gas unit cost in Tez is defined by the protocol. It does not depend on the fee market; it does not depend on arbitrary defaults in config files; etc 
  
Then:
$$Fees≥minF​+min(nꜩ/B)×s+min(nꜩ/gu​)×g$$

The transaction default values are:
* minF=100 µꜩ
* min(nꜩ/B)=250,000 nꜩ/B (250 µꜩ/B)
* min(nꜩ/gu)=100 nꜩ/gu​ [1](#References)

### Testnet
For concenience all the tests made are on the testnet, specifically the *GhostNet*.
This gives the opportunity to do unlimited tests whitout spending money or risk any cyber-attack from outside.
The testnets are widely used in all of SC's Blockchains (like Ethereum).

## Tez Transactions
A simple transaction for 1,10,100 or 1000 tez as always the same gas cost of 1001gu and a three base fees ranges for differents frame time *more pay less wait*:
| Type | Cost |
| - | :-: |
| *Minimal* | 0,0001tez  |
| *Fast*    | 0,00015tez |
| *Rocket*  | 0,0002tez  |
| *Custom*  |  variable  | 

[2](#References)   
This amount will be added to the gas-cost.
For example a *minimal* fee transaction results in total of **0,000503tez** with **0,000403tez** in gas-fee, so 403 nꜩ/gu.
The minimal amount I used for a transaction is **0,00001tez** with a total *baker-fee* [3](#References) of **0,000414tez** with **0,000404tez** in gas-fee, so 404 nꜩ/gu.
The average nꜩ/gu ranges between 401 and 404.


## References
1. [Economics and Rewards](https://opentezos.com/tezos-basics/economics-and-rewards/)
2. The wallet used for the test was the TempleWallet
3. *Baker-fee* are the fees paid to bakers, the [bakers](https://opentezos.com/baking/baking_explained/) are the *miner*-equivalent for other blockchains (with some differents).
