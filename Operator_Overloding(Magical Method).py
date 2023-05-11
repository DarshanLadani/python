class Point:
    #all megic method will start and and with double underscore(__)
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
        
    def __str__(self):
        print("Str Called")
        return"[{0},{1}]".format(self.x,self.y)

    def __add__(self,obj):
        print("add calles")
        a=self.x+obj.x
        b=self.y+obj.y
        return Point(a,b)

    
a=Point(10,20)
print(a)
b=Point(30,40)
print(b)
print("Addition Of 2 Objects : ", a+b)
