import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
randFriend = random.randint(0, len(friends))
# randFriend = random.choice(friends)
print("The random name from the list of friends is: ", friends[round(randFriend)])
