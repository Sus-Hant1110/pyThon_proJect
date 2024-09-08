from main import*

A=BankAccount(20000,"A")
B=BankAccount(30000,"B")

# A.getBalance()
# B.getBalance() 

# A.deposite(5000)
# B.deposite(6000)

# A.withdraw(4000)
# B.transfer(2000000,A)

C=InterestAccount(40000,"C")
C.getBalance()
C.deposite(5000)
C.transfer(1000,B)

D=SavingAccount(50000,"D")
D.getBalance()
D.deposite(5000)
D.withdraw(1000) 
D.transfer(10000,C)