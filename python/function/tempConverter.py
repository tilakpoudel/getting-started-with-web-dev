'''
  This programs converts celcius to and from fraheneit
  c\5 = (f-32 )/9
'''

for i in range(0, 10, 2):
  print(i)

# Parameter vs Argument

def converter (temperature, convertTo): # functions receives parameters
  if convertTo == 'celcius': 
    convertToCelcius(temperature)
  elif convertTo == 'frahreneit':
    convertToFahreneit(temperature)
  else:
    print('Conversion type mismatched ,,,, check once acepted Only---------> celcius or frahreneit')

def convertToCelcius (f):
  c = ((f-32)/9)*5
  print (str(f) + "f = " + str(c) +"celcius")

def convertToFahreneit (c):
  f = ((c/5)*9) + 32
  print (str(c) + "celcius = " + str(f) +"faraheneit")

converter (temperature= 0, convertTo='frahreneit') # arguments are passed while calling funtions
converter (100, 'celcius')

print('----------------------')

# default value in function
def greet(message = 'hi'):
  print(message)

greet('hey')
greet()
greet('how are you ? ')

print('----------------------')

# pass list a argument to the function
def myFriends (friends):
  for i in friends:
    print(i)

myFriends(['ram', 'hari', 'sita', 'gita'])