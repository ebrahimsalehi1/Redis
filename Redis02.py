
import redis
import pymysql as mysql


def connect():
    return redis.Redis(host="127.0.0.1",port=6379,db=0)

def setString(mkey,mval):
    redis1 = connect()
    redis1.set(name=mkey,value=mval)


def getString(mkey):
    redis1 = connect()
    return redis1.get(mkey)

def getDataFromMySQLTransToRedis():
    conn =mysql.connect("127.0.0.1","user_ebi","1234","db_ebi")
    cur1 = conn.cursor()
    cur1.execute("SELECT * FROM employees")
    print("start")
    mkey = None
    mval = None
    for row in cur1.fetchall():
        mkey = "employees"+":"+str(row[0])+":"+"first_name"
        mval = row[1]
        setString(mkey,mval)

        mkey = "employees"+":"+str(row[0])+":"+"last_name"
        mval = row[2]
        setString(mkey,mval)

        mkey = "employees"+":"+str(row[0])+":"+"salary"
        mval = str(row[7])
        setString(mkey,mval)


    print("end")

def deleteKeys(keyPattern):
    redis1 = connect()
    for key in redis1.keys(keyPattern):
        redis1.delete(key)
        #print(key)

#getDataFromMySQLTransToRedis()
deleteKeys("employees*")
