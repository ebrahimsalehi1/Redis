
import redis

def connect():
    return redis.Redis(host="127.0.0.1",port=6379,db=0)

def setString(mkey,mval):
    redis1 = connect()
    redis1.set(name=mkey,value=mval)


def getString(mkey):
    redis1 = connect()
    return redis1.get(mkey)


redis1 = connect()
#redis1.incr(name="abc")
#redis1.incr(name="abc",amount=10)
#redis1.incr(name="abc",amount=-14)

#redis1.incrby(name="abc")
redis1.incrbyfloat(name="abc",amount=-0.1)
print(redis1.get(name="abc"))


