name = "Gopal" # 0= G, 1=o, 2=p, 3=a, 4=l
message = ' i am from  golok vrindaban.'
message1 = '''helo this is message .....
from vrindaban
 '''

print(type(name))
print(name)

print(type(message))
print(message)
print(message1)

'''
    strings in python are array
'''
print(name[0])
print(name[4])

print('================')

# looping through a string 
for x in name:
    print(x)

# print('================')

# for m in message:
#     print(m)
print('================')

# finding the length of a string
print('the length of ' + message + ' is: '+ str(len(message)))

# check if string is present in the given text
print('================')


print("check if hi is present in "+ message)

print('hi' in message)

print('================')

isPresent = 'am' in message

if (isPresent == True):
    print('am is present in the message')
    print('am is present in the message')
    print('am is present in the message')
else:
    print("am is not present in the message")
    print("am is not present in the message")
    print("am is not present in the message")

    # write a program to find searched word the text and print the result as follow
    #- if the word('namesta') is present then print "Congrats the word you are searching is found"
    # - else "Sorry could not find the word .."

    # write a program to generate a random number and display the result on the basis of following criteria.
    # if the number is divisble by 3 and 5 print "Fizz Buzz"
    # if the number is divisible by 3 print "FiZZ"
    # if the number is divisible by 5 print "BUzz"

#check if the word is not present in given text 
message = ' i am from  golok vrindaban. where are you from?'

isPresent = 'am' not in message

print(isPresent)

