import smartpy as sp

class HashTimedLockedContract(sp.Contract):
    def __init__(self):
        self.init(deadline = sp.none, committer = sp.none , receiver = sp.none, hash = sp.none)

    @sp.entry_point
    def commit(self, deadline, receiver, hash):
        #save into data
        self.data.deadline = sp.some(sp.level + deadline)
        self.data.receiver = sp.some(receiver)
        self.data.hash = sp.some(hash)
        
        self.data.committer = sp.some(sp.sender)

    @sp.entry_point
    def reveal(self, word):
        #hash
        sp.set_type(word, sp.TString)
        bytes = sp.pack(word) 
        hash = sp.keccak(bytes) #created
        sp.verify(self.data.hash == sp.some(hash), "Wrong word") #checked

        #transfer collateral to commiter
        sp.send(self.data.committer.open_some(), sp.balance)


    @sp.entry_point
    def timeout(self):
        #check if deadline is reached and if sender is the commiter
        sp.verify(self.data.deadline <= sp.some(sp.level), "Deadline not reached")
        sp.verify(self.data.receiver == sp.some(sp.sender), "You're not the receiver")

        #transfer collateral to receiver
        sp.send(self.data.receiver.open_some(), sp.balance)

        
    

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
    secret = "love"
    bytes = sp.pack(secret)
    hash = sp.keccak(bytes)
    #first commit
    htlc.commit(sp.record(deadline = sp.nat(10) , receiver = sofia.address, hash = hash)).run(sender = pippo, amount = sp.mutez(1000))
    #reveal after 50 rounds
    htlc.reveal("love").run(sender = pippo)
    #timeout after 100 rounds
    htlc.timeout().run(sender = sofia, level = 1000)




