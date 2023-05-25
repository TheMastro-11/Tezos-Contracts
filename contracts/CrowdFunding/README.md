# CrowdFunding
Crowdfunding is a smart contract I created to learn how to program on the Tezos blockchain.

For this reason, I have implemented it with all three languages available.

The contract allows users to donate native cryptocurrency to fund a campaign. To create the contract, one must specify:
- the recipient of the funds,
- the goal of the campaign, that is the least amount of currency that must be donated for the campaign to be successful,
- the deadline for the donations.

The goal and expiration date for the fundraiser are defined before opening the latter and cannot be changed.

There will be three actors:
- Smart contract, that will manage all operations and maintain funds.
- Admin, who will start the SC and will -eventually- receive the funds.
- Contributors, who will donate the money.

The contract implements four different rules:
- There is a range of participation fees, outside of which it is not allowed to participate.
- Contributors (address) can donate more than once. 
- If a minimum is not reached (floor), all contributors could request a refund and the crowdfunding will have failed.
  

## State Variables
- `startDate` : to mark the time of the beginning of the fundraising 
- `endDate` : the end of the fundraising, calculated in minutes from the beginning time
- `contributors` : map of contributors, with the address as key and the list of donations as value, to keep track of who donated and how during the fundraising
- `ceiling` : financial goal


## EntryPoints
- `checkResult()` : verifies whether the deadline and ceiling have been reached
- `contribute()` : called at the time of donation, verifies that the amount is correct and updates contributors
- `refund()` : refund contributors if the crowdfunding failed


## Use Case
1. A person that we'll call Mario decides to open fundraising for the creation of his token, called BitMario.
2. On 01/01/22 CrowdFunding's SC is deployed on the Tezos Blockchain with Mario as Admin. At that moment, all the [State Varaibles](#state-variables) are generated and `startDate` has 01/01/22, or the block number, as its value.
3. The token's project starts to spread on the internet and some users are interested in investing.
4. The first one is Alice: she signs the SC with her wallet and then `contribute()` is called with 100tz as amount. -Note that `contribute()` and `refund()` could be called by any user, while `checkResult()` only by the admin.-
5. Now the SC's balance is 100tz.
6.  Other people join and after 1 week, the fundraising reaches 1200tz.
7.  Mario set, before the SC was deployed, `ceiling` at 1500tz and `endDate` at 2 weeks.
8.  When the deadline is reached, Admin has to call `checkResult()`: if the ceiling is reached it can receive all the money, otherwise the contributors can ask for a refund.


## Differences
1. With LIGO it is not possible to finish the SC as with the others. In fact, LIGO is not usually used for this type of USECASE. The main issue is with the map and list management: I cannot check if an address already exists in `contributors` or update their *map-value* if they donate more than once. I tried using a *list-based-implementation*, but I was not able to concatenate two lists.
2. Only on the Archetype version I was able to use the *states-construct* which gives an extra layer of control during SC execution. Every time an entry is called, the compatibility of the *state* is automatically checked, e.g. `contribute()` can only be called on `funding`.
3. [`sp.verify`]( l ) on SmartPy allowed me to do any checks I needed without using the *if-else* construct. It is also very useful in case of a negative outcome, as it declines the *entry-call*. For example in [`contribute()`](https://github.com/TheMastro-11/Evaluating-execution-and-development-costs-in-the-Tezos-blockchain/tree/contracts/CrowdFunding/SmartPy/#contribute) , if the amount is not valid it sends back an error and the transaction is not sent. In fact, on SmartPy the actual transaction and related fee are only processed when the *entry* is completed without errors in all the actions inside. 
From a developer: 
> Instead of sending back if the amount is too low we fail.
As everything is transactional the amount is never transferred.

referring to : `sp.verify(sp.amount >= self.data.ticketPrice, message="AmountTooLow")` instead of my first version where the SC manually refunds the sender as [`sp.verify`](https://smartpy.io/docs/general/checking_condition/#asserts) fails.


