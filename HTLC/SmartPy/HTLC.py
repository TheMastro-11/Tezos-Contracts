import smartpy as sp

class HashTimedLockedContract(sp.Contract):
    def __init__(self):
        self.init(collateral = sp.tez(0), deadline = sp.none, commiter = sp.none , receiver = sp.none, hash = sp.pack("standard"))

    @sp.entry_point
    def commission(self, deadline, receiver, hash):
        #save into data
        self.data.collateral = sp.amount
        self.data.deadline = sp.some(sp.level + deadline)
        self.data.receiver = sp.some(receiver)
        self.data.hash = hash
        
        self.data.commiter = sp.some(sp.sender)

    @sp.entry_point
    def reveal(self, word):
        #hash
        bytes = sp.pack(word) 
        hash = sp.keccak(bytes) #created
        sp.verify(self.data.hash == hash, "Wrong word") #checked

        #check receiver
        sp.verify(self.data.receiver == sp.some(sp.sender), "Wrong Address")
        #transfer collateral to receiver
        sp.send(self.data.receiver.open_some(), self.data.collateral)


    @sp.entry_point
    def timeout(self):
        #check if deadline is reached
        sp.verify(self.data.deadline == sp.some(sp.level), "Deadline not reached")

        #transfer collateral to commiter
        sp.send(self.data.commiter.open_some(), self.data.collateral)

        
    

@sp.add_test(name = "HTLC")
def testHTLC():
    #set scenario
    sc = sp.test_scenario()
    #create object HashTimedLockedContract
    htlc = HashTimedLockedContract()
    #start scenario
    sc += htlc

    #create users
    sofia = sp.test_account("sofia")
    pippo = sp.test_account("pippo")

    #create hash
    bytes = sp.pack("love")
    hash = sp.keccak(bytes)
    #first commission
    htlc.commission(sp.record(deadline = sp.nat(10) , receiver = sofia.address, hash = hash)).run(sender = pippo, amount = sp.tez(1000))
    #reveal after 50 rounds
    htlc.reveal("love").run(sender = sofia)
    #timeout after 100 rounds
    htlc.timeout().run(valid = False)
    

    
import smartpy as sp

class HashTimedLockedContract(sp.Contract):
    def __init__(self):
        self.init(collateral = sp.tez(0), deadline = sp.none, commiter = sp.none , receiver = sp.none, hash = sp.pack("standard"))

    @sp.entry_point
    def commission(self, deadline, receiver, hash):
        #save into data
        self.data.collateral = sp.amount
        self.data.deadline = sp.some(sp.level + deadline)
        self.data.receiver = sp.some(receiver)
        self.data.hash = hash
        
        self.data.commiter = sp.some(sp.sender)

    @sp.entry_point
    def reveal(self, word):
        #hash
        bytes = sp.pack(word) 
        hash = sp.keccak(bytes) #created
        sp.verify(self.data.hash == hash, "Wrong word") #checked

        #check receiver
        sp.verify(self.data.receiver == sp.some(sp.sender), "Wrong Address")
        #transfer collateral to receiver
        sp.send(self.data.receiver.open_some(), self.data.collateral)


    @sp.entry_point
    def timeout(self):
        #check if deadline is reached
        sp.verify(self.data.deadline == sp.some(sp.level), "Deadline not reached")

        #transfer collateral to commiter
        sp.send(self.data.commiter.open_some(), self.data.collateral)

        
    

@sp.add_test(name = "HTLC")
def testHTLC():
    #set scenario
    sc = sp.test_scenario()
    #create object HashTimedLockedContract
    htlc = HashTimedLockedContract()
    #start scenario
    sc += htlc

    #create users
    sofia = sp.test_account("sofia")
    pippo = sp.test_account("pippo")

    #create hash
    bytes = sp.pack("love")
    hash = sp.keccak(bytes)
    #first commission
    htlc.commission(sp.record(deadline = sp.nat(10) , receiver = sofia.address, hash = hash)).run(sender = pippo, amount = sp.tez(1000))
    #reveal after 50 rounds
    htlc.reveal("love").run(sender = sofia)
    #timeout after 100 rounds
    htlc.timeout().run(valid = False)
    

    
