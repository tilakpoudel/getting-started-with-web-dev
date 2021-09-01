'''
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets().
Since tuples are indexed, they can have items with the same value:

'''

fruitsList = ['apple','mango','orange'] # use square/big bracket for list
print(type(fruitsList))

fruitsTuple = ('apple','mango','orange', 'mango') # use round/small bracket for tuple, allows duplicate data
print(type(fruitsTuple))

print('------------------------@')
print(fruitsTuple[0])
print(fruitsTuple[2])
print(fruitsTuple[-1]) # last item
print(fruitsTuple[-3]) # access the element from the last

print('------------------------')
print((fruitsList))
fruitsList[0] = 'cherry'
print((fruitsList))

# fruitsTuple[0] = 'cherry' # throws an error since tuple is not changable
# print(type(fruitsTuple))

'''
Create Tuple With One Item
To create a tuple with only one item, 
you have to add a comma after the item, otherwise Python will not recognize it as a tuple
'''
single = ('hari')
singleTuple = ('hari',) # use comma at the end if tuple contains single item
multipleTuple = ('hari', 'shyam', True, 20, 56.9) # tuple can contain any data types

print('------------------------')
print(type(single))
print(type(singleTuple))
print(type(multipleTuple))
print(multipleTuple)

'''
It is also possible to use the tuple() constructor to make a tuple.
'''
print('------------------------')
constructTuple = tuple(('radha', 'shyam', 'hari', 'brinda'))
print(type(constructTuple))
print(constructTuple)

print('------------------------')
print(constructTuple[1:3]) # first index is included and last is excluded
print(constructTuple[1:]) # first index is included and last is excluded
print(constructTuple[:]) # first index is included and last is excluded
print(constructTuple[:3]) # first index is included and last is excluded
