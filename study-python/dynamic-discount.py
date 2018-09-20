from rediscluster import StrictRedisCluster

startup_nodes = [{"host": "travel-catalog-cache.nquffl.clustercfg.apn2.cache.amazonaws.com", "port": "6379"}]

rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)

i = 0
keys = []
for key in rc.keys("RANK:SP*"):
    i= i+1
    keys.append(key)

print(rc.hgetall(keys.pop()))

print(i)
