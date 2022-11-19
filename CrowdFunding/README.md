## DISCLAIMER

it's just a draft -> NOT definitive

It has to be translated in English.

  

# <center> CROWDFUNDING<center>

  

Crowdfunding è uno Smart Contract realizzato con l'obiettivo di imparare a programmare sulla blockchain Tezos.

Per questo motivo è stato implementato con tutti e tre i linguaggi disponibili:

-Smartpy

-Archetype

-Ligo

  

Il programma si occupa di gestire un'attività di CrowdFunding: un utente (che rappresenterà il nostro admin),

indirrà una raccolta fondi a cui chiunque può partecipare, con la promessa di una ricompensa per gli investitori una volta raggiunto l'obiettivo o la scadenza. (Nel nostro caso simuleremo l'airdrop di un nuovo token)

L'obiettivo di denaro e la scadenza vengono definiti prima di aprire la raccolta e non possono essere modificati.

  

Gli attori saranno tre:

* Smart Contract che gestirà tutte le operazioni e manterrà i fondi

* Admin che avvierà lo SC e -eventualmente- riceverà i fondi al termine

* Contribuenti, che doneranno i soldi e -eventualmente- riceveranno l'airdrop

  

## RULES:

* esiste un range di quota di partecipazione, al di fuori del quale non è concesso entrare

* i token ditribuiti sono calcolati sulla base della quantità donata

* un contribuente (address) può donare più volte

* se alla scadenza non viene raggiunto un tetto minimo(floor) tutti i contribuenti verrano rimborsati e il crowdfunding avrà fallito

  

# SMARTPY [Link](https://smartpy.io/ide?code=eJzlWN1u2zYUvg@QdyDsG2n1hLgohiFYhwXpspt1GBbfFYHAUJTNRiYFkYqTFHuXvUtfrOeQlETaUpx129V0k4SH5@87v4zY1qoxRG9pY@pHQjXR9enJ6QmrqNbkslG74qqVhZDrRNfZpZKmocyk56cnBL6ClyTPhRQmzxPNq3IBR7SohOTdFfyQkuGtRBvQ844aTt6CosyILYejbZ2cpQvCZeFJywVhqErctkY12l3e0jqp4NdPfy6IueOP7nR1URQN1xrO7mnVesGrX4U2aPHqfWv4U0pA_FbIi61qpfHikJAsUfGWPoxRzpDGuAB31vsUSysrpZqQ8toeC33dMgY2OdKtUlVyRSvNU0JSBBcx@QkoHFx8zGslpBnwZBvO7lYAjAcUMQrBLERZIhmEI4l86@AtqKFZD2@AfZ3d80aUj0nP@MNbx7Lm5poDzoVOEAQwmK5R7Gy14U620EQB96y3Gg0M2FBMaFvDTdtI1MnUtgZIksG2LrrfkO@_ewM4Oa5jYHRZwA90zS1QRJR9iMDahlM4Lsbcx0jQikrGySs8pi7iHRjWRi8pAuPSS_eiZ6k1eswOLxHMuOVmx7nElCNUFphgEyZ5nh9DK_pEjezwGWqUIpXazdLnBUZu9fk9JXAj1ptQYuAdLQqiJKmgniKN4G8Q3LBa7R9USI3maAg7b9L0PJAZoyYM2YmqcvgSA6kH5nZY7oTZEAWHDSmUpEYoGcupm_t3SvpKqxSjVTLzZ7PFUJhnaTrJh064olMG2Med@tD7crMnaUC_Fxrl19E4vAd3fSz@6HNsT8cxm7K61Zsh_CmZa064hqBxshaf_4pCx6EVnf9NBWCoRRjb6odezw20J99wfZ@dQ9wBDc0UETA2GvH0pPoqhhLnYdm_pBNeYY99pvhdD54ofaAHZR@GwrLtgTCH61IZkFTCyCMUktImHSARX6Ru5OCMiRIvOMfkG68OmFzQbw@TqEQ3CDaMQUpmR9qemfjZurAz0bBNDvJ1csCW4jR_WI5wBz6A_Q_LbAND@9lrg1THAPVdjTP4lOnMWby0vvz9mzQ9lqtz2w92AjKc4X5Suv0Ec6CEJUNDEhDtBnDZVtXjVKaHY3rVtFFmDoO4t3lhe2AeZqFBYpQB9oRPdh4f5o8YZittz7WRsDqlk6G0Cn1kXj0TSytmLHZ@ZAdycNYfqUwIcL8VWmiY38KiGqWiKRpVE8l3IP@OB62bOdSY3yfdpgb7XbTQjexx6aAK98XeNOyjXt0szVTNZa4VrFAx9qBL6pI3Ezm4CJoF6EmHPXiF1v_C5Yt24InNt63rCnfW5esz9_3jHfc3atJ@MzsSMQ@ODxctAOzQTlqMNDPfx@zlw7YVt6zJbjXaqV7SpF7QoEJBz_WlIy3Hud0aUWlXtLlROfT9ZL91WSSCTgW7LEYzXI7_z00Dkw_AyQ286RJJt259Dlo0rpgIEl6w50kHDKwr8AhlXNJGKHekfY_Ay3lH6gp6zmDcw26jbj9yZqI54C6w4OUKcqKH7PLNuBTjq9wRu79wOnTl3_HZd9ahvYBlqDc8H2THqlvYlvx2UYu6VoHPlDHcsWCfRUK3nmtVCjp2yxL6W7xZi1FhjjK86Ix7Su49xsE@WrG2QhP5A2ctbt72bsSFP2zIN6ptdLLstLNss0xml3ZHwydnZ1aITjY8dO0TN2L93WJx2b_@xgUMj8M0a1roznZXBbssYovuERE_92NF1xbOr1ZkQR9XtK9p3yVysYZH0r_n2IFnLgW@3jXLP6FrX9mFMXxbYwn9N1iiQnsbmo0ogOj@nxLZ4J4EdrGfzjf3nIgZf4Zl_2roUAeMwbbTlXHmhwBc_wLww9CI)
Nella versione di smartpy troviamo due SC:

 **CrowdFunding**:

* Attributes:

*  `startDate = sp.timestamp(0)` : data di inizio

*  `endDate = x` : data di fine espressa in giorni

*  `contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TList(sp.TMutez) )` : mappa dei donatori

*  `minAmount = sp.mutez(10)` : minima donazione

*  `maxAmount = sp.mutez(1000)` : massima donazione

*  `ceiling = sp.mutez(100000)` : obiettivo economico

*  `floor = sp.mutez(200)` : tetto minimo da raggiungere

*  `isSuccess = sp.bool()` : indicatore successo al termine della raccolta

<br>
 EntryPoints:

```

@sp.entry_point

def checkTime(self, time):

diffTime = time - self.data.startDate

sp.verify(diffTime <= self.getHours(), message = "The time is over")

```

controlla il frame temporale dall'apertura del crowdfunding al momento in cui viene invocato

```

@sp.entry_point

def contribute(self):

#check if ceiling is reached

sp.verify(sp.balance + sp.amount <= self.data.ceiling, message = "Ceiling reached")

#check if amount is between min and max

sp.verify(sp.amount >= self.data.minAmount, message = "Amount too low")

sp.verify(sp.amount <= self.data.maxAmount, message = "Amount too high")

#add on list

sp.if (self.data.contributors.contains(sp.sender)):

#check if it will reach the max amount with other donation

prvDons = sp.local("prvDons", sp.mutez(0))

prvDons = self.checkTotal(self.data.contributors[sp.sender])

sp.verify( prvDons + sp.amount < self.data.maxAmount, message = "Max Amount Reached")

self.data.contributors[sp.sender].push(sp.amount) #se esiste già

sp.else:

self.data.contributors[sp.sender] = sp.list([sp.amount], t = sp.TMutez) #inserisco indirizzo contribuente

```

invocata al momento della donazione, verifica che al cifra sia corretta e aggiorna `contributors`

```

@sp.entry_point

def checkFloor(self):

#check if floor is reached

sp.if sp.balance < self.data.floor:

#if not refund all donators

addressList = sp.local("addressList", self.data.contributors.keys())

sp.for i in addressList.value:

with sp.match_cons(addressList.value) as x1:

address = x1.head

addressList.value = x1.tail

sp.send(address, self.checkTotal(self.data.contributors[address]))

sp.else:

#otherwise crowdfunding is finished successfully

self.data.isSuccess = True

```

verifica che `floor` sia raggiunto, in caso positivo aggiorna `isSuccess` altrimenti rimborsa i `contributors`

  

```

@sp.entry_point

def endFunding(self, cAddress):

#airdrop new token

c = sp.contract(sp.TMap(sp.TAddress, sp.TList(sp.TMutez)), cAddress, entry_point = "airdrop").open_some()

sp.transfer(self.data.contributors, sp.balance, c)

```

si occupa di richiamare lo SC che si occupa dell'airdrop

*↓↓↓ **TokenGen** descritto sotto ↓↓↓*

  
<br>
 Methods:

```

def getHours(self):

return sp.compute(self.data.endDate * 24)

```

trasforma x giorni nel numero di ore corrispondenti

  

```

def checkTotal(self, list_):

total = sp.local("totale", sp.mutez(0))

sp.for j in list_:

with sp.match_cons(list_) as x1:

total.value += x1.head

list_ = x1.tail

return total.value

```

calcola il totale che è stato raccolto

<br><br>

**TokenGen**:

Attributes:

*  `supply = 120000000` : indica la totale supply del token

*  `contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TNat` : tiene conto dei donatori e del numero di token che riceveranno
<br>

EntryPoints:
```
@sp.entry_point

def airdrop(self, adMap):

adList = sp.local("adList", adMap.keys())

sp.for i in adList.value:

with sp.match_cons(adList.value) as x1:

address = x1.head

adList.value = x1.tail

self.data.contributors[address] = sp.utils.mutez_to_nat(self.checkTotal(adMap[address])) * 1200

```

l'invio dei token è simulato inserendo l'ammontare corrispondente nella map

  
  

## Test Scenario

Lo scenario in SP ci permette di testare gli entry_points e le classi da noi realizzate prima di un'effettiva pubblicazione sulla chain

[Link](https://smartpy.io/docs/scenarios/testing/)
