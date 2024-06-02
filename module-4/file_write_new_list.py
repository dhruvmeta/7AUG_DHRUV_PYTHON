# Write a Python program to write a list to a file
with open('globalwarming.txt', 'a') as f:
    l= ['global warming', 'climate change', 'renewable energy']
    f.write(f"\n{l}\n")