import pymysql

connection=pymysql.connect(user="root",host="127.0.0.1",db="engineer")
print("connection established")


mycursor=connection.cursor()
#que="create table student_detail(name varchar(30), age int(3))"
#mycursor.execute(que)
#print("Table created successfully")

#quesins="insert into student_detail(name,age)values('Ram',25)"
#name=input("enter ur name")
#age=input("enetr ur age")
#quesins="insert into student_detail(name,age)values(%s,%s)"
#val=(name,age)
#mycursor.execute(quesins,val)
#queup="update student_detail set age=101 where name='mohan'"
#mycursor.execute(queup)
#connection.commit()  # when u want to permanenty save data

quesel="select * from student_detail"
data=mycursor.execute(quesel)
print(data)
result=mycursor.fetchall()
print(result)
final_result = [list(i) for i in result]

print(final_result)

print("data inserted successfully")
