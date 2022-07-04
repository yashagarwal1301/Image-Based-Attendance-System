# import mysql.connector
# import os
import pandas as pd
from time import strftime
from datetime import datetime

# conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3306)
# cursor = conn.cursor()
# stmt = "select * from student"
# cursor.execute(stmt)
# result = cursor.fetchall()
# print('Result: ',*result)



def mark_absent():
    data = pd.read_csv('attendance.csv')
    sheet = pd.read_csv('student_list.csv')
    now=datetime.now()
    a=[]
    d=[]
    t=[]
    print(list(sheet.Student_ID))
    for i in list(sheet.Student_ID):
        i-=1
        print(i)
        d.append(now.strftime("%d/%m/%Y"))
        t.append(now.strftime("%H:%M:%S"))

        if sheet.iloc[i]['USN'] in list(data['USN']):
            a.append('Present')
            # sheet.Status.iloc[i] = 'Present'
        else:
            a.append('Absent')
            # sheet.Status.iloc[i] = 'Absent'
    sheet['Status']=a
    sheet['Date']=d
    sheet['Time']=t
    sheet.to_csv('D:\Final Project\student_list.csv',index=False)

mark_absent()