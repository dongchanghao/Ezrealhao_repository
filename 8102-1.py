import socket
import sqlite3
sd = socket.socket(family=socket.AF_INET,type = socket.SOCK_STREAM)
sd.bind(('localhost',8800))
sd.listen(5)
while True:
    conn1 = sqlite3.connect('qq.db')
    c = conn1.cursor()
    conn,addr = sd.accept()
    data = conn.recv(1024)
    datas = data.decode('utf-8')
    datas1,pw_r = datas.split('+')
    pw = c.execute('SELECT PASSWORD FROM QQ WHERE ID ={}'.format(datas1))
    for row in pw:
        pw_q = row[0]
    if pw_q =="" or pw_q!=pw_r:
        conn.send("1".encode('utf-8'))
    elif pw_q == pw_r:
        conn.send("0".encode('utf-8'))
    conn.close()
    #conn.send(str(datas).upper().encode('utf-8'))

