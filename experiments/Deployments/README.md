# Contract Deployment Fees
The transaction cost for SCdeploy is composed of two types:
* *baker-fee* 
* *burn-fee* = divided in:
  1. *storage-fee* = as defined [before](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/experiments)
  2. *allocation-fee* = a fixed amount for every contract created on chain.

The *burn-fee* doesn't go to anyone different than the first one, that's the great difference between **Tez Transaction** and **SmartContract Transaction**.
Actually, an admin can add a balance amount as a starter for the contract, that amount must be added to the total cost.
[1](#references)


## Simple Transfer
Simple Transfer requires a total of **0,114275tez** to be deployed:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000775tez |
| *burn-fee* | 0,1135tez |
| *gas* | 1454gu |
| *bytes* | 454 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,04925tez |
| *allocation-fee* | 0,06425tez |

All the details can be found [here](https://better-call.dev/ghostnet/KT1JPWgfwodv4j2zD1FATzfGsRCNkAhfVa7D/operations) or [here](https://ghostnet.tzkt.io/KT1JPWgfwodv4j2zD1FATzfGsRCNkAhfVa7D/operations/).

## Hash Timed Locked Contract
HTLC requires a total of **0,214686tez** to be deployed:

| Type | Cost |
| - | :-: |
| *baker-fee* | 0,001186tez |
| *burn-fee* | 0,2135tez |
| *gas* | 1568gu |
| *bytes* | 597 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,14925tez |
| *allocation-fee* | 0,06425tez |


All the details can be found [here](https://ghost.tzstats.com/oooBfAN2zGv4Mg3GNs8K2zQw7RH3KbmY6bhp8zAq7jM6tKeDePr/162607792171).

## Token Transfer
TokenTransfer requires a total of **0,5145tez** to be deployed:

| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00225tez |
| *burn-fee* | 0,51225tez |
| *gas* | 2109gu |
| *bytes* | 1792 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,448tez |
| *allocation-fee* | 0,06425tez |


All the details can be found [here](https://ghost.tzstats.com/opPfZTiW9ktCULe48nb9QZpA8cm3QooyftcZ3niMuhbUsUXVqS7/166190776352).

## Auction
Auction requires a total of **0,297788tez** to be deployed:

| Type | Cost |
| - | :-: |
| *baker-fee* | 0,001538tez |
| *burn-fee* | 0,29625tez |
| *gas* | 1764gu |
| *bytes* | 928 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,232tez |
| *allocation-fee* | 0,06425tez |


All the details can be found [here](https://better-call.dev/ghostnet/KT19Yw7uupmjzkCUsAmLEsujpZoR3LHwHjTJ/operations).

## Crowd Funding
CrowdFunding requires a total of **0,289781tez** to be deployed:

| Type | Cost |
| - | :-: |
| *baker-fee* | 0,001531tez |
| *burn-fee* | 0,28825tez |
| *gas* | 1682gu |
| *bytes* | 896 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,224tez |
| *allocation-fee* | 0,06425tez |


All the details can be found [here](https://better-call.dev/ghostnet/KT1XQ3Vkxqd54kbpFozpSGd676zdSfPMqrPS/operations).

## King of Tezos
King of Tezos requires a total of **0,161482tez** to be deployed:

| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000982tez |
| *burn-fee* | 0,1605tez |
| *gas* | 1510gu |
| *bytes* | 385 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,09625tez |
| *allocation-fee* | 0,06425tez |


All the details can be found [here](https://better-call.dev/ghostnet/KT1XTv6oPMgX6RbepELh8E6R1GCYU6rArX1x/operations).

### Differences
The main differences between the transaction costs for deployment are made by the storage fee, so how many state variables are generated.
Alongside the *allocation-fee* is the same.
[2](#references)

### References
1. For deployment I used the SmartPy platform.
2. A detailed explanation of how gas and fees are calculated can be found [here](https://kitchen.stove-labs.com/docs/knowledge/tezos_protocol/operations/gas-fees/).
