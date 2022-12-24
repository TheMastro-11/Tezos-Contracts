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

#### STATES
There are only 2 states:

* `funding` : during which only `endFunding()` cannot be called. 

* `airdrop` : the fundraising has ended successfully and only `endFunding()` can be called.

* `refund` : the `floor` is not reached, all the refund-transaction have been already sent and from this moment on no further action can be executed. 

#### DATA ITEM
There are 8 essentials variables/constants:

*  `startDate` : to pin the time when the fundraising started

*  `endDate` : the end of the fundraising calculated in days from the beginning

*  `contributors` : map of contributors, with the address as key and the list of donations as value, to keep trace of who and how donated during the fundraising

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


### TOKENGEN

#### DATA ITEM:

*  `supply` : indicate the total supply of the token.

*  `contributors` : keep track of donors and the number of tokens they will receive.


#### ENTRYPOINT:
*   `airdrop()` : Simulate the sending of tokens to donators by inserting the corresponding amount in `contributors`.

## USE CASE EXAMPLE
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

Differences: 
1. With LIGO is not possible to finish the SC as with the others.
In fact LIGO is not usually used for this type of USECASE.
The main issue is with the map and list management: I cannot check if an address already exists in `contributors` or update his *map-value* if donates more than one time.
I tried to use a *list-based-implementation* but I were not able to concatenate two lists.
2. Only on Archetype verion I could use the *states-construct* which gives an extra layer of control during SC execution. In fact every time a entry is called is automatically checked if the *state* is compatible, e.g. `contribute()` is only callable on `funding`.
3. [`sp.verify`](https://smartpy.io/docs/general/checking_condition/#asserts) on SmartPy allowed me to do any checks I needed without using the *if-else* construct.
Is also very useful because in case of negative outcome declines the *entry-call*. 
For example in [`contribute()`](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy/#contribute) if the amount is not valid it gives an error and the transaction is not sent.
In fact on SmartPy the actual transaction and related fee are only processed when the *entry* complete without errors all the actions inside.

