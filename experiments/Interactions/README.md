# SmartContract Interactions
Calling an **entry-point** requires ,like other transactions on chain, a specific fee:
* *baker-fee*
* *storage-fee* = in this case represents the ***field**-change* from the initial state to the new one.
[1](#references)

## Simple Transfer
In this SC can be called two differents entry-points.
The first one is the *deposit* and requires a total fee of **0,00719tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00044tez |
| *storage-fee* | 0,00675tez |
| *gas* | 2141gu |
| *bytes* | 27 |

The *storage-fee* is calculated because the Address field is changed.
The second one is *Withdraw*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,0012tez |
| *gas* | 1206gu |

*Storage-fee* is not required because there's no change in the Contract field.

## Hash Timeed Locked Contract
In this SC can be called three differents entry-points.
The first one is *Commit* and requires a total fee of **0,0246tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,0006tez |
| *storage-fee* | 0,024tez |
| *gas* | 2220gu |
| *bytes* | 96 |

The second one is *Reveal*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00055tez |
| *gas* | 1214gu |

The third one is *Timeout*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00055tez |
| *gas* | 1211gu |

## Token Transfer
For this SC I tested three differents entry-points.
Two of them are by default for FA2 contracts.
The first one, created by me, is *Mint* and requires a total fee of **0,05891tez**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00091tez |
| *storage-fee* | 0,058tez |
| *gas* | 3311gu |
| *bytes* | 232 |

The second is *Transfer*:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,00075tez |
| *gas* | 2153gu |

The third is *Update_operators* and requires a total fee of **0,017467**:
| Type | Cost |
| - | :-: |
| *baker-fee* | 0,000717tez |
| *storage-fee* | 0,01675tez |
| *gas* | 1.457gu |
| *bytes* | 67 |
Actually this entrypoint has two differents:
* add
* remove
The first one costs more because requires a storage change meanwhile the *baker-fee* is the same.


## Blind Auction
In this SC can be called two differents entry-points.
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

## King of Tezos
In this SC can be called two differents entry-points.
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



### Refernces 
1. At the beginning to do the tests I used the SmartPy platform and after a personalized [script](https://github.com/TheMastro-11/SmartContractTestScript-By-Taquito-) using [Taquito](https://tezostaquito.io/).
