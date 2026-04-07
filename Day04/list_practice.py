# fruits = ["Cherry", "Apple", "Pear"]
#
# fruits.append("Banana")
#
# fruits.extend(["Orange", "Mango"])
#
# print(fruits)
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# 1st Option
random_person = random.randint(0,4)
print(friends[random_person])

# 2nd Option
print(random.choice(friends))
