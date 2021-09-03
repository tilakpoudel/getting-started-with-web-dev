'''
Join Two Sets
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets,
or the update() method that inserts all the items from one set into another:
'''

set1 = {1,2,3}
set2 = {1,2,11,22,33}

set3 = set1.union(set2)
print(set1)
print(set2)
print(set3)

# print('-------------------')
# set1.update(set2)
# print(set1)

print('-------------------')
# Keep ONLY the Duplicates (common)
x = set1.intersection(set2)
print(x)

set1Copy = set1.copy()
print('-------------------')
print(set1Copy)

