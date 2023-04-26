# Calculation Fees
A part of the work in this project also consists in the study of calculation fees on the Texos's Blockchain.

### The formula
On the official documentation can be found a formula that describes how much costs a transaction.
The standard unit is the **mutez**, 1 tez = 1.000.000 mutez.
The minimal unit is the **nano-tez**, 1 mutez = 1000 nano-tez 

Let: 
* Minimal Fees: minFminF​
* Size of the operation (in bytes "BB"): ss 
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

### Contracts
Three differents contracts from this repository are used for these experiments:
* [Simple Transfer](https://github.com/TheMastro-11/LearningTezos/blob/main/contracts/SimpleTransfer)
* [HTLC](https://github.com/TheMastro-11/LearningTezos/blob/main/contracts/SimpleTransfer)
* Token Transfer (NOT DEVELOPED YET)

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

## SmartContract Deploy
The transaction cost for SCdeploy is composed by two types:
* *baker-fee* 
* *burn-fee* = divided in:
  1. *storage-fee* = as defined [above](#the-formula)
  2. *allocation-fee* = a fix amount for every contract created on chain.

The *burn-fee* doesn't go to anyone differently then the first one, that's the great difference between **Tez Transaction** and **SmartContract Transaction**.
Actually an admin can add a balance amount as starter for the contract, that amount must be added to the total cost.

### Simple Transfer
Simple Transfer requires a total of **0,114275tez** to be deployed:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000775tez |
| *burn-fee* | 0,1135tez |
| *gas* | 1454gu |
| *bytes* | 454 |

The *burn-fee* are divided in:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,04925tez |
| *allocation-fee* | 0,06425tez |

All the details can be found [here](https://better-call.dev/ghostnet/KT1JPWgfwodv4j2zD1FATzfGsRCNkAhfVa7D/operations) or [here](https://ghostnet.tzkt.io/KT1JPWgfwodv4j2zD1FATzfGsRCNkAhfVa7D/operations/).

### Hash Timed Locked Contract
HTLC requires a total of **0,214686** to be deployed:

| Type | Cost |
| - | :-: |
| *baker-fee* | 0,001186tez |
| *burn-fee* | 0,2135tez |
| *gas* | 1568gu |
| *bytes* | 597 |

The *burn-fee* are divided in:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,14925tez |
| *allocation-fee* | 0,06425tez |


All the details can be found [here](https://ghost.tzstats.com/oooBfAN2zGv4Mg3GNs8K2zQw7RH3KbmY6bhp8zAq7jM6tKeDePr/162607792171).

### Token Transfer
(Working on)

### Differences
The main differences between the transaction costs for deploy are made by the storage fee.
Alongside the *allocation-fee* is the same.
[4](#references)
(Working on)

## SmartContract Interaction
Calling an **entry-point** requires ,like other transactions on chain, a specific fee:
* *baker-fee*
* *storage-fee* = in this case represents the ***field**-change* from the initial state to the new one.

### Simple Transfer
In this SC can be called two differents entry-points.
The first one is the *deposit* and requires a total fee of ** 0,007473tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000723tez |
| *storage-fee* | 0,00675tez |
| *gas* | 2141gu |
| *bytes* | 27 |

The *storage-fee* is calculated because the Address field is changed.
The second one is *Withdraw*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00142tez |
| *gas* | 1206gu |

*Storage-fee* is not required because there's no change in the Contract field.

### Hash Timeed Locked Contract
In this SC can be called three differents entry-points.
The first one is *Commission* and requires a total fee of **0,02603tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00078tez |
| *storage-fee* | 0,024tez |
| *gas* | 2220gu |
| *bytes* | 96 |

The second one is *Reveal*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000597tez |
| *gas* | 1214gu |

The third one is *Timeout*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,0007tez |
| *gas* | 1211gu |


#### Low rates
The fee showed above are the standard one proposed by the RPC [5](#references) during deployment.
Doing various tests can be found lowest fees, these are the ones I found:
| Contract | EntryPoint | Lowest Fee |
| - | - | :-: |
| SimpleTransfer | Deposit |  0,00044tez |
| SimpleTransfer | Withdraw | 0,0012tez |
| HTLC | Commission | 0,0006tez |
| HTLC | Commission | 0,00055tez |
| HTLC | Commission | 0,00055tez |




## References
1. [Economics and Rewards](https://opentezos.com/tezos-basics/economics-and-rewards/)
2. The wallet used for the test was the TempleWallet
3. *Baker-fee* are the fees paid to bakers, the [bakers](https://opentezos.com/baking/baking_explained/) are the *miner*-equivalent for other blockchains (with some differents).
4. A detailed explaination of how gas and fees are calculated can be found [here](https://kitchen.stove-labs.com/docs/knowledge/tezos_protocol/operations/gas-fees/).
5. RPC stands for ['Remote Procedure Call'](https://en.wikipedia.org/wiki/Remote_procedure_call), widely use in the IT. In this case it's used to gain information from the blockchain.
