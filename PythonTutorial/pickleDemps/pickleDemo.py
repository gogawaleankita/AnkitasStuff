import os
import json
import pickle
import builtins
import io

def funct1(value):
    a = json.loads(value)

    data = json.dumps(a)
    datas=[]
    return data


if __name__ == "__main__":
    try:
        data = '{   "data":[{"name":"John", "age":30, "city":"New York"},{"name":"Smith", "age":35, "city":"California"}]}'
        print(funct1(data[data]))
        print(True)
    except ValueError as error:
        print(False)


class Player:
    def __init__(self,name,runs):
        self.name=name;
        self.runs=runs;


myPlayer=Player("dhoni",10000)

pickle.dump(myPlayer, file =open("../test.pkl", "wb"))

del myPlayer

myPlayer=pickle.load(file=open("../test.pkl", "rb"))

print(myPlayer)

s=['10001', 'std1', 'Maths', '100'], ['10002', 'std2', 'Physics', '80'], ['10003', 'std3', 'English', '65'], ['10004', 'std4', 'Social', '95'], ['10005', 'std5', 'Chemistry', '99']

print(str(s))