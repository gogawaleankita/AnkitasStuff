import os
import json

value = '{"data":[{"name":"John", "age":30, "city":"New York"},{"name":"Smith", "age":35, "city":"California"}]}'
def func33(value):
    a= json.loads(value)
    data = a['data']


def func1(value):
    a=json.loads(value)
    b=a
    return b

if __name__ == "__main__":
    try:
        data='[{"1": "Student1", "Marks": 90}, {"2": "Student2", "Marks": 95}]'
        b=func1(data)
        print(True)
        print(b)
        print(b[1].values())
    except ValueError as error:
        print(False)