
## DISCLAIMER

  

it's just a draft -> NOT definitive

  

It has to be translated in English.

  

# <center>LEARNING TEZOS<center>

"Learning Tezos" is a university project that aims to develop skills in the modeling and analysis of decentralized applications on the blockchain.

To this end, programming languages for smart contracts supported by the [blockchain](https://tezos.com/) will be studied.

Specifically, a set of use cases will be proposed that will be implemented in the Archetype, LIGO, and SmartPy languages, and then a report will be produced on the differences between the various implementations.
  

## USE CASES

* [CrowdFunding](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding)

* [Lottery](https://github.com/TheMastro-11/LearningTezos/tree/contracts/Lottery)

* [King of Tezos](https://github.com/TheMastro-11/LearningTezos/tree/contracts/KingOfTezos)

* [Blind Auction](https://github.com/TheMastro-11/LearningTezos/tree/contracts/BlindAuction)

* (in progress)

  

## PROGRAMMING LANGUAGES COMPARISON

*-For a detailed analysis, see the comparisons in the differents use cases.-*
  
[Archetype](https://archetype-lang.org/), [Ligo](https://tezos.com/developers/ligo/) and [SmartPy](https://smartpy.io/) are a programming languages and toolkit for writing and deploying smart contracts on Tezos blockchain

Some in common key features of these languages include:
* Support for testing and debugging, including a built-in test framework and integration with popular testing tools.
* Integration with popular development tools and frameworks, including support for IDEs like Visual Studio Code and integration with Git and GitHub.
* High

Overall, while Ligo, Archetype, and SmartPy all have similar capabilities and are well-suited for developing smart contracts, they have slightly different syntax and tool sets.

### Smartpy 
Smartpy took a long time to understand the dynamics of how a Smart Contract works on Tezos and the use of *entrypoint*.
I was helped by:
* Using a populare language (Python).
* Extensive documentation and several online tutorials.
* The great availability of the developers in the Telegram group.

Once I took the hand then the realization of several usecases was quite simple. (See the folders above)

Compared to the classic Python requires strong typing, which can result in a pros or cons depending on your writing method.

**Pro**:
* Keep several SCs within the same file.
* The use of the scenario is undoubtedly very convenient.
* It’s easy to keep the code neat, clean and understandable thanks to nomenclature, e.g.: *@sp.entry_point*, *@sp. -type-*...
* SmartPy didn’t give me any trouble for any implementation I wanted to add.
* Use of attributes in a SC statement.
* Python syntax.
* IDE really well made.

**Cons**:
* Lack of *states*.

### Archetype
**Pro**:
* Archetype has good documentation.
* A simple, readable syntax that is inspired by other popular programming languages.
* Allows the use of *states*. 

**Cons**:
* Fewer developers in general and therefore less chance of finding specific support.
* Not an easy installation for the compiler (it's recommended to use a GitPod workspace).

### Ligo
**Pro**:
* Ligo has a syntax that is inspired by OCaml so is familiar to those who already know.

**Cons**:
* It's difficult to use some constructs like *Option*.
* Little documentation and few developers.
* It could be confusing the fact that there are several versions: JsLIGO, CameLIGO, PascaLIGO and ReasonLIGO.
* The system through which the *main* calls *entrypoints* could be cumbersome: in Ligo a return value is always required for the entrypoints so that the operations carried out inside can be transmitted to the main.
* You can't create functions outside of the *entries* and have global variables.


