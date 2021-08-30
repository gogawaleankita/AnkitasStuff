class grandpa(object):
    pass

class father(grandpa):
    pass

class mother(object):
    pass

class child(mother, father):
    pass

print(child.__mro__)