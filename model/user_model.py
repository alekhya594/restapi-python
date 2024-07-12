import mysql.connector
#import json
from flask import make_response
class user_model:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="W7301@jqir#",database="flask_practice")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("connection succssful")
        except:
            print("some error")


    def user_getall_model(self):
        self.cur.execute("SELECT * from users")
        result = self.cur.fetchall()
        if len(result)>0:
            #return json.dumps(result)
            return  make_response({"payload":result},200)
        else:
            return {"message":"no data found"}
        
    def user_addone_model(self,data):
       # self.cur.execute("SELECT * from users")
       self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
    
       
       return  make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    def user_update_model(self,data):
       # self.cur.execute("SELECT * from users")
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}")
        if  self.cur.rowcount>0:
           return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)

    def user_delete_model(self,id):
       # self.cur.execute("SELECT * from users")
        self.cur.execute(f"DELETE from users WHERE id={id}")
        if  self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)


    
    def user_patch_model(self, data, id):
        qry = "UPDATE users SET "
        for key in data:
            
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {'id'}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)  
        