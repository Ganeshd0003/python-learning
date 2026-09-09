class Account:
    def __init__(self,acc,password):
        self.account = acc
        self.__password = password
    
    def get_pass(self):
        print(self.__password)
    
ac1 = Account(1234,"abc@123")
print(ac1.account)
# print(ac1.__password) # we cannot access this outside the class it gives error

# But we can access thee privated attribut inside the class
ac1.get_pass()