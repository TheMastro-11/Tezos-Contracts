
## DISCLAIMER

  

it's just a draft -> NOT definitive

  

It has to be translated in English.

  

# <center>LEARNING TEZOS<center>

"Learning Tezos" is a university project that aims to develop skills in the modeling and analysis of decentralized applications on the blockchain.

To this end, programming languages for smart contracts supported by the [blockchain](https://tezos.com/) will be studied.

Specifically, a set of use cases will be proposed that will be implemented in the Archetype, LIGO, and SmartPy languages, and then a report will be produced on the differences between the various implementations.
  

## USE CASES

* CrowdFunding [Link](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding)

* (in progress)

  

## PROGRAMMING LANGUAGES

[Archetype](https://archetype-lang.org/), [Ligo](https://tezos.com/developers/ligo/) and [SmartPy](https://smartpy.io/) are a programming languages and toolkit for writing and deploying smart contracts. They are designed to be easy to use and to enable developers to write contracts that are safe, secure, and easy to understand.

Some key features of these languages include:
* A simple, readable syntax that is inspired by other popular programming languages.
* A rich set of built-in libraries and data types, including support for integers, strings, lists, tuples, records, and maps.
* Support for testing and debugging, including a built-in test framework and integration with popular testing tools.
* Integration with popular development tools and frameworks, including support for IDEs like Visual Studio Code and integration with Git and GitHub.
* Syntax: Ligo has a syntax that is inspired by OCaml and other functional programming languages, while SmartPy has a syntax that is similar to Python and Archetype has a syntax that is inspired by other popular programming languages.

Overall, while Ligo, Archetype, and SmartPy all have similar capabilities and are well-suited for developing smart contracts, they have slightly different syntax and tool sets.

## COMPARISON

#### Smartpy 
Smartpy took a long time to understand the dynamics of how a Smart Contract works on Tezos and the use of *entrypoint*.
I was helped by:
* Using a language (Python) I already knew.
* Extensive documentation and several online tutorials.
* The great availability of the developers in the Telegram group.

Once I took the hand then the realization of several usecases was quite simple. (See the folders above)

Pro:
* Keep several SCs within the same file.
* The use of the scenario is undoubtedly very convenient.
* It’s easy to keep the code neat, clean and understandable thanks to nomenclature, e.g.: *@sp.entry_point*, *@sp. -type-*...
* SmartPy didn’t give me any trouble for any implementation I wanted to add.
* I really appreciated the use of attributes in a SC statement.
* Classic use of functions.
* I really enjoyed the list and map management.
* IDE really well made.

If I had to use a language among the three I would definitely select this.
Vote: 9/10 (it can always improve)

#### Archetype
Archetype also has good documentation, but fewer developers in general and therefore less chance of finding specific support.
I had difficulty installing the compiler and I ended up with a GitPod workspace.

Vote: 7/10 (needs a full IDE) 

#### Ligo
I had difficulty using some constructs like *Option*.
Little documentation and few developers.
I did not like the fact that there are several versions:
* JsLIGO
* CameLIGO
* PascaLIGO
* ReasonLIGO
I find it confusing.

I found the system through which the *main* calls *entrypoints* cumbersome.
I didn’t appreciate the fact that I couldn’t create functions outside of the *entries* and couldn’t have global variables.

Vote 5/10 (doesn't suit for me)


For a detailed analysis, see the comparisons in the different use cases.
