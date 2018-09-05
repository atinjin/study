import redis

r = redis.Redis(
    host='localhost',
    port=6379)

r.set('test-key', 'test-value')
value = r.get('test-key')
print(value)