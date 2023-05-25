# Evaluating execution and development costs in the Tezos blockchain 
The goal of this project is to evaluate the costs of developing and executing smart contracts in the [Tezos blockchain](https://tezos.com/). 

## The Tezos Blockchain 
A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes.[[1]](#references)<br> 
In a few words, blockchains represent the new frontier in the finance world.<br> 
Born in 2008 with Bitcoin (the first ever published), a blockchain is a fully decentralized system that gives to millions (potentially billions) users around the world the opportunity to exchange money (like bitcoin) with [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) transactions and very low fees.<br> 
Due to its growth, new mechanics were born and the system's functionalities were expanded, one of which was the smart contract. 

Launched in 2018, Tezos is an open-source platform for assets and applications that can evolve by upgrading itself.[[2]](#references)<br> 
It is designed to enable secure, efficient, and scalable smart contracts and decentralized applications (dApps). <br> 
It uses an on-chain governance model that enables the protocol to be amended when upgrade proposals receive a favorable vote from the community[[3]](#references), offering stakeholders the ability to actively participate in the decision-making process of protocol upgrades.<br> 
Tezos uses a proof-of-stake (PoS[[4]](#references)) consensus mechanism, allowing token holders to participate in the validation of transactions and the creation of new blocks. PoS system promotes energy efficiency and reduces the environmental impact typically associated with traditional proof-of-work (PoW[[4]](#references)) blockchains, like Bitcoin. 
Its core language, Michelson, is designed for formal verification, a technique that ensures the correctness of smart contracts by mathematically proving their properties. By leveraging formal verification, Tezos aims to minimize the risks associated with coding errors, making it a robust and reliable platform for developers.<br> 
Additionally, Tezos supports tokenization, enabling the creation of digital assets and facilitating the issuance of new tokens on the platform. This functionality opens up opportunities for crowdfunding, asset tokenization, and the creation of decentralized financial applications.<br> 
Tezos offers three different programming languages: 
- SmartPy 
- Archetype 
- Ligo 

each one with unique properties and funtionalities.<br> 
Therefore at the beginning of my work, i tested all three of them. 

## Use Cases 
I have developed a set of use cases: 

- [Simple Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/SimpleTransfer) 
- [Auction](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/Auction) 
- [King of Tezos](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/KingOfTezos) 
- [CrowdFunding](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/CrowdFunding) 
- [HTLC](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/HTLC) 
- [Token Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/TokenTransfer) 

## Language Comparison 
After developing several contracts in every language available, I made a [detailed](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts) comparison between them to find out which one was the best to continue developing and test. 
Between all of them, I chose SmartPy 


## Analysis of execution costs 
I have [experimented](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/experiments) 7 smart contracts on *Test Net* to evaluate the paid fees fot both [deployment](/experiments/Deployments/) and [interactions](/experiments/Interactions/). 
To help me in this work I have developed a [tool](https://github.com/TheMastro-11/SmartContract-Execution-Costs-By-Taquito) to automatize the estimation of the execution costs. 

## References 
1. Blockchain article from [Wikipedia](https://en.wikipedia.org/wiki/Blockchain) 
2. Tezos [basics](https://tezos.com/learn/what-is-tezos/) 
3. Tezos article from [Wikipedia](https://en.wikipedia.org/wiki/Tezos) 
4. You can find a more detailed description of PoS [here](https://en.wikipedia.org/wiki/Proof_of_stake) and PoW [here](https://en.wikipedia.org/wiki/Proof_of_work) 
5. Smart contract article from [Wikipedia](https://en.wikipedia.org/wiki/Smart_contract) 
6. You can find an example of how *Tokenization* works [here](https://www.nasdaq.com/articles/what-is-tokenization-and-how-does-it-work) 
7. [Michelson.org](https://www.michelson.org/) 
8. [Tezos Developer Portal](https://tezos.b9lab.com/smartpy/intro) 
9. An example article from [Medium](https://medium.com/@matej.sima/tutorial-implementing-a-mini-token-contract-on-tezos-with-on-chain-callbacks-tzip-12-b04cf7ee2059) 
