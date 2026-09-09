class Account:
    def __init__(self,acc,password):
        self.account = acc
        self.password = password
    
    def __test_private(self):
        print("This is Private Method")
    
    def private_test_working(self):
        self.__test_private()

ac1 = Account(1234,"abc@123")
print(ac1.account)
print(ac1.password)

# If we try to access the Private Method it gives error
# ac1.__test_private()

# we can access private method inside the class
ac1.private_test_working()