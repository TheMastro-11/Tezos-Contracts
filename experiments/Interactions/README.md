# Contract Interaction Fees
Here are all the interaction costs of each entrypoints of every [contract](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts) developed.
At the beginning to do the tests I used the SmartPy platform and after a personalized [script](https://github.com/TheMastro-11/SmartContract-Execution-Costs-By-Taquito) using [Taquito](https://tezostaquito.io/).

## Simple Transfer
In this SC can be called two differents entry-points.
The first one is the *deposit* and requires a total fee of **0,00719tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00044tez |
| *storage-fee* | 0,00675tez |
| *gas* | 2141gu |
| *bytes* | 27 |

The second one is *Withdraw*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,0012tez |
| *gas* | 1206gu |


## Auction
In this SC can be called two different entry-points.
The first one is the *bid* and requires a total fee of **0,015545tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000545tez |
| *storage-fee* | 0,015tez |
| *gas* | 2343gu |
| *bytes* | 60 |

The second one is *getWinner*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000438tez |
| *gas* | 1211gu |

## King of Tezos
In this SC can be called two different entry-points.
The first one is the *newKing* and requires a total fee of **0,010536tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000536tez |
| *storage-fee* | 0,01tez |
| *gas* | 1210gu |
| *bytes* | 40 |

The second one is *killKing*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000436tez |
| *gas* | 1209gu |

## Crowd Funding
In this SC can be called three differents entry-points.
The first one is the *checkResult*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000567tez |
| *gas* | 1211gu |

The second one is *contribute* and requires a total fee of **0,010048**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000548tez |
| *storage-fee* | 0,0095tez 
| *gas* | 2285gu |
| *bytes* | 38 | 

The second one is *refund*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000535tez |
| *gas* | 1211gu |


## Hash Timed Locked Contract
In this SC can be called three differents entry-points.
The first one is *commit* and requires a total fee of **0,0246tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,0006tez |
| *storage-fee* | 0,024tez |
| *gas* | 2220gu |
| *bytes* | 96 |

The second one is *reveal*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00055tez |
| *gas* | 1214gu |

The third one is *timeout*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00055tez |
| *gas* | 1211gu |

## Token Transfer
For this SC I tested three differents entry-points.
Two of them are by default for FA2 contracts.
The first one, created by me, is *mint* and requires a total fee of **0,05891tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00091tez |
| *storage-fee* | 0,058tez |
| *gas* | 3311gu |
| *bytes* | 232 |

The second is *transfer*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00075tez |
| *gas* | 2153gu |

The third is *update_operators* and requires a total fee of **0,017467**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000717tez |
| *storage-fee* | 0,01675tez |
| *gas* | 1.457gu |
| *bytes* | 67 |
Actually, this entrypoint has two different operation:
* add
* remove
The first one, shows above, costs more because requires a storage change meanwhile the *baker-fee* is the same.


## Comparison
| Contract | EntryPoint | Cost |
| - | - |:-: | 
| Simple Transfer | deposit | 0,00719tez |
| Simple Transfer | withdraw | 0,0012tez  |
| Auction | bid | 0,015545tez | 
| Auction | getWinner | 0,000438tez | 
| King of Tezos | newKing| 0,010536tez |
| King of Tezos | killKing | 0,000436tez |
| Crowd Funding | checkResult | 0,000567tez |
| Crowd Funding | contribute |0,010048tez |
| Crowd Funding | refund | 0,000535tez |
| HTLC | commit | 0,0246tez |
| HTLC | reveal | 0,00055tez |
| HTLC | timeout | 0,00055tez |
| Token Transfer | mint | 0,05891tez |
| Token Transfer | transfer | 0,00075tez |
| Token Transfer | update_operators | 0,017467tez |

The main differences between the transaction costs for deployment are made by the *storage-fee*, so how many state variables are changed.
