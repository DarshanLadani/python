import random

l=[]
lucky=[]

#print(random.randint(1000,9999))
#print(random.choice([10,"darshan","ladani",555,999,"Python",0000,"hello"]))
for i in range(1,101):
    l.insert(i,i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
print(l)
print(lucky)
