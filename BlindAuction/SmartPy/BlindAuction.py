import smartpy as sp


class Auction(sp.Contract):
    def __init__ (self):
        self.init(bidders = sp.map(l = {}, tkey = sp.TAddress, tvalue = sp.TMutez), top = sp.record(winning = sp.list(l = [], t = sp.TAddress), amount = sp.mutez(0)), minBid = sp.mutez(0))

    
    @sp.entry_point
    def bid(self):
        #add to bidders
        self.data.bidders[sp.sender] = sp.amount

        #check if is top bid
        sp.if sp.amount >= self.data.top.amount:
            sp.if sp.amount > self.data.top.amount:
                self.data.top = sp.record(winning = [sp.sender], amount = sp.amount)
            sp.else:
                newList = sp.cons(sp.sender, self.data.top.winning)
                self.data.top = sp.record(winning = newList, amount = sp.amount)
        
    @sp.entry_point
    def getWinner(self):
        #check how many winners
        listTemp = sp.local("listTemp", self.data.top.winning)
        #remove temporarily winners from map
        sp.for i in listTemp.value:
            with sp.match_cons(listTemp.value) as x1:
                adTemp = x1.head
                listTemp.value = x1.tail
                #delete winner from map
                del self.data.bidders[adTemp]
        
        #rimborso 
        addressList = sp.local("addressList", self.data.bidders.keys())
        sp.for i in addressList.value:
            with sp.match_cons(addressList.value) as x1:
                address = x1.head
                addressList.value = x1.tail
                sp.send(address, self.data.bidders[address])
                del self.data.bidders[address]
                
        #re-list
        listTemp.value = self.data.top.winning
        sp.for j in listTemp.value:
            with sp.match_cons(listTemp.value) as x1:
                address = x1.head
                listTemp.value = x1.tail
                self.data.bidders[address] = self.data.top.amount

        #case: more then 1 winners
        sp.if sp.len(self.data.bidders) > 1:
            self.data.minBid = self.data.top.amount
            self.data.top = sp.record(winning = [], amount = sp.mutez(0))
            adList = sp.local("adList",self.data.bidders.keys())
            sp.for k in adList.value:
                with sp.match_cons(adList.value) as x1:
                    address = x1.head
                    adList.value = x1.tail
                    sp.send(address, self.data.minBid)


@sp.add_test(name = "auctionTest")
def auctionTest():
    #set scenario
    sc = sp.test_scenario()
    #new object Auction
    auction = Auction()
    #start scenario
    sc += auction

    #users
    sofia = sp.test_account("sofia")
    piero = sp.test_account("piero")
    carla = sp.test_account("carla")

    #first bid
    sc.h1("First Bid")
    auction.bid().run(sender = sofia, amount = sp.mutez(100))
    #second bid
    sc.h1("Second Bid")
    auction.bid().run(sender = piero, amount = sp.mutez(10))
    #third bid
    sc.h1("Third Bid")
    auction.bid().run(sender = carla, amount = sp.mutez(100))
    #ending
    sc.h1("ending")
    auction.getWinner()
    
