fruits = ['mango', 'appple', 'banana', 'orange']

# sorting 
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
fruits.sort()
print(fruits)
print('........................')

# descending order sorting
fruits.sort(reverse=True)
print(fruits)

print('........................')
marks = [56, 85, 79, 60, 49]
marks.sort()
print(marks)

print('........................ descending')

for i in range(len(marks)-1, -1):
  print(marks[i])

print('........................')
marks.sort(reverse=True)
print(marks)

# reverse the list 
print('........................')
print(marks)
marks.reverse()
print(marks)

print('........................')
fruits = ['Mango', 'appple', 'Banana', 'orange']
fruits.sort()
print(fruits)

print('........................')
# copy the list 
newFruits = fruits.copy()
print(newFruits)
