## DISCLAIMER

it's just a draft -> NOT definitive

It has to be translated in English.

  

# CROWDFUNDING

Crowdfunding is a Smart Contract created with the aim of learning to program on the Tezos blockchain.

For this reason it has been implemented with all three languages available:

-[Smartpy](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/SmartPy/README.md)

-[Archetype](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/Archetype/README.md)

-[Ligo](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/Ligo/README.md)

  

The program manages a crowdfunding activity: a user (representing our admin), will hold a fundraiser where anyone can participate, with the promise of a reward for investors once the goal or deadline is reached. (In our case we will simulate the Airdrop of a new token).

The money goal and expiration date are defined before opening the funding and cannot be changed.


There will be three actors:

* Smart Contract that will manage all operations and maintain funds

* Admin who will start the SC and -eventually- will receive the funds at the end

* Contributors, who will donate the money and -eventually- receive the Airdrop

  

## RULES:

* there is a range of participation fees, outside which it is not allowed to contribute

* tokens are calculated on the basis of the amount donated

* a contributor (address) can donate several times

* if a minimum cap is not reached (floor) all contributors will be refunded and crowdfunding will have failed
  

## COMPARISON
The order with which I realized the SC was:
1. [SmartPy](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy)
2. [Archetype](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/Archetype
3. [Ligo](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/Ligo)

#### SmartPy
Beyond the [initial](https://github.com/TheMastro-11/LearningTezos#smartpy) part of general understanding, SmartPy was the language I preferred in the realization of this Use Case.

No hitches or limitations.

The only flaw, the lack of *states* which i used on Archetype version.

#### Archetype
Archetype took very little time to build.

I appreciated the use of *states* and *transitions*.

It would have been better to keep the two SCs inside the same file.

#### Ligo
With Ligo, I had enormous difficulties. 

Terrible management of lists and maps that did not allow me to complete the SC as I did on others.

I have no idea how I could make TokenGen and then pass the address to CrowdFunding.


