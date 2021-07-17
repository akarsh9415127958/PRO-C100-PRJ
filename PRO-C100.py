class ATM(object):
    def __init__(self,atmCardno,pinNumber):
        self.atmCardno=atmCardno
        self.pinNumber=pinNumber

      
    def cashWithdrawl(self):
        print("500 Withdrawled")

    def cashEnquiry(self):
        print("You have $50000")

atm = ATM("123456789","5002")
print(atm.cashWithdrawl())
        


        