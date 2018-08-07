from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import socket
def sql_create():
    conn = sqlite3.connect('qq.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE QQ
              (ID CHAR(20) PRIMARY KEY NOT NULL ,
              PASSWORD CHAR(20) NOT NULL);''')
    conn.commit()
    conn.close()
def add_data():
    conn = sqlite3.connect('qq.db')
    c = conn.cursor()
    #c.execute("INSERT INTO QQ(ID,PASSWORD) VALUES ('111','1')");
    #c.execute("INSERT INTO QQ(ID,PASSWORD) VALUES ('222','2')");
    cursor = c.execute("SELECT * FROM QQ")
    for row in cursor:
        print("ID=",row[0])
        print("Password=",row[1])
    conn.commit()
    conn.close()
def istrue():
    s = socket.socket()
    s.connect(('localhost',8800))
    li=answerEntry1.get()+"+"+answerEntry2.get()
    s.send(li.encode('utf-8'))
    ret = int(s.recv(1024).decode('utf-8'))
    #print(ret)
    #print(type(ret))
    if ret == 0:
        return second()
    else:
        print('用户密码不正确')
    s.close()
def second():
    print('yes')
    root.destroy()
    root2 = Tk()
#sql_create()
#add_data()
root = Tk()
var1 = IntVar()
var2 = IntVar()
root.title('qq')
img = Image.open('1.gif')  # 打开图片
img2 = Image.open('2.gif')  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
photo2 = ImageTk.PhotoImage(img2)  # 用PIL模块的PhotoImage打开
imglabel = Label(root, image=photo)
imglabe2 = Label(root, image=photo2)
imglabel.grid(row=0, column=0, columnspan=3)
imglabe2.grid(row=1, column=0,rowspan = 2)

#Label(root, text="Password:").grid(row=2, column=0, sticky=S + N)
#Label(root, text="Id:").grid(row=1, column=0, sticky=S + N)

answerEntry1 = Entry(root)
answerEntry2 = Entry(root,show = '*')
btn1 = Button(root, text="logo",command = istrue)
btn2 = Button(root, text="find password")
checkButton1 = Checkbutton(root,text='记住密码',variable = var1)
checkButton2 = Checkbutton(root,text='自动登录',variable = var2)
answerEntry1.grid(row=1, column=1)
answerEntry2.grid(row=2, column=1)
btn1.grid(row=1, column=2)
btn2.grid(row=2, column=2)
checkButton1.grid(row = 3,column =1)
checkButton2.grid(row = 3,column =2)
mainloop()