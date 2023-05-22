# SmartContract Interactions
Calling an **entry-point** requires ,like other transactions on chain, a specific fee:
* *baker-fee*
* *storage-fee* = in this case represents the ***field**-change* from the initial state to the new one.
[1](#references)

## Simple Transfer
In this SC can be called two differents entry-points.
The first one is the *deposit* and requires a total fee of **0,007473tez**:
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

## Hash Timeed Locked Contract
In this SC can be called three differents entry-points.
The first one is *Commit* and requires a total fee of **0,02603tez**:
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
| *baker-fee* | 0,000786tez |
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


### Low rates
The fees showed above are the standard one proposed by the RPC [2](#references) during deployment.
Doing various tests can be found lowest fees, these are the ones I found:
| Contract | EntryPoint | Lowest Fee |
| - | - | :-: |
| SimpleTransfer | Deposit |  0,00044tez |
| SimpleTransfer | Withdraw | 0,0012tez |
| HTLC | Commit | 0,0006tez |
| HTLC | Reveal | 0,00055tez |
| HTLC | Timeout | 0,00055tez |
| TokenTransfer | Mint | 0,0415tez |
| TokenTransfer | Transfer | 0,00075tez |
| TokenTransfer | Update_operators | 0,01743tez |

### Refernces 
1. At the beginning to do the tests I used the SmartPy platform and after a personalized [script](https://github.com/TheMastro-11/SmartContractTestScript-By-Taquito-) using [Taquito](https://tezostaquito.io/).
2. RPC stands for ['Remote Procedure Call'](https://en.wikipedia.org/wiki/Remote_procedure_call), widely use in the IT. In this case it's used to gain information from the blockchain.
