from hashlib import md5
s=[['10001', 'std1', 'Maths', '100'], ['10002', 'std2', 'Physics', '80'], ['10003', 'std3', 'English', '65'], ['10004', 'std4', 'Social', '95'], ['10005', 'std5', 'Chemistry', '99']]
s=['10005', 'std5', 'Language', '99']
e=[['10001', 'std1', 'Maths', '100'], ['10002', 'std2', 'Physics', '80'], ['10003', 'std3', 'English', '65'], ['10004', 'std4', 'Social', '95']]
s=md5(str.encode(str(s))).hexdigest()
print(s)