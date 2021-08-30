import os
import json
import mpu

# def funct1(value):
#     a=json.loads(value)

#     data=json.dumps(a)
#     return data

# if __name__=="__main__":
#     try:
#         data='{   "data":[{"name":"John", "age":30, "city":"New York"},{"name":"Smith", "age":35, "city":"California"}]}'
#       b=funct1(data)
#         print(True)
#     except ValueError as error:
#         print(False)

pickles = []
for root, dirs, files in os.walk("./"):
    pickles.extend((os.path.join(root, f) for f in files if f.endswith(".pickle")))

pickles = str(pickles)
print(pickles)
unserialized_data = mpu.io.read('test.pickle')
s1 = str(unserialized_data.runs)
s = md5(str.encode(unserialized_data.name)).hexdigest()
s1 = md5(str.encode(s1)).hexdigest()


def test_s():
    assert s == "e783c7044c361cd2f88aefc5caf9b7c5"


def test_s1():
    assert s1 == "b7a782741f667201b54880c925faec4b"