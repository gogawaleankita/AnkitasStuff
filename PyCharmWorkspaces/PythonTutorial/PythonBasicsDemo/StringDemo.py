import os
from collections import *


# Enter your code here.
# namedtuple
from collections import defaultdict


def func1(x, y):
    ankita = namedtuple('player', ['name', 'runs'])
    s = ankita(x, y);
    return s


# deque
def func2(s):
    ankita = list(s);
   # ankita.append(s);
    d = deque();
    d.append(ankita);
    return  d;

    #return ankita;


def func3(x):
    e = Counter(x);

    return e


def func4(m, n, o, p, q):
    s = [m, n, o, p, q];
    d = OrderedDict();
    d[1] = m;
    d[2] = n;
    d[3] = o;
    d[4] = p;
    d[5] = q;
    return d

    return d
def func5(a,b):

    s = defaultdict(list);
    s[0]=a;
    s[1]=b;
    return s;

print(func1("ankita",1000));
print(func2("Ankita"))
print(func3("Ankita"))
print(func4(3,4,5,6,7));
print(func5("preparation","time"));