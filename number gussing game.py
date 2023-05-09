import random

a=random.randint(1,20)
count=0
while True:
    count+=1
    try:
        gn=int(input("Guess Number between 1 to 20 : "))
        if gn>a:
            print(" You Guess Heigher Number ")
        elif gn<a:
            print(" Yoy Guess Lower Number ")
        elif gn==a:
            print("\n Congratulations you did it in ",count," attempted")
            break
    except Exception as d:
        print("Exception Caught : ",d)
    finally:
        print("\n")
