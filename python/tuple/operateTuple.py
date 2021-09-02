'''
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable,
 or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple.
'''

fruits = ('mango', 'apple', 'banana', 'orange')
print(type(fruits))
print(fruits)

# print('------------------')
# fruits[0] = 'papaya' # can't update because tuple is immutable/ unchangable
# print(fruits)

'''
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list,
change the list, and convert the list back into a tuple.
'''
# step 1 convert tuple into list
fruitsList = list(fruits) #convert to list / type casting

print('------------------')
print(type(fruits))
print(type(fruitsList))
print(fruitsList)

#step 2: now after converting to list perform operation
fruitsList[0]  = 'papaya'
fruitsList[2]  = 'guava'
fruitsList.append('litchi')
fruitsList.remove('apple')
# perform any operations

# step3 after performing operation convert back to tuple
fruits = tuple(fruitsList)
print('------------------')
print(fruits)

# Unpacking tuples
friends = ('hari', 'shyam', 'rita', 'govinda')
(hari, shyam, rita, govinda) = friends
print('------------------')

print('i am ' + hari)
print('i am ' + shyam)
print('i am ' + rita)
print('i am ' + govinda)
