t=(1,10,20,30,40,50,True,"python",6.6,[111,222,333],"darshan",70,80,90,100)

print(t)
print(t.count(1))
print(t.index("darshan"))

for i in t:
    print(i)
print(list(t))
print (100 in t)
print(t[9])
t[9].append(444)
print(t[9])
print(t)
