# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:22:09 2020

@author: Ankita Gogawale
"""


import sqlite3  as sql

DBPath="E:\D\PyCharmWorkspaces\PythonTutorial\sqlDemo\Test.db"

connection=sql.connect(DBPath)

sqlcreateQuery= '''
   CREATE TABLE IF NOT EXISTS EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )

'''

cursor= connection.cursor()
cursor.execute(sqlcreateQuery)
print("Table Creation ")

sqlDropQuery= '''
DROP TABLE EMPLOYEE IF EXISTS
'''
d1=(1708974,'Ankita',22,'F',27000)
sqlInsertQuery= '''
Insert into EMPLOYEE values(?,?,?,?,?)
'''


records = [

    (123456, 'John', 25, 'M', 50000.00),

    (234651, 'Juli', 35, 'F', 75000.00),

    (345121, 'Fred', 48, 'M', 125000.00),

    (562412, 'Rosy', 28, 'F', 52000.00)

    ]



try :
    cursor.execute(sqlInsertQuery,d1)
    print("Single Row Inserted ")
    cursor.executemany(sqlInsertQuery, records)
    print("Multiple ROW INSETED")

    
except Exception as e : 
    print("Exception occrs  :: ",e )
    
    
    
selectQuery='''
 select * from EMPLOYEE
 '''   
 
try : 
    cursor.execute(selectQuery)
    result=cursor.fetchmany(4)
    for i in result: 
        
        print(i)
except Exception as e : 
    print(" Unable to Fetch  Data :: ", str(e))
 
    
connection.close()
print("Connection Closed ")
