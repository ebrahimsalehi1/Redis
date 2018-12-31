
import redis

def connect():
    return redis.Redis(host="127.0.0.1",port=6379,db=0)

def setString(mkey,mval):
    redis1 = connect()
    redis1.set(name=mkey,value=mval,xx=False)


def getString(mkey):
    redis1 = connect()
    return redis1.get(mkey)


#setString("abc","89")
print(getString("abc"))

#i=0
#while i<100:
#    print(getString("abc"))
#    i=i+1

