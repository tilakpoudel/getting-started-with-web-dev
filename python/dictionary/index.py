'''
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:


'''
student  = {
  'name': 'Hari',
  'grade': '10',
  'section': 'A',
  'address': 'butwal'
}

print(type(student))
print(student)

formatMessage = "My name is {0} from {1}. I study in grade {2} section {3}"
print(formatMessage.format(student['name'], student['address'], student['grade'], student['section']))