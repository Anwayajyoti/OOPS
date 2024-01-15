#Single Level
class A:
    a=10
    b=20

class B(A):
    c=30

base=B() 
Parent=A()
print(base.a,base.b,base.c) #Deriving variable a,b from class A
print(Parent.a,Parent.b)

#------------------------------------------------------------------------------------------------------------

#MULTI LEVEL INHERITANCE
class A:
    a=10

class B(A):
    b=20

class C(B):
    c=30

obj=C()
print(obj.c,obj.b,obj.a)

#------------------------------------------------------------------------------------------------------------

#MULTIPLE INHERITANCE [Multiple BASE CLASS Single DERIVE CLASS]
class A:
    def summation(self,a,b):
        print(a+b)
class B:
    def multiplication(self,a,b):
        print(a*b)

class C(A,B):
    def divide(self,a,b):
        print(a/b)

obj=C()
obj.summation(20,30)
obj.multiplication(20,30)
obj.divide(20,30)

#------------------------------------------------------------------------------------------------------------

#HIERARCHILA INHERITANCE[One BASE CLASS Multiple DERIVE CLASS]
class A:
    def parent(self):
        print('M the parent')

class B(A):
    def child1(self):
        print('M child one')

class C(A):
    def child2(self):
        print('M child 2')

obj1=B()
obj2=C()

obj1.parent()
obj1.child1()

obj2.parent()
obj2.child2()
        
#------------------------------------------------------------------------------------------------------------

#HYBRID IHERITANCE:
class A:
    a=10
class B(A):
    b=15
class C:
    c=45
class D(B,C):
    d=90

obj=B()
obj2=D()
print(obj.a,obj.b)
print(obj2.a,obj2.b,obj2.c,obj2.d) #Here we used single level and multiple inheritance
    
    
