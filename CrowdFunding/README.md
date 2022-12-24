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
  

## PROJECT STRUCTURE
This project needs two differents contracts:
* `CrowdFunding` : that manage the donation process.
* `TokenGen` : that manage the airdrop (in case of success).

### CROWDFUNDING

#### DATA ITEM
There are 8 essentials variables/constants:

*  `startDate` : to pin the time when the fundraising started

*  `endDate` : the end of the fundraising calculated in days from the beginning

*  `contributors` : map of contributors to keep trace of who donated during the fundraising

*  `minAmount` : minimum donation for single transaction

*  `maxAmount` : maximum donation for single e total transactions

*  `ceiling` : financial goal that if reached allows the funding to be succeful before the `endDate`

*  `floor` : minimum target to be reached

*  `isSuccess` : success indicator at the end of the fundraising


#### ENTRYPOINTS

There are 4 essentials entrypoints:

* `checkTime()` : Checks if the deadline has been reached.

* `contribute()` : Called at the time of donation, checks that the amount is correct and updates `contributors`.

* `checkFloor()` : Checks if `floorPrice` has been reached, if so updates `isSuccess` otherwise it refunds `contributors`.
  
* `endFunding()` : Finalizes the crowdfunding sending the funds to the [SC](#TokenGen) for the airdrop.

The total number and them implementations could be differents based on single language.


### TokenGen

#### DATA ITEM:

*  `supply` : indicate the total supply of the token.

*  `contributors` : keep track of donors and the number of tokens they will receive.


#### ENTRYPOINT:
*   `airdrop()` : Simulate the sending of tokens to donators by inserting the corresponding amount in `contributors`.

#### USE CASE EXAMPLE
1. A person that we'll call Mario decides to open a fundraising for the creation of his own token called BitMario. 
2. On 01/01/22 the CrowdFunding's SC is been deployed on the Tezos Blockchain with Mario as Admin, on that moment all the DATA ITEMs are generated and `startDate` has 01/01/22, or the block number, as own value.
3. The token's project started to spread on internet and some users are interested to make an investement.
4. The first one is Alice: she signs the SC with her wallet and then `contribute()` is called with 100tz as amount.
-Note that only `contribute` could be called by any user, while the other *entrypoints* only by the admin.-
5. Now the SC's balance is 100tz.
6. The next one is Bob: he donated 50tz but `contribute()` refused because the `minAmount` is set on 100tz.
7. The SC's balance is still 100tz.
8. On 01:00 of every day since the beginning `chechTime()` and `checkFloor()` are called (imagine is done automatically) by Admin. 
9. Other people join and after 1 week the fundraising reachs 1200tz.
10. Mario has setted, before the SC was deployed, `ceiling` at 5000tz, `floor` at 1500tz and `endDate` at 2 weeks.
11. At the deadline Admin has to call for the last time `checkFloor()`, if it returns true (not this case) the admin can call `endFunding()` otherwise the SC automatically refunds all the contributors.


## COMPARISON
The order with which I realized the SC was:
1. [SmartPy](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy)
2. [Archetype](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/Archetype)
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


