'''
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets().
Since tuples are indexed, they can have items with the same value:

'''

fruitsList = ['apple','mango','orange']
print(type(fruitsList))

fruitsTuple = ('apple','mango','orange', 'mango')
print(type(fruitsTuple))

print('------------------------')
print(fruitsTuple[0])
print(fruitsTuple[-1])

print('------------------------')
print((fruitsList))
fruitsList[0] = 'cherry'
print((fruitsList))

# fruitsTuple[0] = 'cherry' # throws an error since tuple is not changable
# print(type(fruitsTuple))

