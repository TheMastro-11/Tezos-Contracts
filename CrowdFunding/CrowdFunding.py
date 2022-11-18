import smartpy as sp

class CrowdFunding(sp.Contract):
    def __init__(self, deadline):
        self.init(startDate = sp.timestamp(0), endDate = 1, contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TList(sp.TMutez) ), minAmount = sp.mutez(10), maxAmount = sp.mutez(1000), ceiling = sp.mutez(100000), floor = sp.mutez(200), isSuccess = sp.bool(False)  )

    @sp.entry_point
    def checkTime(self, time):
        diffTime = time - self.data.startDate
        sp.verify(diffTime <= self.getSeconds(), message = "The time is over")

    def getSeconds(self):
        return sp.compute(self.data.endDate * 86400)
    
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
            self.data.contributors[sp.sender] =  sp.list([sp.amount], t = sp.TMutez) #inserisco indirizzo contribuente
    
    
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
    
    def checkTotal(self, list_):
        total = sp.local("totale", sp.mutez(0))
        sp.for j in list_:
            with sp.match_cons(list_) as x1:
                total.value += x1.head
                list_ = x1.tail
        return total.value


    @sp.entry_point
    def endFunding(self, cAddress):
        #airdrop new token
        c = sp.contract(sp.TMap(sp.TAddress, sp.TList(sp.TMutez)), cAddress, entry_point = "airdrop").open_some()
        sp.transfer(self.data.contributors, sp.balance, c)

class TokenGen(sp.Contract):
    def __init__(self):
        self.init(supply = 120000000, contributors = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TNat))

    
    @sp.entry_point
    def airdrop(self, adMap):
        adList = sp.local("adList", adMap.keys())
        sp.for i in adList.value:
            with sp.match_cons(adList.value) as x1:
                address = x1.head
                adList.value = x1.tail
                self.data.contributors[address] = sp.utils.mutez_to_nat(self.checkTotal(adMap[address])) * 1200

    def checkTotal(self, list_):
        total = sp.local("totale", sp.mutez(0))
        sp.for j in list_:
            with sp.match_cons(list_) as x1:
                total.value += x1.head
                list_ = x1.tail
        return total.value

@sp.add_test(name = "Crowdfunding")
def testCrowd():
    #set scenario
    sc = sp.test_scenario()
    #create object crowdfunding
    crowdFunding = CrowdFunding(14)
    #create object tokenGen
    tokenGen = TokenGen()
    #start scenario
    sc += crowdFunding
    sc += tokenGen

    #create users
    pippo = sp.test_account("pippo")
    sofia = sp.test_account("sofia")
    sergio = sp.test_account("sergio")

    time = sp.timestamp(0) #calculate execution time
    time = time.add_hours(1)
    sc.h1("Check Time")
    crowdFunding.checkTime(time)
    sc.h1("Pippo Contribute")
    crowdFunding.contribute().run(sender = pippo, amount = sp.mutez(10))
    sc.h1("Sofia Contribute")
    crowdFunding.contribute().run(sender = sofia, amount = sp.mutez(100))
    sc.h1("Pippo Contribute Again")
    crowdFunding.contribute().run(sender = pippo, amount = sp.mutez(100))
    sc.h1("Sergio Contribute")
    crowdFunding.contribute().run(sender = sergio, amount = sp.mutez(1000))
    sc.h1("Attempt to Contribute")
    crowdFunding.contribute().run(sender = sofia, amount = sp.mutez(10000)).run(valid = False)
    sc.h1("check floor")
    crowdFunding.checkFloor()
    sc.h1("End Funding")
    crowdFunding.endFunding(tokenGen.address)
