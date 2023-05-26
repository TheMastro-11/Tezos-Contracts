# Evaluating execution and development costs in the Tezos blockchain 
The goal of this project is to evaluate the costs of developing and executing smart contracts in the [Tezos blockchain](https://tezos.com/). 

## The Tezos Blockchain 
A blockchain refers to a fully decentralized digital ledger that consists of an expanding collection of records, aka transactions, known as blocks and are interconnected using cryptographic hashes to ensure a high level of security.[[1]](#references)<br> 
In a few words, blockchains represent the new frontier in the finance world.<br> 
Born in 2008 with Bitcoin (the first ever published), a blockchain is a fully decentralized system that gives to millions (potentially billions) users around the world the opportunity to exchange money (like bitcoin) with [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) transactions and very low fees.<br> 
Due to its growth, new mechanics were born and the system's functionalities were expanded, one of which was the smart contract. <br> <br>

Tezos, introduced in 2018, is an open-source platform designed to facilitate the creation and management of assets and applications. <br>
One of its notable features is the ability to evolve and upgrade itself through a self-amendment mechanism. This means that proposed upgrades and changes to the Tezos protocol are voted upon by stakeholders within the network. If a proposal receives a favorable vote, it can be implemented, enabling the platform to adapt and evolve over time in a decentralized manner. This governance mechanism empowers the Tezos community to actively participate in the decision-making process and shape the future direction of the platform.[[2]](#references),[[3]](#references). 
It is designed to enable secure, efficient, and scalable smart contracts and decentralized applications (dApps). <br> 
Tezos uses a proof-of-stake (PoS[[4]](#references)) consensus mechanism, allowing token holders to participate in the validation of transactions and the creation of new blocks. PoS system promotes energy efficiency and reduces the environmental impact typically associated with traditional proof-of-work (PoW[[5]](#references)) blockchains, like Bitcoin. 
Its core language, Michelson, is designed for formal verification, a technique that ensures the correctness of smart contracts by mathematically proving their properties. By leveraging formal verification, Tezos aims to minimize the risks associated with coding errors, making it a robust and reliable platform for developers.<br> 
Additionally, Tezos supports tokenization, enabling the creation of digital assets and facilitating the issuance of new tokens on the platform. This functionality opens up opportunities for crowdfunding, asset tokenization, and the creation of decentralized financial applications.<br> 
Tezos offers three different programming languages: 
- SmartPy 
- Archetype 
- Ligo 

each one with unique properties and functionalities.<br> 
Therefore at the beginning of my work, i tested all three of them. 

## Use Cases 
First I read all the manuals in order to understand how a smart contract works and what were the available features and the various generalities on: types, methods, utils, etc.. in each languages.
Than I have developed a set of use cases trying to explore all possible features and complexity levels: 
- [Simple Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/SimpleTransfer) 
- [Auction](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/Auction) 
- [King of Tezos](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/KingOfTezos) 
- [CrowdFunding](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/CrowdFunding) 
- [HTLC](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/HTLC) 
- [Token Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/TokenTransfer) 

## Language Comparison 
After developing several contracts, I made a [detailed](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts) comparison between languages to find out which one was the best to continue developing and test. 
Each language has its pros and cons:
* SmartPy benefits from its Python-like syntax, convenient usage of scenarios, and excellent IDE support.
* Archetype offers readable syntax and state management capabilities. 
* Ligo provides simplicity, strong typing, and good formal verification potential but may have difficulty with certain constructs and has limited documentation.
Overall, these programming languages offer similar capabilities for developing smart contracts on Tezos, but they have slight syntax and toolset differences, catering to different developer preferences and requirements.
Between all of them, I chose SmartPy

## Analysis of execution costs 
I did a thorough study to start understanding how fees were calculated.
I started with a formula described in the official documentation that determines the cost of a transaction. <br>
The formula includes fundamental factors such as storage fee, gas fee, baker fees and burn fees, also common in other blockchains. <br>
After I have [experimented](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/experiments) 7 smart contracts on *TestNet* and view the results case by case. 
At the end I introduced the two main sections which are:
* [deployment](/experiments/Deployments/) : the publication of contracts on chain
* [interactions](/experiments/Interactions/) : the call of individual entrypoints
<br> <br>
To help me in this work I have developed a [tool](https://github.com/TheMastro-11/SmartContract-Execution-Costs-By-Taquito) to automatize the estimation of the execution costs.<br>
The script is based on the Taquito boilerplate repository and offers a set of tools aimed at creating a client or a DAPP to interact with the Tezos blockchain.<br>
Is written in TypeScript and use HTML and CSS for Browser interaction.
My script consists of two modified files from original: "App.ts" and "index.html."
The second is a web interface that allows users to interact with the script by pasting the contract address and selecting the contract type to refer to (*SimpleTransfer*, *HTLC* etc..). <br>
The results of the execution can be viewed in the browser's console log. <br>
Each contract function follows a similar structure, involving obtaining contract information, calling entrypoints with parameters and retrieving transaction information as execution costs.


## References 
1. [Blockchain](https://en.wikipedia.org/wiki/Blockchain) (last update 22 May 2023) Wikipedia, *The free encyclopedia*. Retrieved May 23, 2023.
2. [Tezos basics](https://tezos.com/learn/what-is-tezos/) (n.d.) Tezos. Retrieved May 24, 2023 
3. [Tezos](https://en.wikipedia.org/wiki/Tezos) (last update 13 May 2023), Wikipedia, *The free encyclopedia*. Retrieved May 24, 2023.
4. [Proof of stake](https://en.wikipedia.org/wiki/Proof_of_stake) (last update 07 May 2023), Wikipedia, *The free encyclopedia*. Retrieved May 24, 2023.
5. [Proof of work](https://en.wikipedia.org/wiki/Proof_of_work) (last update 13 May 2023), Wikipedia, *The free encyclopedia*. Retrieved May 24, 2023.
