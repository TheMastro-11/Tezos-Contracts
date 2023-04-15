import smartpy as sp

class SimpleTransfer(sp.Contract):
    def __init__(self):
        self.init(receiver = sp.none)

    @sp.entry_point
    def deposit(self, receiver):
        #update data
        self.data.receiver = sp.some(receiver)
        
    @sp.entry_point
    def withdraw(self):
        #check receiver
        sp.verify(self.data.receiver == sp.some(sp.sender), "Wrong Address")

        #withdraw
        sp.send(self.data.receiver.open_some(), sp.balance)

@sp.add_test(name = "SimpleTransfer")
def testSimpleTransfer():
    #set scenario
    sc = sp.test_scenario()
    #create object SimpleTransfer
    sitr = SimpleTransfer()
    #start scenario
    sc += sitr

    #create users
    sofia = sp.test_account("sofia")
    pippo = sp.test_account("pippo")

    #deposit
    sitr.deposit(sofia.address).run(amount = sp.tez(10))
    #withdraw
    sitr.withdraw().run(sender = sofia)
    

    
