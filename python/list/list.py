# List are used to store muliple values in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
#  the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
fruits = ['mango', 'apple', 'pineapple', 'banana', 'mango']
print(type(fruits))
print(fruits)

myList = ['mango', 'hari', 100, 10.5] # values can be of any type
print(type(myList))
print(myList)
print(len(myList))

# List items are ordered, changeable/mutable, and allow duplicate values.

# It is also possible to use the list() constructor when creating a new list.
newList = list(('pen', 'pencil', 'sharpner'))
li = list((1,1,2,3,'hello'))
print(newList)
print(type(newList))

#access list items
fruits = ['mango', 'apple', 'pineapple', 'banana', 'orange']
print(fruits)
print(fruits[0])
print(fruits[4])
print(fruits[0:2])
print(fruits[-1])
print(fruits[-3 : -1])
print(fruits[-3 :])
print(fruits[0 :])
print(fruits[:])

if "apple" in fruits:
    print('yes apple is in the fruit list')
else:
    print('apple is not present')

print('-----------------')

# change the values of the list 
fruits = ['mango', 'apple', 'pineapple', 'banana', 'orange']
print(fruits)
print(len(fruits))


fruits[1] = 'Papaya' #replace itema at index 1 with Papaya
print(fruits)

fruits[2:4] = ['Lemon', 'Litchi'] #[startindex: endindex] where endindex is excluded
print(fruits)
print('-----------------')

fruits[2:4] = ['Lemon1', 'Litchi1', 'guava', 'starfruit']
print(fruits)
print(len(fruits))

fruits[2:4] = ['Lemon2']
print(fruits)
print(len(fruits))

print('........................')

# insert item at the specific position in the list 
fruits.insert(3, "watermelon")
print(fruits)
print(len(fruits))

print('........................')
# add items to the end of the list
fruits.append('cherry')
print(fruits)
print(len(fruits))

print('+++++++++++++++========')

# To append elements from another list to the current list, use the extend() method.
friends = ['ram', 'laxman', 'sita']
newFriends = ['gita', 'shyam', 'hari']

print(friends)

friends.extend(newFriends)

print(newFriends)
print(friends)

# Remove item from list 
# remove by value
print('+++++++++++++++========')
print(friends)
friends.remove('sita') # remove sita from friends list
print(friends)

# remove by index
friends.pop(0) # remove item with index 1 ie ram from friends list
print(friends)
print('+++++++++++++++========')

friends.pop() # remove last item from the list if the  index is not given
print(friends)

print('+++++++++++++++========')

del friends[1] # remove item at index 1 
print(friends)

# clear the list 
friends.clear()
print(friends)


del friends # delete the list
print(friends)


