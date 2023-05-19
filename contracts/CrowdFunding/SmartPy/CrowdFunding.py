import smartpy as sp

class CrowdFunding(sp.Contract):
    def __init__(self, admin, deadline):
        self.init(admin = admin, startDate = sp.timestamp(0), endDate = deadline, contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TList(sp.TMutez) ), ceiling = sp.mutez(100000))

    @sp.entry_point
    def checkResult(self, time):
        sp.verify(sp.sender == self.data.admin, message = "You are not the Admin")
        sp.verify(time >= self.data.startDate.add_minutes(self.data.endDate), message = "The time is not over")
        sp.verify(sp.balance >= self.data.ceiling, message = "Crowdfund failed")
        #send all money to Admin
        sp.send(self.data.admin, sp.balance)


    def getSeconds(self):
        return sp.compute(self.data.endDate * 60)
    
    @sp.entry_point
    def contribute(self):
        #add on list
        sp.if (self.data.contributors.contains(sp.sender)): 
            #check if it will reach the max amount with other donation
            prvDons = sp.local("prvDons", sp.mutez(0))
            prvDons = self.checkTotal(self.data.contributors[sp.sender])
            self.data.contributors[sp.sender].push(sp.amount) #if already exist
        sp.else:
            self.data.contributors[sp.sender] =  sp.list([sp.amount], t = sp.TMutez) #insert donator address
    
    def checkTotal(self, list_):
        total = sp.local("totale", sp.mutez(0))
        sp.for j in list_:
            with sp.match_cons(list_) as x1:
                total.value += x1.head
                list_ = x1.tail
        return total.value

    @sp.entry_point
    def refund(self):
        #check if sender is a contributor
        sp.verify(self.data.contributors.contains(sp.sender), message = "You are not a contributor")

        #refund
        sp.send(sp.sender, self.checkTotal(self.data.contributors[sp.sender]))



@sp.add_test(name = "Crowdfunding")
def testCrowd():
    #set scenario
    sc = sp.test_scenario()
    #create admin
    admin = sp.test_account("admin")
    #create object crowdfunding
    crowdFunding = CrowdFunding(admin.address , 1)
    #start scenario
    sc += crowdFunding

    #create users
    pippo = sp.test_account("pippo")
    sofia = sp.test_account("sofia")
    sergio = sp.test_account("sergio")

    time = sp.timestamp(0) #calculate execution time
    time = time.add_minutes(2)
    sc.h1("Check Time")
    crowdFunding.checkResult(time).run(sender = admin).run(valid = False)
    sc.h1("Pippo Contribute")
    crowdFunding.contribute().run(sender = pippo, amount = sp.mutez(10))
    sc.h1("Sofia Contribute")
    crowdFunding.contribute().run(sender = sofia, amount = sp.mutez(100))
    sc.h1("Pippo Contribute Again")
    crowdFunding.contribute().run(sender = pippo, amount = sp.mutez(1000000))
    sc.h1("Sergio Contribute")
    crowdFunding.contribute().run(sender = sergio, amount = sp.mutez(1000))
    sc.h1("Attempt to Contribute")
    crowdFunding.contribute().run(sender = sofia, amount = sp.mutez(10000))
    sc.h1("Check Result")
    crowdFunding.checkResult(time).run(sender = admin)
    
