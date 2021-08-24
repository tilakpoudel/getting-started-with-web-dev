name = 'Sita'
address = 'Janakpur'
nature = 'Kind'

print('Hello i am '+ name + ' from ' + address + '. I am very ' + nature) 

messageFormat = '  I am very {} , Hello i am {} from {} .'
messageFormat = '  I am very {2} , Hello i am {0} from {1} .'
print(messageFormat.format(name, address, nature))