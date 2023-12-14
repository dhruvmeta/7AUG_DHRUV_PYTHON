# Write a Python program to combine values in python list of dictionaries.
from collections import Counter

# output Expected Output: Counter ({'item1': 1150, 'item2': 300})
dic1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = Counter()
for d in dic1:
    result[d['item']] += d['amount']
print(result) 