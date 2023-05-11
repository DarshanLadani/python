class A:
    def getA(self,a):
        self.a=a

    def putA(self):
        print("A : ",self.a)
class B(A):
    def getB(self,b):
        self.b=b

    def putB(self):
        print("B : ",self.b)
        
    def sum(self):
        print("Addition : ",self.a+self.b)
        
a=B()
a.getA(int(input("Enter Value A :")))
a.getB(int(input("Enter Value B :")))
a.putA()
a.putB()
a.sum()
