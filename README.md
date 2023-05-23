# Evaluating execution and development costs in the Tezos blockchain
The goal of this project is to evaluate the costs of developing and executing smart contracts in the [Tezos blockchain](https://tezos.com/).

## What is a Blockchain
A blockchain is a distributed ledger with growing lists of records (blocks) that are securely linked together via cryptographic hashes.[1](#references)
In few words represent the new frontier in finance world.
Born in 2008 with Bitcoin (the first blockchain published) is a fully decentralized system that gives to millions (potentially billions) users around the world the opportunity to exchange money (like bitcoin) with [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) transactions and very low fees.
Due to the growth of this environment new mechanics were born and expanded the functionalities of the system, one of them was Smart Contract.

## What is a Smart Contract
A smart contract is the best solution for the lack of a *judge* in the blockchain world.
For example:
In traditional finance ecosystem if you want to buy a small object (like a videoGames) or a property (like a car) you have a series of guarantees that allow you to make the purchase in complete safety.
In first scenario if you buy the product from an official shop (not from a man around the corner) and it does not work properly you have a receipt that allows you to get a refund.
In second scenario if you purchase from an individual you will go to an official authorized to effect the property change or if you purchase from a dealer you will sign a contract, either way you will have a strong guarantee.
Because a blockchain is fully decentralized, there are no intermediaries, here comes the Smart Contract.
A smart contract is a program the runs perpetually on the blockchain since is deployed and gives users a safe place where make transaction for service or *tokenized item* (You can find an example of how *Tokenization* works [here](https://www.nasdaq.com/articles/what-is-tokenization-and-how-does-it-work)).
For example: 
**A** from USA wants to buy a song from an artist in Australia called **B**, they could chat and make the purchase with a simple transaction, but who would guarantee **A** that **B** doesn’t disappear once he gets the money?
A smart contract did: if **B** didn't send the song it would automatically refund **A** and the deal would be off.

## Tezos
The [Tezos](https://tezos.com/learn/getting-started/) blockchain is a decentralized, self-amending platform designed to enable secure, efficient, and scalable Smart Contracts and decentralized applications (dApps). 
Launched in 2018, Tezos introduced a new approach to blockchain governance, offering stakeholders the ability to actively participate in the decision-making process of protocol upgrades.
Tezos uses a proof-of-stake (PoS[2](#references)) consensus mechanism, allowing token holders to participate in the validation of transactions and the creation of new blocks. PoS system promotes energy efficiency and reduces the environmental impact typically associated with traditional proof-of-work (PoW[2](#references)) blockchains, like Bitcoin.
Its core language, Michelson, is designed for formal verification, a technique that ensures the correctness of smart contracts by mathematically proving their properties. By leveraging formal verification, Tezos aims to minimize the risks associated with coding errors, making it a robust and reliable platform for developers.
Additionally, Tezos supports tokenization, enabling the creation of digital assets and facilitating the issuance of new tokens on the platform. This functionality opens up opportunities for crowdfunding, asset tokenization, and the creation of decentralized financial applications.
Tezos offers three different programming languages:
- SmartPy
- Archetype
- Ligo
each one with unique properties and funtionalities.
Therefore I tested all of them during first work period.

### Smart Contract in Tezos
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
After developing a bunch of Contracts in every language available I made a [detailed](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts) comparison between them to find out which was the best solution to continue developing and make tests. 
I choose SmartPy.

## Analysis of execution costs
I have [experimented](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/experiments) 7 Smart Contracts on *Test Net* to evaluate the paid fees fot both [deployment](/experiments/Deployments/) and [interactions](/experiments/Interactions/).
To help me in this work I have developed a [tool](https://github.com/TheMastro-11/SmartContract-Execution-Costs-By-Taquito) to automatize the estimation of the execution costs.

## References
1. Blockchain article from [Wikipedia](https://en.wikipedia.org/wiki/Blockchain)
2. You can find a more detailed description of PoS [here](https://en.wikipedia.org/wiki/Proof_of_stake) and PoW [here](https://en.wikipedia.org/wiki/Proof_of_work)
