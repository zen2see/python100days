from gamedata import data 
import random

random_topic1 = random.choice(data)
print(random_topic1)
"""
print(data[2]['follower_count'])
print(data[3]['follower_count'])
if data[2]['follower_count'] > data[3]['follower_count']:
    print(True)
else:
    print(False)
"""
