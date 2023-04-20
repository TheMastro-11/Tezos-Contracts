import smartpy as sp

class NavalBattle(sp.Contract):
    def __init__(self):
        self.init(players = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TNat), entryPrice = sp.tez(1))

    @sp.entry_point
    def joinGame(self):
        sp.verify(sp.amount == self.data.entryPrice, message = "amount incorrect")
        self.data.players[sp.sender] = 8

class Player(sp.Contract):
    def __init__(self, address):
        self.init(account = address, grid = sp.map(l = {}, tkey = sp.TNat, tvalue = sp.TMap(sp.TNat, sp.TBool)), ship = sp.map(l = {}, tkey = sp.TString, tvalue = sp.TNat), army = sp.map(l = {}, tkey = sp.TString, tvalue = sp.TNat))

    @sp.entry_point
    def startArmy(self, ironclad, carrier, submarine, boat):
        self.data.army["ironclad"] = ironclad
        self.data.army["carrier"] = carrier
        self.data.army["submarine"] = submarine
        self.data.army["boat"] = boat
        
    @sp.entry_point
    def startShip(self, ironclad, carrier, submarine, boat):
        self.data.ship["ironclad"] = ironclad
        self.data.ship["carrier"] = carrier
        self.data.ship["submarine"] = submarine
        self.data.ship["boat"] = boat
    
    @sp.entry_point
    def startGrid(self, x, y):
        xGrid = sp.local("xGrid", sp.map(l = {}, tkey = sp.TNat, tvalue = sp.TBool))
        sp.for i in sp.range(1, x, step = 1):
            xGrid.value[i] = False 
        
        sp.for j in sp.range(0, y, step = 1):
            self.data.grid[j] = xGrid.value


    @sp.entry_point
    def deploy(self, ship, x, y, orientation):
        #verify if input is correct
        sp.verify((orientation == "vr") | (orientation == "ho"), message = "wrong input orientation")
        sp.verify(self.data.army.contains(ship), message = "ship not found")
        
        #get ship dimension
        dim = sp.local("dim", self.data.army[ship]) 
        
        #vertical orientation
        sp.if (orientation == "vr"): 
            sp.verify((y + dim.value) <= sp.len(self.data.grid), message = "size incorrect")
            xTmp = sp.local("xTmp", sp.map(l = {}, tkey = sp.TNat, tvalue = sp.TBool))
            sp.for i in sp.range(y, (y+dim.value), step = 1):
                xTmp.value = self.data.grid[i] #get map
                xTmp.value[x] = True #update value
                self.data.grid[i] = xTmp.value #update grid



@sp.add_test(name = "Test Naval Battle")
def testBattle():
    #set up scenario
    sc = sp.test_scenario()

    #new object NavalBattle
    battle = NavalBattle()

    #create users
    pl1 = sp.test_account("player1")
    pl2 = sp.test_account("player2")

    #create players
    player1 = Player(pl1.address)
    player2 = Player(pl2.address)

    #start scenario
    sc.h1("Initiale State")
    sc += battle
    sc.h1("Player 1")
    sc += player1
    sc.h1("Player 2")
    sc += player2

    #configure game
    sc.h1("Player1.start")
    player1.startArmy(sp.record(ironclad = 5, carrier = 4, submarine = 3, boat = 1))
    player1.startShip(sp.record(ironclad = 1, carrier = 1, submarine = 2, boat = 4))
    player1.startGrid(sp.record(x = 10, y = 10))
    sc.h1("Player2.start")
    player2.startArmy(sp.record(ironclad = 5, carrier = 4, submarine = 3, boat = 1))
    player2.startShip(sp.record(ironclad = 1, carrier = 1, submarine = 2, boat = 4))
    player2.startGrid(sp.record(x = 10, y = 10))

    #join game
    sc.h1("JoinGame")
    battle.joinGame().run(sender = pl1, amount = sp.tez(1))
    battle.joinGame().run(sender = pl2, amount = sp.tez(2)).run(valid = False)
    battle.joinGame().run(sender = pl2, amount = sp.tez(1))

    #deploy army
    player1.deploy(sp.record(ship = "ironclad", x = 1, y = 5, orientation = "vr" ) ).run(valid = False)
    player1.deploy(sp.record(ship = "ironclad", x = 1, y = 1, orientation = "vr" ) )
