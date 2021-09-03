'''
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.
Set items are unordered, unchangeable, and do not allow duplicate values.

Sets are written with curly brackets{}.
'''

fruits = {'apple', 'banana', 'cherry'}
print(type(fruits))
print(fruits)

# set doesnot allow duplicate values
fruits = {'apple', 'banana', 'cherry', 'apple'}
print(type(fruits))
print(fruits)
print(len(fruits))

sets = {10, 'ten', 10.5}
print(sets)

print('------------------')
setConstructor = set(('ram', 'hari', 'shyam'))
print(setConstructor)


print('------------------')
# accesss the items in the set
for item in setConstructor:
  print(item)

print('------------------')
# check if item is in set
print('ram1' in setConstructor)