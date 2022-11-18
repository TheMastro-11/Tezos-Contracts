## DISCLAIMER
it's just a draft -> NOT definitive

# CROWDFUNDING
Crowdfunding è uno Smart Contract realizzato con l'obiettivo di imparare a programmare sulla blockchain Tezos.
Per questo motivo è stato implementato con tutti e tre i linguaggi disponibili:
-Smartpy
-Archetype
-Ligo

Il programma si occupa di gestire un'attività CrowdFunding: un utente (che rappresenterà il nostro admin),
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

# SMARTPY
Nella versione di smarty troviamo due SC:
* **CrowdFunding**:
 * Attributes:
	* `startDate = sp.timestamp(0)` : data di inizio
	* `endDate = x` : data di fine
	* `contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TList(sp.TMutez) )` : mappa dei donatori 
	* `minAmount = sp.mutez(10)` : minima donazione
	* `maxAmount = sp.mutez(1000)` : massima donazione
	* `ceiling = sp.mutez(100000)` : obiettivo economico
	* `floor = sp.mutez(200)` : tetto minimo da raggiungere
	* `isSuccess = sp.bool()` : indicatore successo al termine della raccolta 
	
 * EntryPoints:
	* # checktime() : diffTime = time - self.data.startDate sp.verify(diffTime <= self.getWeeks(), message = "The time is over")
	controlla il frame temporale dall'apertura del crowdfunding al momento in cui viene invocato
 	* contribute() : invocata al momento della donazione, verifica che al cifra sia corretta e aggiorna 'contributors'
	* checkFloor() :


