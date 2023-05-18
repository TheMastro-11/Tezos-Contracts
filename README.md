# Evaluating execution and development costs in the Tezos blockchain

The goal of this project is to evaluate the costs of developing and executing smart contracts in the [Tezos blockchain](https://tezos.com/).

Specifically:
* I have developed a set of use cases in the Archetype, LIGO, and SmartPy languages;
* I have compared the implementations in the three languages;
* Focusing on SmartPy I have [experimented](https://github.com/TheMastro-11/LearningTezos/tree/main/experiments) the Smart Contract to evaluate the paid fees;
* I have developed a [tool](https://github.com/TheMastro-11/SmartContractTestScript-By-Taquito-) to automatize the estimation of the execution costs;

## USE CASES

- [CrowdFunding](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/CrowdFunding)
- [Lottery](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/Lottery)
- [King of Tezos](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/KingOfTezos)
- [Blind Auction](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/BlindAuction)
- [HTLC](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/HTLC)
- [Simple Transfer](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/SimpleTransfer)
- [Token Transfer](https://github.com/TheMastro-11/LearningTezos/tree/main/contracts/TokenTransfer)

## PROGRAMMING LANGUAGES COMPARISON

*-For a more detailed analysis, see the comparison between different use cases.-*

[Archetype](https://archetype-lang.org/), [Ligo](https://tezos.com/developers/ligo/) and [SmartPy](https://smartpy.io/) are programming languages and toolkits for writing and deploying smart contracts on the Tezos blockchain.

Some key features that these languages have in common are:

- Support for testing and debugging, including a built-in test framework and integration with popular testing tools.
- Use of common development tools and frameworks, including support for IDEs like Visual Studio Code and integration with Git and GitHub.

Overall, while Ligo, Archetype, and SmartPy all have similar capabilities and are well-suited for developing smart contracts, they have slightly different syntax and toolsets.

### SMARTPY

While using SmartPy, it took me a long time to understand the dynamics of how a Smart Contract works on Tezos and the use of *entrypoints*. 
I was helped by:
- The use of a commonly used language (Python).
- Extensive documentation and several online tutorials.
- Great availability of the developers of SmartPy for the resolution of problems.

Once I got the hang of it, I was able to realize several use cases with little to no difficulty (see folders above).  

Compared to Python, SmartPy is a strongly typed language, which can result in pros or cons depending on one’s writing method.

**Pros**:
- Possibility to keep several SCs within the same file.
- Convenience in using the *scenario*. 
- Ease in keeping the code neat, clean and understandable thanks to nomenclature, e.g.: *@sp.entry_point*, *@sp.-type-*...
- No problems when adding any implementations I wanted. 
- Use of attributes in an SC statement.
- Python syntax.
- Well-made IDE.

**Cons**:
- Lack of *states*.


### ARCHETYPE
**Pros**:
- Good documentation. 
- A simple, readable syntax that is inspired by other popular programming languages.
- Allows the use of *states*.

**Cons**:
- Fewer developers in general and therefore less chance of finding specific support.
- Not an easy installation for the compiler (it's recommended to use a GitPod workspace).


### LIGO
**Pros**:
- Ligo has a syntax that is inspired by OCaml, therefore it is familiar to those who already know this language. 

**Cons**:
- Difficulty in using constructs like *Option*.
- Little documentation and few developers.
- The several versions of this language (JsLIGO, CameLIGO, PascaLIGO and ReasonLIGO) could cause some confusion in their use.
- The system through which the *main* calls *entrypoints* is quite complex: in Ligo, a return value is always required for the entrypoints so that the operations carried inside can be transmitted to the main.
- Inability to create functions outside of the *entries* and have global variables.
