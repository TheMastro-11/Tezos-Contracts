# Smart contract in Tezos 
A smart contract is a computer program or transaction protocol designed to automate, control or record events and actions based on predefined terms and conditions.[[1]](#references)<br>
Because the blockchain is fully decentralized the main goals include minimizing the reliance on trusted intermediaries, reducing arbitration expenses, preventing fraud losses, and mitigating both intentional and unintentional errors or exceptions.<br>
A smart contract runs perpetually on the blockchain since its deployment and its terms are written into code (publicy visible) and executed automatically, ensuring transparency and efficiency in the agreement's enforcement.
These contracts have the potential to revolutionize various industries by streamlining processes, increasing trust, and enabling new business models. They can be utilized in areas such as supply chain management, financial services, real estate transactions through a process call *tokenization*[[2]](#references) and more, offering benefits in terms of speed, cost savings, and enhanced security.<br> 
An example: 
in the traditional finance ecosystem, if someone wants to buy something, whether it's a videogame or a car, they have a series of guarantees that allow them to make the purchase in complete safety.<br> 
In the first case, they would buy the product from an official shop, and if it doesn't work, they have a receipt that they can use to get a refund. In the second case, if they buy the car in a private deal, they then have to go to an authorized official to make a change of ownership, or if they buy from a dealer they'll have to sign a contract to complete the purchase, either way they have a strong guarantee.<br>  

Another example: <br> 
person **A** from the USA wants to buy an item from person **B** in Australia; they could make the purchase privately with a simple transaction, but **A** would then have no guarantee that **B** wouldn't disappear once the purchase is finalized. This is where the smart contract comes in: if **B** doesn't send the item for the purchase, the smart contract automatically refunds **A** and the deal is off. <br> <br>
By default, Tezos smart contracts are written in Michelson[[3]](#references), which is an hard to learn, low level formal language and is the reason why are avaiable three different languages.<br> 
This is the *transpile* process: <br>
![alt text](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/blob/master/src/smartml.png)<br> 
The SmartPy library is used to access SmartML definitions; We can get a SmartML piece from a SmartPy piece. SmartPy offers a compiler to translate SmartML to Michelson.[[4]](#references)<br> 

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
**A** wants to send 100tz to **B** using a smart contract, [Simple Transfer](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/master/contracts/SimpleTransfer ). <br>

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
It’s up to the receiving contract to decide what to do with the incoming data, however none of those transaction can fail, otherwise the whole chain of transactions will be rolled back.[[5]](#references) <br> 

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

# Programming Languages Comparison
[Archetype](https://archetype-lang.org/), [Ligo](https://tezos.com/developers/ligo/) and [SmartPy](https://smartpy.io/) are programming languages and toolkits for writing and deploying smart contracts on the Tezos blockchain.

Some key features that these languages have in common are:

- Support for testing and debugging, including a built-in test framework and integration with popular testing tools.
- Use of common development tools and frameworks, including support for IDEs like Visual Studio Code and integration with Git and GitHub.

They all have similar capabilities but also they have slightly different syntax and toolsets.

## SmartPy
SmartPy is a comprehensive solution for developing, testing, and deploying smart contracts on the Tezos blockchain. With its easy-to-use Python syntax, developers can create contracts in a familiar and intuitive way, while SmartPy's type inference provides added safety.[[6]](#references)
It took me a long time to understand the dynamics of how a Smart Contract works on Tezos and the use of *entrypoints*. 
I was helped by:
- The use of a commonly used language (Python).
- Extensive documentation and several online tutorials.
- Great availability of the developers of SmartPy for the resolution of problems.

Once I got the hang of it, I was able to realize several use cases with little to no difficulty.  

Compared to Python, SmartPy is a strongly typed language, which can result in pros or cons depending on one’s writing method.

**Pros**:
- Possibility to keep several SCs within the same file.
- Convenience in using the *scenario*. 
- Ease in keeping the code neat, clean and understandable thanks to nomenclature, e.g.: *@sp.entry_point*, *@sp.-type-*...
- No problems when adding any implementations I wanted. 
- Python syntax.
- Well-made IDE.

**Cons**:
- Lack of *states*.


## Archetype
Archetype is an elegant generic-purpose language to develop Smart Contracts on the Tezos blockchain.
It supports all Michelson features, but also provides exclusive high-level features for a precise and concise source code, that make contracts easier to develop, read and maintain.[[7]](#references)
**Pros**:
- Good documentation. 
- A simple, readable syntax that is inspired by other popular programming languages.
- Allows the use of *states*.

**Cons**:
- Fewer developers in general and therefore less chance of finding specific support.
- Not an easy installation for the compiler (I used a GitPod workspace).


## Ligo
LIGO is a functional language designed to include the features you need while avoiding patterns that make formal verification hard. Most useful smart contracts can express their core functionality in under a thousand lines of code. This makes them a good target for formal methods, and what can't be easily proven can at least be extensively tested. The simplicity of LIGO also keeps its compiled output unbloated. Our hope is to have a simple, strongly typed language with a low footprint.[[8]](#references)

**Pros**:
- Ligo has a syntax that is inspired by OCaml, therefore it is familiar to those who already know this language. 

**Cons**:
- Difficulty in using constructs like *Option*.
- Documentation can be improved.
- Few developers.
- The several versions of this language (JsLIGO, CameLIGO, PascaLIGO and ReasonLIGO) could cause some confusion in their use.
- The system through which the *main* calls *entrypoints* is quite complex: in Ligo, a return value is always required for the entrypoints so that the operations carried inside can be transmitted to the main.
- Inability to create functions outside of the *entries* and have global variables.


## References
1. [Smart contract](https://en.wikipedia.org/wiki/Smart_contract) (last update 03 May 2023), Wikipedia, *The free encyclopedia*. Retrieved May 24, 2023.
2. [What Is Tokenization and How Does It Work?](https://www.nasdaq.com/articles/what-is-tokenization-and-how-does-it-work) (01 September 2022), Nasdaq - GOBankingRates, Taylor DeJesus. Retrieved May 22, 2023. 
3. [Michelson, the language of Tezos smart-contracts](https://www.michelson.org/) (n.d.), Michelson. Retrieved May 24, 2023. 
4. [SmartPy - First Steps](https://tezos.b9lab.com/smartpy/intro) (n.d.), Tezod Developer Portal. Retrieved May 24, 2023.
5. [Implementing a mini token contract with on-chain callbacks (TZIP-12)](https://medium.com/@matej.sima/tutorial-implementing-a-mini-token-contract-on-tezos-with-on-chain-callbacks-tzip-12-b04cf7ee2059) (28 February 2020), Medium - Matej Šima. Retrieved May 24, 2023.
6. [SmartPy Introduction](https://smartpy.io/docs/manual/introduction/overview) (n.d.), SmartPy. Retrieved on May 23, 2023.
7. [Archetype introduction](https://archetype-lang.org/docs/introduction) (n.d.), Archetype-lang. Retrieved on May 23, 2023.
8. [Ligo introduction](https://ligolang.org/docs/intro/introduction?lang=jsligo) (n.d.), Ligolang. Retrieved on May 23, 2023.
