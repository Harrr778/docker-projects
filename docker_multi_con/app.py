import redis
import time

r = redis.Redis(host='redis', port=6379, decode_responses=True)

while True:
    r.incr('counter')
    print(f"Counter: {r.get('counter')}")
    time.sleep(2)
