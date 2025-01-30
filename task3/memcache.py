from pymemcache.client import base
import time

client = base.Client(('localhost', 11211))

keys_values = {
    'example1': 'answer1',
    'example2': 'answer2',
    'example3': 'answer3'
}

for key, value in keys_values.items():
    client.set(key, value, expire=5)

time.sleep(6)

for key in keys_values.keys():
    result = client.get(key)
    print(f"{key}: {result}")