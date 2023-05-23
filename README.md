# Evaluating execution and development costs in the Tezos blockchain
The goal of this project is to evaluate the costs of developing and executing smart contracts in the [Tezos blockchain](https://tezos.com/).

## Use Cases
I have developed a set of use cases in the Archetype, LIGO, and SmartPy languages;

- [Blind Auction](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/BlindAuction)
- [CrowdFunding](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/CrowdFunding)
- [HTLC](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/HTLC)
- [King of Tezos](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/KingOfTezos)
- [Lottery](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/Lottery)
- [Simple Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/SimpleTransfer)
- [Token Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/TokenTransfer)

## Language Comparison
After developing a bunch of Contracts in every language available I made a [detailed](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts) comparison between them to find out which was the best solution to continue developing and make tests. 
I choose SmartPy.

## Analysis of execution costs
I have [experimented](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/experiments) 7 Smart Contracts on *Test Net* to evaluate the paid fees fot both [deployment](/experiments/Deployments/) and [interactions](/experiments/Interactions/).
To help me in this work I have developed a [tool](https://github.com/TheMastro-11/SmartContractTestScript-By-Taquito-) to automatize the estimation of the execution costs.
