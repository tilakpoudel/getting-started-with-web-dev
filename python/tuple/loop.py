friends = ('hari', 'shyam', 'rita', 'govinda')
# for in , for in range, while can be used to iterate over the list or tuples

for item in friends:
  print('i am '+ item)

print('=====================')
for index in range(len(friends)):
  print(friends[index])

print('=====================')
i = 0
while i < len(friends):
  print(friends[i])
  i = i + 1