## DISCLAIMER

it's just a draft -> NOT definitive

It has to be translated in English.

  

# CROWDFUNDING

Crowdfunding is a Smart Contract I created with the aim of learning how to program on the Tezos blockchain.

For this reason, I have implemented it with all three languages available:

-[Smartpy](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/SmartPy/README.md)

-[Archetype](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/Archetype/README.md)

-[Ligo](https://github.com/TheMastro-11/LearningTezos/blob/contracts/CrowdFunding/Ligo/README.md)

The program manages a crowdfunding activity: a user (representing our admin), will hold a fundraiser where anyone can participate, with the promise of a reward for investors once the goal or deadline is reached (in our case, the Airdrop of a new token). 

The goal and expiration date for the fundraiser are defined before opening the latter and cannot be changed.

There will be three actors:

- Smart Contract, that will manage all operations and maintain funds.
- Admin, who will start the SC and will -eventually- receive the funds.
- Contributors, who will donate the money and -eventually- receive the Airdrop.

  

## RULES:

- There is a range of participation fees, outside of which it is not allowed to participate
- Tokens are calculated based on the amount donated. 
- Contributors (address) can donate more than once. 
- If a minimum is not reached (floor), all contributors will be refunded and the crowdfunding will have failed.
  

## PROJECT STRUCTURE
This project needs two different contracts:
- `CrowdFunding` : that manages the donation process.
- `TokenGen` : that manages the Airdrop (in case of success).

### CROWDFUNDING

#### STATES
- `funding` : during which only endFunding() cannot be called.
- `airdrop` : the fundraising has ended successfully and only endFunding() can be called.
- `refund` : the floor is not reached, all the refund-transactions have already been sent and from this moment on no further action can be executed.

#### DATA ITEM
- `startDate` : to mark the time of the beginning of the fundraising 
- `endDate` : the end of the fundraising, calculated in days from the beginning time
- `contributors` : map of contributors, with the address as key and the list of donations as value, to keep trace of who donated and how during the fundraising
- `minAmount` : minimum donation for single transaction
- `maxAmount` : maximum donation for single and total transactions
- `ceiling` : financial goal that, if reached, allows the funding to be successful before the endDate
- `floor` : minimum target to be reached
- `isSuccess` : success indicator at the end of the fundraising


#### ENTRYPOINTS
- `checkTime()` : verifies whether  the deadline has been reached
- `contribute()` : called at the time of donation, verifies that the amount is correct and updates contributors.
- `checkFloor()` : Checks if floorPrice has been reached, if so updates isSuccess, otherwise it refunds contributors.
- `endFunding()` : Finalizes the crowdfunding sending the funds to the [SC](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding#TokenGen) for the airdrop.


### TOKENGEN

#### DATA ITEM:
- `supply` : indicates the total supply of the token.
- `contributors` : keeps track of donors and the number of tokens they will receive.


#### ENTRYPOINT:
- `airdrop()` : Simulates the sending of tokens to donators by inserting the corresponding amount in contributors

## USE CASE EXAMPLE
1. A person that we'll call Mario decides to open a fundraising for the creation of his own token, called BitMario.
2. On 01/01/22 the CrowdFunding's SC is deployed on the Tezos Blockchain with Mario as Admin. At that moment, all the DATA ITEMs are generated and `startDate` has 01/01/22, or the block number, as its own value.
3. The token's project starts to spread on the internet and some users are interested in making an investment.
4. The first one is Alice: she signs the SC with her wallet and then `contribute()` is called with 100tz as amount. -Note that only contribute could be called by any user, while the other *entrypoints* only by the admin.-
5. Now the SC's balance is 100tz.
6. The next investor is Bob: he donats 50tz but `contribute()` refused because the `minAmount` is set on 100tz.
7. The SC's balance is still 100tz.
8. On 01:00 pm of every day since the beginning `chechTime()` and `checkFloor()` are called (imagine it is done automatically) by Admin.
9. Other people join and after 1 week, the fundraising reaches 1200tz.
10. Mario set, before the SC was deployed, `ceiling` at 5000tz, `floor` at 1500tz and `endDate` at 2 weeks.
11. When the deadline is reached, Admin has to call `checkFloor()` for the last time: if it returns true (not in this case) the admin can call `endFunding()`, otherwise the SC automatically refunds all the contributors.


## COMPARISON
The order with which I realized the SC was:
1. [SmartPy](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy)
2. [Archetype](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/Archetype)
3. [Ligo](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/Ligo)

Differences:
1. With LIGO it is not possible to finish the SC as with the others. In fact, LIGO is not usually used for this type of USECASE. The main issue is with the map and list management: I cannot check if an address already exists in `contributors` or update their *map-value* if they donate more than once. I tried using a *list-based-implementation*, but I was not able to concatenate two lists.
2. Only on the Archetype version I was able to use the *states-construct* which gives an extra layer of control during SC execution. Every time an entry is called, the compatibility of the *state* is automatically checked, e.g. `contribute()` can only be called on `funding`.
3. [`sp.verify`]( l ) on SmartPy allowed me to do any checks I needed without using the *if-else* construct. It is also very useful in case of negative outcome, as it declines the *entry-call*. For example in [`contribute()`](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy/#contribute) , if the amount is not valid it sends back an error and the transaction is not sent. In fact, on SmartPy the actual transaction and related fee are only processed when the *entry* is completed without errors in all the actions inside. From a developer:
>Instead of sending back if the amount is too low we fail.
As everything is transactional the amount is never transferred.

referring to : `sp.verify(sp.amount >= self.data.ticketPrice, message="AmountTooLow")` instead of my first version where the SC manually refunds the sender as [`sp.verify`](https://smartpy.io/docs/general/checking_condition/#asserts) fails.


