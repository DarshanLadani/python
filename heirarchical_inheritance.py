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

class C(A):
    def getC(self,c):
        self.c=c

    def putC(self):
        print("C : ",self.c)
class D(A):
    def getD(self,d):
        self.d=d

    def putD(self):
        print("D : ",self.d)
     
        
c=C()
b=B()
d=D()
d.getA(int(input("Enter Value A :")))
b.getB(int(input("Enter Value B :")))
c.getC(int(input("Enter Value C :")))
d.getD(int(input("Enter Value D :")))
d.putA()
b.putB()
c.putC()
d.putD()

