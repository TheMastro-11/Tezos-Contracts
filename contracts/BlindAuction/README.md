# Blind Auction
This contract manage an auction where each partecipant knows only its bid and not the others.
By this way each contestant tries to offer the biggest amount because afraid of the other proposal.
Also following this method an auction not requires long time to be competed, once the time starts and all the bidders sent their money (usually in minutes through blockchain), the winner could be discovered minutes right after.

There will be three actors:

- Smart Contract, that will manage all operations and maintain funds.
- Admin, who will start the SC and will receive the biggest bid at the end of the auction.
- Bidders, who will try to achieve the prize with their offer.

The contract implements three differents rules:
- There is minimum amount to offer.
- A partecipant can only make one offer. 
- The loosers will be refunded.
 
## State Variables
- `bidders` : map of bidders with the address as key and the offer as value 
- `top` : the list of top bidder/s with relative amount, is a list in case there are two or more equals offers
- `minBid` : the mimimum value for a bid. 

## EntryPoints
- `bid()` : called at the time of bidding, verifies that the amount is correct and updates bidders and eventually top
- `getWinner()` : called at the end, refunds the loosers and proclaims the winner.

## Use Case
1. Mario open an auction for selling his own epoque car. He set bidding on 01/01/23 from 12:00 to 12:15.
2. A lot of collectors and epoque car lovers decide to join the event.
3. Once the SC is open the bidders have only a quarter to make their own offer.
4. Giuseppe sent 1400tz, Carla 1200tz and Piero 5000tz.
5. At 12:20 the winner is announced, Giuseppe and Carla have been refunded and Piero is ready to collect is own prize. 
