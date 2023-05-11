class A:
    def getA(self,a):
        self.a=a

    def putA(self):
        print("A : ",self.a)
class B:
    def getB(self,b):
        self.b=b

    def putB(self):
        print("B : ",self.b)

class C(A,B):
    def getC(self,c):
        self.c=c

    def putC(self):
        print("B : ",self.c)

        
    def sum(self):
        print("Addition : ",self.a+self.b+self.c)
        
a=C()
a.getA(int(input("Enter Value A :")))
a.getB(int(input("Enter Value B :")))
a.getC(int(input("Enter Value C :")))
a.putA()
a.putB()
a.putC()
a.sum()
