fruits = ['mango', 'appple', 'banana', 'orange']

# iterate over the list
# use for loop
for item in fruits:
  print(item)

for i in range(len(fruits)):
  print('fruit at index ' + str(i) +' is '+ fruits[i])
print('...................')

i = 0
while i < len(fruits):
  print('fruit at index ' + str(i) +' is '+ fruits[i])
  i = i + 1

print('...................')
# list comprehension
# List Comprehension offers the shortest syntax for looping through lists:
[print(item) for item in fruits]