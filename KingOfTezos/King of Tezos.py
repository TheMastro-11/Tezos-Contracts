import smartpy as sp

class Throne(sp.Contract):
    def __init__(self, admin):
        self.init(king = admin, history = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TRecord(value = sp.TMutez, data = sp.TTimestamp)), floorPrice = sp.mutez(5000))
    @sp.entry_point
    def newKing(self):
        #verify amount
        sp.verify(sp.amount == self.data.floorPrice, message = "Amount incorrect")
        #refund previous king
        #sp.if self.data.king != self.data.admin: with # send to admin the revenue
        sp.send(self.data.king, sp.amount)
        #update history
        self.data.history[sp.sender] = sp.record(value = sp.amount, data = sp.now)
        self.data.king = sp.sender
        #update price -> plus 10%
        self.data.floorPrice += sp.fst(sp.ediv(self.data.floorPrice, sp.nat(10)).open_some()) 

    @sp.entry_point
    def deThrone(self):
        #reset king
        self.data.king = sp.sender
        #reset floorPrice
        self.data.floorPrice = sp.mutez(5000)
        

@sp.add_test("testThrone")
def testThrone():
    #create scenario
    sc = sp.test_scenario()
    #create admin
    admin = sp.test_account("admin")
    #object Lottery
    throne = Throne(admin.address)
    #start scenario
    sc.h1("Initial State")
    sc += throne

    #users
    sofia = sp.test_account("sofia")
    sergio = sp.test_account("sergio")

    #first king
    sc.h1("First King")
    throne.newKing().run(sender = sofia, amount = sp.mutez(5000))
    #failed attempt
    sc.h1("Failed Attempt")
    throne.newKing().run(valid = False, sender = sergio, amount = sp.mutez(5000))
    #second King
    sc.h1("Second King")
    throne.newKing().run(sender = sergio, amount = sp.mutez(5500))
    #deThrone
    sc.h1("End of reign")
    throne.deThrone().run(sender = admin)

     
