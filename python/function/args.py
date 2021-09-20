'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''


def favouriteFruit(*fruit):
  print("My favourite fruit " + fruit[1])

favouriteFruit('apple', 'orange', 'banana', 'litchi')

def myFriend( **friend):
  print('My best friend is ' + friend['firstName'] + ' ' +friend['lastName'])

myFriend(firstName = 'Hari', lastName = 'Pandey', age = 20, rollno=10)