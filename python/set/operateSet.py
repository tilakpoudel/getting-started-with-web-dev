'''
  Add item in a set
  Once a set is created, you cannot change its items, but you can add new items.

  Add an item to a set, using the add() method:
'''

fruits = {'apple', 'orange'}
fruits.add('banana')
fruits.add('litchi')
print(fruits)

'''
To add items from another set into the current set, use the update() method.
'''

print('---------------')
localfruits = {'guava', 'pineapple', 'apple', 'orange'}
fruits.update(localfruits)
print(fruits)

print('---------------')
fruitsList = ['papaya']
fruits.update(fruitsList)
print(fruits)

'''
To remove an item in a set, use the remove(), or the discard() method.
'''
fruits.remove('apple')
print('---------------')
print(fruits)

fruits.discard('banana')
print('---------------')
print(fruits)

'''
You can also use the pop() method to remove an item, 
but this method will remove the last item. Remember that sets are unordered, 
so you will not know what item that gets removed.
'''

print('---------------')
removed = fruits.pop()
print(removed)
print(fruits)

fruits.clear() # empties the fruits set
print(fruits)
print(len(fruits))

del fruits # removes the entire variable
print(fruits)


