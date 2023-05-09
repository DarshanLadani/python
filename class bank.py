import random

class Bank:
    def openaccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("\nHello",self.cname,"Your Account Number is ",self.acno,"is Oppened with Balance ",self.balance)
   
    def depo(self,amount):
        self.balance+=amount
    def wdrw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("\ninsfficient balance")
    def chechbal(self):
        print("\ncurrent Balance : ",self.balance)

    

b=Bank()
no=int(input("\nEnter Account Number : "))
name=input("\nEnter Name : ")
b.openaccount(no,name,1000)

while True:
   
    try:
        print("\n\tWelcom Tops Bank\n\n")
        print("1) Deposite \n")
        print("2) Withdraw \n")
        print("3) Check Balance \n")
        print("4) Exit \n")

        ch=int(input("\nSelect Which Opration you want to do : "))
        if ch==1:
            da=int(input("\nEnter Deposit Ammount Number : "))
            b.depo(da)
            b.chechbal()
        elif ch==2:
            wa=int(input("\nEnter Withdraw Ammount Number : "))
            b.wdrw(wa)
            b.chechbal()
        elif ch==3 :
            b.chechbal()
        elif ch==4:
            print("\nThank You")
            break
        else:
            print("\n!!!! Enter Valid Input !!!!\n")
    except Exception as a:
        print("\nException Caugth : ",a)
    finally:
        print("\n")
