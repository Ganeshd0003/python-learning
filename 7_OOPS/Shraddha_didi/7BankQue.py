class Bank:
    bank_name = "HDFC"

    def __init__(self, user):
        self.user = user
        self.total = 0

    def Credit(self, amount):
        self.total += amount
        print(f"\n{self.bank_name} Banking Service")
        print(f"₹{amount} was credited.")

    def Debit(self, amount):
        print(f"\n{self.bank_name} Banking Service")
        if self.total >= amount:
            self.total -= amount
            print(f"{self.user} withdrew ₹{amount}.")
            print(f"Remaining Balance: ₹{self.total}")
        else:
            print("Insufficient Funds!")

    def Balance(self):
        print(f"\nCurrent Balance: ₹{self.total}")


c1 = Bank("Ganesh")
c1.Credit(10000)
c1.Debit(10)
c1.Balance()