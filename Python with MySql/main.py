import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.conn = connector.connect(host='localhost',port='3306',user='root',password='73060694moaz@',database='moaztest')
        query = 'create table if not exists user(UserId int primary key,username varchar(200), phone varchar(12))'
        cur = self.conn.cursor()
        cur.execute(query)
        print("Created")
        
    def insert_user(self, userid, username, phone):
        query = "insert into user(UserId, username, phone) values({},'{}','{}')".format(userid, username, phone)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("user saved to db")
        
    def fetch_all(self):
        query = "select * from user"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print('UserId :', row[0])
            print('username :', row[1])
            print('phone :', row[2],)
            print()
            
    def delete_user(self, UserId):
        query = "delete from user where UserId={}".format(UserId)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        # self.conn.commit()    #when we need the data permanently deleted,use commit
        print("deleted")
        
    def update_user(self, userid, newName, newPhone):
        query = "update user set username='{}', phone='{}' where UserId={}".format(newName, newPhone, userid)
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated")

helper = DBHelper()
# helper.insert_user(111, "Moaz", "12345")
# helper.insert_user(112, "Rabbi", "23456")
# helper.insert_user(113, "Makmudul", "34567")
# helper.insert_user(114, "Hasan", "45678")
# helper.delete_user(112)
# helper.fetch_all()
helper.update_user(114, 'Tahmid', '098765')
helper.fetch_all()
