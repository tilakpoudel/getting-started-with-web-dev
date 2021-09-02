# Join Two Tuples
# To join two or more tuples you can use the + operator:

numbers = (10,52,69,70)
alphabet = ('a', 'k', 'i', 'l')

num_alpha = numbers + alphabet

print(numbers)
print(alphabet)
print(num_alpha)

print('====================')
friends = ('hari', 'shyam', 'rita', 'govinda')
newfriends = friends * 3
print(friends)
print(newfriends)

print('====================')
# print('Hari has occuerred ' + str(newfriends.count('hari')) + ' times')
print('govinda has occuerred ' + str(newfriends.count('govinda')) + ' times and is located at index ' + str(newfriends.index('govinda')))