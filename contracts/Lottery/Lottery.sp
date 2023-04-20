import smartpy as sp

class Lottery(sp.Contract):
    def __init__(self, owner):
        self.init(
            ticketPrice=sp.mutez(10_000),
            ticketMax=5,
            ticketOwn=sp.map(l = {}, tkey = sp.TNat, tvalue = sp.TAddress),
            owner=owner.address
        )

    @sp.entry_point
    def purchase(self):
        sp.verify(sp.amount >= self.data.ticketPrice, message="AmountTooLow")
        #calculate how many ticket the sender can buy
        numbers = sp.local("numbers", sp.fst(sp.ediv(sp.amount, self.data.ticketPrice).open_some()))
        #calculate ticket left to buy
        ticketLeft = sp.local("ticketLeft", sp.as_nat(self.data.ticketMax - sp.len(self.data.ticketOwn)))
        #texoz more then necessary
        tezExceed = sp.local("tezExceed", sp.snd(sp.ediv(sp.amount, self.data.ticketPrice).open_some()))
        #excess ticket
        exceed = sp.local("exceed", 0)
        sp.if numbers.value >= ticketLeft.value:
            exceed.value = numbers.value - ticketLeft.value
            sp.send(sp.sender,  (sp.mul(self.data.ticketPrice, sp.as_nat(exceed.value)) + tezExceed.value))
        sp.else:
            sp.send(sp.sender, tezExceed.value)

        #buy ticket and update map
        numbers.value = sp.utils.mutez_to_nat(sp.amount) / sp.utils.mutez_to_nat(self.data.ticketPrice)
        mapLen = sp.len(self.data.ticketOwn) #acquisisco lunghezza mappa
        sp.for i in sp.range(0, numbers.value - sp.as_nat(exceed.value), step = 1):
            self.data.ticketOwn[mapLen+1] = sp.sender #inserisco ticket venduto e possessore

    @sp.entry_point
    def checkWinner(self):
        #verify if ticketMax is reached
        sp.verify(sp.len(self.data.ticketOwn) == self.data.ticketMax)
        #select winner
        winner = sp.local("winner", self.data.ticketOwn[1])
        #send prize
        sp.send(winner.value, sp.balance)

#Test
@sp.add_test(name = "Test Lottery")
def testLottery():
    #create scenario
    sc = sp.test_scenario()
    #create admin
    lottery = sp.test_account("lottery")
    #object Lottery
    myLottery = Lottery(lottery)
    #start scenario
    sc.h1("Initial State")
    sc += myLottery
   
    #user
    sofia = sp.test_account("sofia")
    paolo = sp.test_account("paolo")

    #first buy
    sc.h1("First buy")
    myLottery.purchase().run(sender = sofia, amount = sp.mutez(15_000))
    #attempt failed
    sc.h1("Attemp failed")
    myLottery.purchase().run(sender = sofia, amount = sp.mutez(1_000), valid=False, exception="AmountTooLow")
    #second buy
    sc.h1("Second buy")
    myLottery.purchase().run(sender = paolo, amount = sp.mutez(100000))
    #end
    sc.h1("Winner")
    myLottery.checkWinner()
