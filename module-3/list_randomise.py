# How will you randomizes the items of a list in place?

import random
n = [1,2,3,4,5,6]
i = sorted(n, key=lambda x: random.random())
print(i)