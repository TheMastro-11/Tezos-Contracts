# Programming Languages Comparison
[Archetype](https://archetype-lang.org/), [Ligo](https://tezos.com/developers/ligo/) and [SmartPy](https://smartpy.io/) are programming languages and toolkits for writing and deploying smart contracts on the Tezos blockchain.

Some key features that these languages have in common are:

- Support for testing and debugging, including a built-in test framework and integration with popular testing tools.
- Use of common development tools and frameworks, including support for IDEs like Visual Studio Code and integration with Git and GitHub.

They all have similar capabilities but also they have slightly different syntax and toolsets.

## SmartPy
While using SmartPy, it took me a long time to understand the dynamics of how a Smart Contract works on Tezos and the use of *entrypoints*. 
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
**Pros**:
- Good documentation. 
- A simple, readable syntax that is inspired by other popular programming languages.
- Allows the use of *states*.

**Cons**:
- Fewer developers in general and therefore less chance of finding specific support.
- Not an easy installation for the compiler (I used a GitPod workspace).


## Ligo
**Pros**:
- Ligo has a syntax that is inspired by OCaml, therefore it is familiar to those who already know this language. 

**Cons**:
- Difficulty in using constructs like *Option*.
- Little documentation and few developers.
- The several versions of this language (JsLIGO, CameLIGO, PascaLIGO and ReasonLIGO) could cause some confusion in their use.
- The system through which the *main* calls *entrypoints* is quite complex: in Ligo, a return value is always required for the entrypoints so that the operations carried inside can be transmitted to the main.
- Inability to create functions outside of the *entries* and have global variables.
