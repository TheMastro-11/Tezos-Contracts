## DISCLAIMER

it's just a draft -> NOT definitive
  

# BLIND AUCTION

Versions:

- [Smartpy](https://github.com/TheMastro-11/LearningTezos/tree/contracts/BlindAuction/SmartPy/README.md)


This contract manage an auction where each partecipant knows only its bid and not the others.
By this way each contestant tries to offer the biggest amount because afraid of the other proposal.
Also following this method an auction not requires long time to be competed, once the time starts and all the bidders sent their money (usually in minutes through blockchain), the winner could be discovered minutes right after.

There will be three actors:

- Smart Contract, that will manage all operations and maintain funds.
- Admin, who will start the SC and will receive the biggest bid at the end of the auction.
- Bidders, who will try to achieve the prize with their offer.


## RULES:
- There is minimum amount to offer.
- A partecipant can only make one offer. 
- The loosers will be refunded.
  

## PROJECT STRUCTURE
This project needs only one contract:
- `BlindAuction` : that manages the bidding process.

### BLIND AUCTION

#### STATES
- `funding` : during which the bidders can make thei offers.
- `winner` : during which the winner is announced.

#### DATA ITEM
- `bidders` : map of biddersm whit the address as key and the offer as value 
- `top` : the list of top bidder/s with relative amount, is a list in case there are two or more equals offers
- `minBid` : the mimimum value for a bid. 

#### ENTRYPOINTS
- `bid()` : called at the time of bidding, verifies that the amount is correct and updates bidders and eventually top
- `getWinner()` : called at the end, refunds the loosers and proclaims the winner.


## USE CASE EXAMPLE
1. A person that we'll call Mario decides to open an auction for selling his own epoque car. He set bidding on 01/01/23 from 12:00 to 12:15.
2. A lot of collectors and epoque car lovers decide to join the event.
3. Once the SC is open the bidders have only a quarter to make their own offer.
4. Giuseppe sent 1400tz, Carla 1200tz and Piero 5000tz.
5. At 12:20 the winner is announced, Giuseppe and Carla have been refunded and Piero is ready to collect is own prize. 


## COMPARISON
The order with which I realized the SC was:
1. [SmartPy](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy)





