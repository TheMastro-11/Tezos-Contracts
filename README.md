# Evaluating execution and development costs in the Tezos blockchain
The goal of this project is to evaluate the costs of developing and executing smart contracts in the [Tezos blockchain](https://tezos.com/).

## Tezos Blockchain
A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes.[[1]](#references)
In a few words, blockchains represent the new frontier in the finance world.
Born in 2008 with Bitcoin (the first ever published), a blockchain is a fully decentralized system that gives to millions (potentially billions) users around the world the opportunity to exchange money (like bitcoin) with [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) transactions and very low fees.
Due to its growth, new mechanics were born and the system's functionalities were expanded, one of which was the Smart Contract.

Launched in 2018, Tezos is an open-source platform for assets and applications that can evolve by upgrading itself.[[2]](#references)
It is designed to enable secure, efficient, and scalable Smart Contracts and decentralized applications (dApps). 
It uses an on-chain governance model that enables the protocol to be amended when upgrade proposals receive a favorable vote from the community[[3]](#references), offering stakeholders the ability to actively participate in the decision-making process of protocol upgrades.
Tezos uses a proof-of-stake (PoS[[4]](#references)) consensus mechanism, allowing token holders to participate in the validation of transactions and the creation of new blocks. PoS system promotes energy efficiency and reduces the environmental impact typically associated with traditional proof-of-work (PoW[[4]](#references)) blockchains, like Bitcoin.
Its core language, Michelson, is designed for formal verification, a technique that ensures the correctness of smart contracts by mathematically proving their properties. By leveraging formal verification, Tezos aims to minimize the risks associated with coding errors, making it a robust and reliable platform for developers.
Additionally, Tezos supports tokenization, enabling the creation of digital assets and facilitating the issuance of new tokens on the platform. This functionality opens up opportunities for crowdfunding, asset tokenization, and the creation of decentralized financial applications.
Tezos offers three different programming languages:
- SmartPy
- Archetype
- Ligo

each one with unique properties and funtionalities.
Therefore at the beginning of my work, i tested all three of them.


## Smart Contract in Tezos
A smart contract is a computer program or a transaction protocol that is intended to automatically execute, control or document events and actions according to the terms of a contract or an agreement. The objectives of smart contracts are the reduction of need for trusted intermediators, arbitration costs, and fraud losses, as well as the reduction of malicious and accidental exceptions. [[5]](#references)
An example:
in the traditional finance ecosystem, if someone wants to buy something, wether it's a videogame or a car, they have a series of guarantees that allow them to make the purchase in complete safety.
In the first case, they would buy the product from an official shop, and if it doesn't work, they have a receipt that they can use to get a refund. In the second case, if they buy the car in a private deal, they then have to go to an authorized official to make a change of ownership, or if they buy from a dealer they'll have to sign a contract to complete the purchase, either way they have a strong guarantee.
Because the blockchain is fully decentralized, hence there are no intermediaries, that's what the Smart Contract is used for.
A smart contract is a program which runs perpetually on the blockchain since its deployment; it gives users a safe place where they can make transactions for services or *tokenized items*[[6]](#references).
Another example: 
person **A** from the USA wants to buy an item from person **B** in Australia; they could make the purchase privately with a simple transaction, but **A** would then have no guarantee that **B** wouldn't disappear once the purchase is finalized. This is where the smart contract comes in: if **B** doesn't send the item for the purchase, the smart contract automatically refunds **A** and the deal is off.

A smart contract in Tezos has two fundamental parts:
* Storage or State Variables
* Entrypoints

The first one is the memory, publicly visible:
```
class HashTimedLockedContract(sp.Contract):
    def __init__(self):
        self.init(deadline = sp.none, committer = sp.none , receiver = sp.none, hash = sp.none)

```
at the origination this contract has four empty fields
```
 def commit(self, deadline, receiver, hash):
        #save into data
        self.data.deadline = sp.some(sp.level + deadline)
        self.data.receiver = sp.some(receiver)
        self.data.hash = sp.some(hash)
        
        self.data.committer = sp.some(sp.sender)
```
after this call the storage will be updated and will keep the values for the next time they are used
```
def reveal(self, word):
        #hash
        sp.set_type(word, sp.TString)
        bytes = sp.pack(word) 
        hash = sp.keccak(bytes) #created
        sp.verify(self.data.hash == sp.some(hash), "Wrong word") #checked

        #transfer collateral to commiter
        sp.send(self.data.committer.open_some(), sp.balance)
```
here the **committer** and **hash** values are taken from storage.
Both **commit** and **reveal** are entrypoints, essentially what allows a user to interact with the smart contract.
```
contract.methods.commit(deadline, secret, receiver).send({fee : 2000, amount: 1000, mutez: true});
```
Here an example of how interact with the contract via [client](https://github.com/TheMastro-11/SmartContractTestScript-By-Taquito-).

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
I have [experimented](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/experiments) 7 Smart Contracts on *Test Net* to evaluate the paid fees fot both [deployment](/experiments/Deployments/) and [interactions](/experiments/Interactions/).
To help me in this work I have developed a [tool](https://github.com/TheMastro-11/SmartContract-Execution-Costs-By-Taquito) to automatize the estimation of the execution costs.

## References
1. Blockchain article from [Wikipedia](https://en.wikipedia.org/wiki/Blockchain)
2. Tezos [basics](https://tezos.com/learn/what-is-tezos/)
3. Tezos article from [Wikipedia](https://en.wikipedia.org/wiki/Tezos)
4. You can find a more detailed description of PoS [here](https://en.wikipedia.org/wiki/Proof_of_stake) and PoW [here](https://en.wikipedia.org/wiki/Proof_of_work)
5. Smart Contract article from [Wikipedia](https://en.wikipedia.org/wiki/Smart_contract)
6. You can find an example of how *Tokenization* works [here](https://www.nasdaq.com/articles/what-is-tokenization-and-how-does-it-work)
