class A:
    def show(self):
        print("Show From A")

class B(A):
    def show(self):
        super().show()
        print("Show From B")

class C(A):
    def show(self):
        super().show()
        print("Show From C")

class D(B,C):
    def show(self):
        super().show()
        print("Show From D")
        
c=D()
c.show()
