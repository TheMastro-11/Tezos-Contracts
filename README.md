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


## Smart contract in Tezos 
A smart contract is a computer program or a transaction protocol that is intended to automatically execute, control or document events and actions according to the terms of a contract or an agreement. The objectives of smart contracts are the reduction of need for trusted intermediators, arbitration costs, and fraud losses, as well as the reduction of malicious and accidental exceptions. [[5]](#references)<br> 
An example: 
in the traditional finance ecosystem, if someone wants to buy something, whether it's a videogame or a car, they have a series of guarantees that allow them to make the purchase in complete safety.<br> 
In the first case, they would buy the product from an official shop, and if it doesn't work, they have a receipt that they can use to get a refund. In the second case, if they buy the car in a private deal, they then have to go to an authorized official to make a change of ownership, or if they buy from a dealer they'll have to sign a contract to complete the purchase, either way they have a strong guarantee.<br> 
Because the blockchain is fully decentralized, hence there are no intermediaries, that's what the smart contract is used for.<br> 
A smart contract is a program which runs perpetually on the blockchain since its deployment; it gives users a safe place where they can make transactions for services or *tokenized items*[[6]](#references).<br> 
Another example: <br> 
person **A** from the USA wants to buy an item from person **B** in Australia; they could make the purchase privately with a simple transaction, but **A** would then have no guarantee that **B** wouldn't disappear once the purchase is finalized. This is where the smart contract comes in: if **B** doesn't send the item for the purchase, the smart contract automatically refunds **A** and the deal is off. <br>
By default, Tezos smart contracts are written in Michelson[[7]](#references), but it is an hard to learn low level formal language and is the reason why the above mentioned languages are available.<br> 
This is the *transpile* process: 
![alt text](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/blob/main/src/smartml.png)<br> 
The SmartPy library is used to access SmartML definitions; We can get a SmartML piece from a SmartPy piece. SmartPy offers a compiler to translate SmartML to Michelson.[[8]](#references)<br> 

A smart contract has two fundamental parts: 
* Storage or State Variables 
* Entrypoints 

The first one is the memory, publicly visible.<br> 
At the origination an admin can give some value to the contract: 
``` 
class Throne(sp.Contract): 
def __init__(self, admin): 
self.init(king = admin, history = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TRecord(value = sp.TMutez, data = sp.TTimestamp)), floorPrice = sp.mutez(5000)) 
``` 
in this case `admin` is passed as parameter during deployment meanwhile `floorprice` is setted before and `history` is empty.<br><br> 
Otherwise a contract could have all empty field at the beginning: 

``` 
class HashTimedLockedContract(sp.Contract): 
def __init__(self): 
self.init(deadline = sp.none, committer = sp.none , receiver = sp.none, hash = sp.none) 
``` 
and they will be modified during *entrypoint* executions 
<br>
Let’s see an example: <br>
**A** wants to send 100tz to **B** using a smart contract, [Simple Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/main/contracts/SimpleTransfer ). <br>
Simple Transfer has only one state variable `receiver`, setted as empty
```
class SimpleTransfer(sp.Contract):
    def __init__(self):
        self.init(receiver = sp.none)
```
Then **A** call `deposit ` and insert the **B** address as parameter
```
@sp.entry_point
    def deposit(self, receiver):
        #update data
        self.data.receiver = sp.some(receiver)
```
Here an example of how interact with the contract via [client](https://github.com/TheMastro-11/SmartContractTestScript-By-Taquito-). 
``` 
contract.methods.deposit(—B-Address—).send({amount: 100}); 
``` 
Now the *storage* is updated, and will keep the values for the next time they are necessary.<br>
The *storage* partially replaces the lack of a *return*, in fact we will never receive a response from the contract as a function do.<br> 
In some cases we could use a *callback*:<br> 
The *callback* contract is a combination of an address and an optional entrypoint, which is type-checked on-chain at runtime — which means we can be certain that it supports the required callback parameters, which is a list of responses (requests + balance).<br> 
List of responses is sent to the *callback* contract in an operation emitted internally by the TZIP-12 contract.<br> 
It’s up to the receiving contract to decide what to do with the incoming data, however none of those transaction can fail, otherwise the whole chain of transactions will be rolled back.[[9]](#references) 
<br> 
When **B** wants to receive the money it calls the `withdraw`
``` 
@sp.entry_point
    def withdraw(self):
        #check receiver
        sp.verify(self.data.receiver == sp.some(sp.sender), "Wrong Address")

        #withdraw
        sp.send(self.data.receiver.open_some(), sp.balance)
``` 
The `receiver` value is taken from storage. <br>
Both **deposit** and **withdraw** are *entrypoints*, essentially what allows a user to interact with the smart contract.<br> 

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
