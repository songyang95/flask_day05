from rediscluster import *
if __name__ == '__main__':
    try:
        #构建所有节点，redis会使用crc16算法将，键和值写到某个节点上
        startup_nodes=[
            {'host':'192.168.103.132','port':'7000'},
            {'host':'192.168.103.132','port':'7001'},
            {'host':'192.168.103.132','port':'7002'},
        ]
        #构建StrictRedisCluester对象
        src = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)
        result = src.set('name','itheima')
        print(result)
        #获取键为name
        name = src.get('name')
        print(name)
    except Exception as e:
        print(e)