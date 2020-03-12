import pymysql

dbinfo={
    "host":"123.56.131.22",
    "user":"root",
    "password":"123456",
    "port":3319
}
dbinfoyoyo={
    "host":"49.235.92.12",
    "user":"root",
    "password":"123456",
    "port":3309

}

class DbConnect():
    def __init__(self,db_cof,database="hrun"):
        self.db_cof=db_cof
        self.db=pymysql.connect(database=database,cursorclass=pymysql.cursors.DictCursor,**db_cof)
        self.cursor=self.db.cursor()


    def execute(self,sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        self.db.close()

    #查询
    def select(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result

def select_sql(sql):
    db=DbConnect(dbinfoyoyo,database="apps")
    result=db.select(sql)
    db.close()
    return result

def execute_sql(insert_sql):
    db=DbConnect(dbinfoyoyo,database="apps")
    db.execute(insert_sql)
    db.close()


if __name__ == '__main__':
    sql="select * from auth_user where username='test';"
    res=select_sql(sql)
    print(res)






