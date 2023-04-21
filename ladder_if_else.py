sid=int(input("Enter Student ID : "))
sname=input("Enter Student Name : ")

maths=float(input("Enter Student Maths Mark : "))
phy=float(input("Enter Student Physics Mark : "))
che=float(input("Enter Student Chemistry Mark : "))
eng=float(input("Enter Student English Mark : "))
com=float(input("Enter Student English Mark : "))

total=maths+phy+che+eng+com
per=total/5

if total>200 :
    print(" Congratulation You are Pass ")
    print(" Total Marks : ",total)
    print(" Percentage : ",per)

if per>70 :
        print(" Grade : Distinction ")
elif per>60 :
    print(" Grade : First Class ")
elif per>50 :
    print(" Grade : Second Class ")
elif per>40 :
     print("Grade : Passs Class ")

else :
    print(" Sorry You Are Fail ")

    

          
