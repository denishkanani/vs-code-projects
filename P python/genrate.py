# import random

# coin = random.choice(["heads", "tails"])

# print(coin)

# import random

# number = random.randint(1, 10)
# print(number)

import random

cards = ["king", "queen", "jack"]
random.shuffle(cards)
for i in cards:
    print(i)