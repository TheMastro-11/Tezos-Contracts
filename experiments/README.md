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
* *Minimal* = 0,0001tez
* *Fast* = 0,00015tez
* *Rocket* = 0,0002tez 
* *Custom* [2](#References)  

This amount will be added to the gas-cost.
For example a *minimal* fee transaction results in total of 0,000503tez with 0,000403tez in gas-fee, so 403 nꜩ/gu.
The minimal amount I used for a transaction is 0,00001tez with a total *baker-fee* [3](#References) of 0,000414 tez with 0,000404tez in gas-fee, so 404 nꜩ/gu.
In general the nꜩ/gu ranges between 401 and 404.

## SmartContract Deploy
The transaction cost for SCdeploy is composed by two types:
* *baker-fee* 
* *burn-fee* = divided in:
  1. *storage-fee* = as defined [above](#the-formula)
  2. *allocation-fee* = a fix amount for every contract created on chain.

The *burn-fee* doesn't go to anyone differently then the first one.
Actually an admin can add a balance amount as starter for the contract, that amount must be added to the total cost.

### Simple Transfer
Simple Transfer requires a total of 0,114275tez to be deployed:
* *baker-fee* = 0,000775tez
* *burn-fee* = 0,1135tez:
  1. *storage-fee* = 0,04925tez
  2. *allocation-fee* = 0,06425tez
* *gas* = 1454gu
* *bytes* = 454.

All the details can be found [here](https://better-call.dev/ghostnet/KT1JPWgfwodv4j2zD1FATzfGsRCNkAhfVa7D/operations) or [here](https://ghostnet.tzkt.io/KT1JPWgfwodv4j2zD1FATzfGsRCNkAhfVa7D/operations/).

### Hash Timed Locked Contract
HTLC requires a total of 0,248828tez to be deployed:
* *baker-fee* = 0,001328tez
* *burn-fee* = 0,2475tez:
  1. *storage-fee* = 0,18325tez
  2. *allocation-fee* = 0,06425tez
* *gas* = 1615gu
* *bytes* = 990.

All the details can be found [here](https://better-call.dev/ghostnet/KT1WUApPrzQ11EYEhzbeNjd4N96NQQop94w6/operations) or [here](https://ghostnet.tzkt.io/KT1WUApPrzQ11EYEhzbeNjd4N96NQQop94w6/operations/).

### Token Transfer
(Working on)

## Differences
The main differences between the transaction costs for deploy are made by the storage fee.
Alongside the *allocation-fee* is the same.
[4](#references)
(Working on)



#### References
1. [Economics and Rewards](https://opentezos.com/tezos-basics/economics-and-rewards/)
2. The wallet used for the test was the TempleWallet
3. *Baker-fee* are the fees paid to bakers, the [bakers](https://opentezos.com/baking/baking_explained/) are the *miner*-equivalent for other blockchains (with some differents). So *baker-fee* = total-fee.
4. A detailed explaination of how gas and fees are calculated can be found [here](https://kitchen.stove-labs.com/docs/knowledge/tezos_protocol/operations/gas-fees/).
