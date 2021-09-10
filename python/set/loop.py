fruitsSet = {'apple', 'banana', 'orange0', 'pineapple'}
fruitsList = ['apple', 'banana', 'orange0', 'pineapple']
fruitsTuple = ('apple', 'banana', 'orange0', 'pineapple')

#looping / iteration in set
print('items in set')
for item in fruitsSet: 
  print(item)
print('--------------------')
print('items in list')
print('--------------------')


for item in fruitsList: 
  print(item)

print('--------------------')
print('items in tuple')
print('--------------------')


for item in fruitsTuple:
  print(item)

print('--------------------')
#append data in list . append adds data to the last index 
fruitsList.append("litchi")
print(fruitsList)

#add data in list . insert adds data to the specified index 
fruitsList[0] = 'guava'
fruitsList.insert(0, 'lemon')
print(fruitsList)
