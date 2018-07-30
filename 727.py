import sqlite3

conn = sqlite3.connect('student.db')

# print ("Opened database successfully")
# c = conn.cursor()
# c.execute('''CREATE TABLE STUDENT
#       (ID INT PRIMARY KEY     NOT NULL,
#       STU_NAME           CHAR(20),
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50));''')

# print ("Table created successfully")
# conn.commit()
# conn.close()

c = conn.cursor()
# print("Opened database successfully")
# c.execute("INSERT INTO STUDENT(ID,STU_NAME,AGE,ADDRESS)\
#           VALUES(20154071115,'dch',22,'1-223') ");
# c.execute("INSERT INTO STUDENT(ID,STU_NAME,AGE,ADDRESS)\
#           VALUES(20154071112,'fwx',22,'1-222') ");
# c.execute("INSERT INTO STUDENT(ID,STU_NAME,AGE,ADDRESS)\
#           VALUES(20154071111,'cg',22,'1-223') ");
# c.execute("INSERT INTO STUDENT(ID,STU_NAME,AGE,ADDRESS)\
#           VALUES(20154071110,'wyf',22,'1-222') ");
# conn.commit()
# print("Records created successfully")
# conn.close()
# cursor = c.execute("SELECT id,name,address FROM student")
# for row in cursor:
#     print("ID = ",row[0])
#     print("NAME = ",row[1])
#     print("ADDRESS = ",row[2])
# print("Operation done successfully")
# conn.close()
def display_menu():
    print("学生表操作界面")
    print("---------------------")
    print("1.增添学生信息")
    print("2.查询学生有关资料")
    print("3.修改学生有关信息")
    print("4.删除学生信息")
    print("5.查询现在的学生信息")
    print("0.退出")
    print("---------------------")
def append_data():
    while True:
        id = int(input("请输入新学生的学号："))
        name = input("请输入新学生的名字")
        age = int(input("请输入新学生的年龄"))
        address = input("请输入新学生的地址")
        sqlStr = "select * from student where id = {};".format(id)
        cursor = conn.execute(sqlStr)
        if len(cursor.fetchall())>0:
            print("列表中已经有这个学生了")
        else:
            sqlStr = "insert into student(ID,STU_NAME,AGE,ADDRESS) VALUES ({},{},{},{})".format(id,name,age,address)
            conn.execute(sqlStr)
            conn.commit()
def update_date():
    id = int(input("请输入你要修改的学号："))
    sqlStr = "select * from student where id = {};".format(id)
    cursor = conn.execute(sqlStr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("该学生的姓名是",rows[0][1])
        name = input("请输入学生的新名字")
        age = int(input("请输入学生的新年龄"))
        address = input("请输入学生的新地址")
        sqlStr = "update student set STU_NAME = '{}',age = '{}',address = '{}' where id = {}".format(name,age,address,id)
        conn.execute(sqlStr)
        conn.commit()
        print("修改成功")
    else:
        print("不存在该学生")
def delete_data():
    id = int(input("请输入要删除的学生id："))
    sqlStr = "select * from student where id = {};".format(id)
    cursor = conn.execute(sqlStr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("该学生的姓名是",rows[0][1])
        s = int(input("请确认删除(如果删除请输入'1',不删除请输入'0'):"))
        if s == 1:
            sqlStr = "delete from student where id = {}".format(id)
            conn.execute(sqlStr)
            print("删除成功")
        else:
            return display_menu()
def select_data():
    id = int(input("请输入要修改的学生id："))
    sqlStr = "select * from student where id = {};".format(id)
    cursor = conn.execute(sqlStr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("该学生信息如下：")
        print(rows)
    else:
        print("该学生不存在")

def display_data():
    cursor = conn.execute('SELECT * FROM student;')
    for row in cursor:
        print(row)
while True:
    display_menu()
    choice = int(input("请输入你的选择"))
    if choice == 0:
        conn.close()
        break
    elif choice == 2:
        select_data()
    elif choice == 3:
        update_date()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        display_data()
    elif choice == 1:
        append_data()
    else:break
