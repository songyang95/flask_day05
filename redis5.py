from redis import  StrictRedis
if __name__ == '__main__':
    try:
        #创建链接到redis数据库的对象
        sr = StrictRedis(host="192.168.153.131",port=6379,db=0)
        #字符串新增
        result = sr.set("name","zxc")
        print(result)

        #获取
        name = sr.get("name")
        print(name)
    except Exception as e:
        raise e
