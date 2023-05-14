import smartpy as sp

class FeeTransfer(sp.Contract):
    def __init__(self, admin):
        self.init(admin = admin)

    @sp.entrypoint
    def purchaseWithFee(self, cAddress, param):
        #calculate fee
        fee = sp.split_tokens(sp.amount, 1, 100)
        #send fee
        sp.send(self.data.admin, fee)
        #send price
        c = sp.contract(sp.TNat, cAddress, entrypoint="purchase").open_some()
        sp.transfer(param, (sp.amount - fee) , c)


class ContractExample(sp.Contract):
    def __init__(self):
        self.init( param = sp.nat(0))

    @sp.entrypoint
    def purchase(self, param):
        self.data.param = param
        

@sp.add_test(name = "HTLC")
def testHTLC():
    #set scenario
    sc = sp.test_scenario()
    #create object FeeTransfer
    #create admin
    bob = sp.test_account("bob")
    ft = FeeTransfer(bob.address)
    #create object ContractExample
    ce = ContractExample()
    #start scenario
    sc += ft 
    sc += ce

    #create user
    alice = sp.test_account("alice")

    #first transfer
    ft.purchaseWithFee(sp.record(cAddress = ce.address, param = sp.nat(10))).run(sender = alice, amount = sp.mutez(1000))




