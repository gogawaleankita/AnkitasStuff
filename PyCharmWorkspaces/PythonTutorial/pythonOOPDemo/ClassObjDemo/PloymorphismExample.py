class A:
    def __init__(self, a = 5):
        # print("a of A ",a)
        self.a = a
        # print("a of A  s", self.a)
        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b
        print("b ",self.b)
    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)


class A:
    def __init__(self, x=5, y=4):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A(x: {}, y: {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y


def f1():
    a = A(12, 3)
    b = A(3, 12)
    if (a == b):
        print(b != a)
        print(a)


f1()