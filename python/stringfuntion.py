print('Work on various strings functions')

name = 'yAsHodha'
address = 'butwal'
# to change into upper case ie YASHODHA ; use upper()
UNAME = name.upper()
LNAME = name.lower()
CNAME = address.capitalize()

print('original name is :' + name)
print( name + ' in capital is :' + UNAME)
print( name + ' in lower is :' + LNAME)
print( name + ' in lower is :' + CNAME)

# to remove extra spaces from the string; use strip() function 
# eg :      Hari    => Hari

Message = "    Hari is my best friend. Hari is very kind.  "
print('Original message is : '+ Message)
print('Message after removing beginning and end whitespace is : '+ Message.strip())
print('Count occcurrence of Hari in ' + Message + 'is ' + str(Message.count('Hari')))

# to replace word from string; use strip() function 
print('Message after replacing my friend name is : '+ Message.replace('Hari', 'Shyam'))

# to break word from string into list; use split() function 
myFriends = 'hari, shyam, gita, sita, gopal'
fruits = 'mango orange banana apple,litchi'
print(type(myFriends))
print(myFriends)

myNewFriends = myFriends.split(',')
print(type(myNewFriends))
print(myNewFriends)

myNewFriuts = fruits.split(' ')
print(myNewFriuts)
print(len(myNewFriuts))


# hello my name is "Radha".
print ("hello my name is \"Radha\" .")
print ('hello my name is \'Radha\' .')
# marks obtained is 50/100
print ('Marks Obtained is \t 50/100.')
print ('Marks Obtained is \n 50/100.')


