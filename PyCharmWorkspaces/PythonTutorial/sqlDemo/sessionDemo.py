from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "sqlite:///tests.db"

db = create_engine(db_string)
base = declarative_base()

class Teacher(base):

  __tablename__ = 'students'
  stdid = Column(String,primary_key=True)
  stdname = Column(String)
  subjects = Column(String)
  marks = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

#Create
s1=Teacher(stdid='10001',stdname= 'std1', subjects='Maths',marks= '100'),
s2=Teacher(stdid='10002',stdname= 'std2', subjects='Physics',marks= '80')
s3=Teacher(stdid='10003',stdname= 'std3', subjects='English',marks= '65')
s4=Teacher(stdid='10004',stdname= 'std4', subjects='Social',marks= '95')
s5=Teacher(stdid='10005',stdname= 'std5', subjects='Chemistry',marks= '99')

# session.add(s1)
# session.add(s2)
# session.add(s3)
# session.add(s4)
# session.add(s5)

session.add_all([s1,s3,s3,s4,s5])
session.commit()


#Read
s=[]
result_set = session.query(Teacher).all()
print(result_set)
for i in result_set:
  s.append(i)

# s=[['10001', 'std1', 'Maths', '100'], ['10002', 'std2', 'Physics', '80'], ['10003', 'std3', 'English', '65'], ['10004', 'std4', 'Social', '95'], ['10005', 'std5', 'Chemistry', '99']]
#Update
print(s)
s5.subjects="Language"
session.commit()
q=[]
result_set = session.query(Teacher).all()
for i in result_set:
  q.append(i)



#Delete

session.delete(s5)
session.commit()

e=[]
result_set = session.query(Teacher).all()
for i in result_set:
  e.append(i)




s=str(s)
q=str(q)
e=str(e)
with open(".hidden.txt",'w') as f:
	f.write(s)

with open(".hidden1.txt",'w') as f:
	f.write(q)

with open(".hidden2.txt",'w') as outfile:
	outfile.write(e)
