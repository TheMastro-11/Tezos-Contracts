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
  

# COMPARISON

