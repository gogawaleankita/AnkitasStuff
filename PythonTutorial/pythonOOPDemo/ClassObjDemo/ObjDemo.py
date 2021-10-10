class Person:
    def __init__(self,name,lname):
        self.fname=name
        self.lname=lname
p1=Person("Ankita","Gogawale")
print(p1.fname, '-', p1.lname)

class A:
    x = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        A.x += 1

    def displayCount(self):
        print('Count : %d' % A.x)

    def display(self):
        print('a :', self.a, ' b :', self.b)

a1 = A('George', 25000)
a2 = A('John', 30000)

a1.display()
a2.display()
print(A.x)