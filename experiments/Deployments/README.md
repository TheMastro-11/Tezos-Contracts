# Contract Deployment
Here are all the deployment costs of every [contract](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts) developed.

## Simple Transfer
Simple Transfer requires a total of **0,114275tez** to be deployed:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000775tez |
| *burn-fee* | 0,1135tez |
| *gas* | 1454gu |
| *bytes* | 197 |

The *burn-fee* are divided into the:
| Type | Cost |
| - | :-: |
| *storage-fee* | 0,04925tez |
| *allocation-fee* | 0,06425tez |

All the details can be found [here](https://better-call.dev/ghostnet/oohEy52J6bD2snRtQy84re9Tx5tbPiw87nsyrNbJDD1r4zkk6hX/contents)

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


All the details can be found [here](https://better-call.dev/ghostnet/onsVYi3GxNwkCYcBUBCpwpf6iKZjZXqBFjUFp6iyaCWQH6XnrCe/contents).

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


All the details can be found [here](https://better-call.dev/ghostnet/onsWLyAYL8kqWZDszvQYRhXpbmMS2p4cJHfqaboVigwHu86gwUz/contents).

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


All the details can be found [here](https://better-call.dev/ghostnet/ooxqG6tyNzg9owvz5jvoRM3tP7EeDVkqnyN5FP1UuKrbxSGjMyB/contents).

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


All the details can be found [here](https://better-call.dev/ghostnet/oooBfAN2zGv4Mg3GNs8K2zQw7RH3KbmY6bhp8zAq7jM6tKeDePr/contents).

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


All the details can be found [here](https://better-call.dev/ghostnet/opPfZTiW9ktCULe48nb9QZpA8cm3QooyftcZ3niMuhbUsUXVqS7/contents).


## Comparison
| Contract | Cost |
| - | :-: |
| Simple Transfer | 0,114275tez |
| Auction | 0,297788tez |
| Kinf of Tezos | 0,161482tez |
| Crowd Funding | 0,289781tez |
| HTLC | 0,214686tez |
| Token Transfer | 0,5145tez |

The main differences between the transaction costs for deployment are made by the *storage-fee*, so how many state variables are generated.
Alongside the *allocation-fee* is the same.
[1](#references)

## References
1. [Gas & Fees](https://kitchen.stove-labs.com/docs/knowledge/tezos_protocol/operations/gas-fees/) (n.d.), Stove Labs' Kitchen. Retrieved May 20, 2023.
