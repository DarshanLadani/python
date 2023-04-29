d={1:"darshan",2:"ladani",3:"Tops",4:"java",5:"python",6:"php",7:"html",8:"css",9:"c",10:"C++"}
print(d)
print(d.copy())
print(d.get(5))
print(d.items())
print(d.keys())
print(d.pop(5))
print(d.popitem())
print(d.values())

d1={5:"python",10:"c++"}
d.update(d1)
print(d)


for i in d:
    print (i," : ",d[i])


