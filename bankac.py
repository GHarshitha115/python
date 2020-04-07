class user:
    def __init__(self,name,mobile_no,address=""):
        self.name=name
        self.mobile_no=mobile_no
        #self.generate_account_no()
        self.address=address
class BankAccount:
    def __init__(self,user_details):
        self.account_holder=user_details
        self.generate_account_no()
        self.bal=0
    
    def generate_account_no(self):
        import uuid
        self.account_no=str(uuid.uuid4())
    def deposit(self,amount):
        self.bal+=amount
    def withdraw(self,amount):
        '''if amount>self.bal:
            print("Invalid bal")
        else:'''
        self.bal-=amount
'''b=BankAccount("Harshi","7995295719")
print(b.name)
print(b.mobile_no)
#b.generate_account_no()
print(b.account_no)
print(b.bal)
b.deposit(100)
b.deposit(100)
print(b.bal)
b.withdraw(500)'''


u=user("fghj","5678","sdfghj")
print(u.name)

b=BankAccount(u)
print(b.account_holder.name)
print(b.account_holder.mobile_no)
print(b.account_no)
print(b.bal)

