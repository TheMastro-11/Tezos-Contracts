## DISCLAIMER

it's just a draft -> NOT definitive 


# KING OF TEZOS
Versions:
- [Smartpy](https://github.com/TheMastro-11/LearningTezos/blob/contracts/KingOfTezos/SmartPy/README.md)

King of Tezos is a game anyone can join.
The goal is to take the throne over others players.
The SC works like a cycle:
- The SC is deployed on chain
1. The floor price is setted (at this point it's everytime the same by default) and anyone can buy the throne at that price.
2. The throne has taken by an address that sent to SC the price. The price for a new buyer now increase of a x%. A timer setted randomly started.
3. At this time can happen two things:
    1. if someone takes the throne by paying the new price the old king will be refunded and the SC goes back on 2nd point. 
    2. Otherwise if the timer ends the king will be 'killed' and the SC goes back on 1st point. This is how the admin earns money.

There will be three actors:

- Smart Contract, that will manage all operations and maintain funds.
- Admin, who will start the SC and will earns money in case of point number 3.2.
- Players who will try to achieve and mantain the throne during the game.

  
## RULES:
There are no further rules other than the ones explained above.

## PROJECT STRUCTURE
This project needs only one Contract:
- `KingOfTezos` : that manages all the game.


### KING OF TEZOS

#### STATES
- `empty` : 1st point of the cycle.
- `newKing` : 2nd and 3.1th points.
- `kindIsDead` : 3.2th point.


#### DATA ITEM
- `king` : the realtime king. (For developing reasons could be the admin address the first time). 
- `history` : the full kings history. Is a map with address as key and a record combine by amount and date as value, referred to time when the throne has been taken.
- `floorPrice` : the realtime throne's price.


#### ENTRYPOINTS
- `newKing()` : check if the amount is correct and then replace the king
- `killKing()` : the timer ended and the king has to be 'killed'.


## USE CASE EXAMPLE
1. The admin started the game. The floor price is 1000tz. The throne is empty.
2. Luca buys the throne for 1000tz and now is the king. The price increases to 1100tz (10% more). The timer starts from 10 days.
3. Paolo buys the throne on 2nd day and became the king. The price increases to 1210tz. The timer restarts, this time for 6 days.
4. The new king is unlucky, no one bought the throne and he died. Price is resetted.
5. Paolo wants again to be king and buys the throne for 1000tz. The price increases to 1100tz and timer starts from 40 days.
- Now the game continues until one point between 3.1 and 3.2 happens.


## COMPARISON
The order with which I realized the SC was:
1. [SmartPy](https://github.com/TheMastro-11/LearningTezos/tree/contracts/CrowdFunding/SmartPy)

Differences:
1. On smartpy i cannot set `king` on a void value.
