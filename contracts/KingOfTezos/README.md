# KING OF TEZOS
King of Tezos is a game anyone can join.
The goal is to win the throne over other players.
The SC works like a cycle:
- The SC is deployed on chain
1. The floor price is set (at this point it's the same every time by default) and anyone can buy the throne at that price.
2. The throne is taken by an address that sent the price to SC. The price for a new buyer now increases by x%. A randomly set timer starts.
3. At this point two things can happen:
    1. If someone takes the throne by paying the new price, the old king will be refunded and the SC goes back on 2nd point. 
    2. Otherwise, if the timer ends the king will be 'killed' and the SC goes back on 1st point. This is how the admin earns money.

There will be three actors:
- Smart contract, that will manage all operations and maintain funds.
- Admin, who will start the SC and will earn money in case of point 3.2.
- Players who will try to achieve and maintain the throne during the game.

## State Variables
- `king` : the real-time king. (For developing reasons the default could be the admin address). 
- `history` : the full kings' history. It is a map with the address as key and a record, formed by amount and date, as value, both referring to the time when the throne has been taken.
- `floorPrice` : the throne's real-time price.


#### EntryPoints
- `newKing()` : checks if the amount is correct and then replaces the king
- `killKing()` : the timer ended and the king has to be 'killed'.


## Use Case
1. The admin started the game. The floor price is 1000tz. The throne is empty.
2. Luca buys the throne for 1000tz and is now the king. The price increases to 1100tz (10% more). The timer for 10 days starts.
3. Paolo buys the throne on the 2nd day and becomes the king. The price increases to 1210tz. The timer restarts, this time for 6 days.
4. The new king is unlucky, no one else bought the throne and he dies. The price is reset.
5. Paolo wants to be king again and he buys the throne for 1000tz. The price increases to 1100tz and the timer starts for 40 days.
- Now the game continues until either point 3.1 or 3.2 happens.

