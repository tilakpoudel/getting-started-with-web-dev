student = {
  "key": "value",
  "name": "Shyam",
  "address": "Mathura",
  "age": 10,
  "status": False,
  "interest": ["singing", "dancing", "travelling"]
}
print(student)

print('-------------')
print(student["name"])
print(student["address"])
print(student["age"])
print(student["status"])
print(student["interest"])
print(student["interest"][0])

print('-------------')
print(student.get("name"))
print(student.get("interest")[1])

# access the keys in the dictionary using key() methods
print('-------------')
keys = student.keys()
print(keys)

# access the values in the dictionary using values() methods
print('-------------')
values = student.values()
print(values)

# access the items in the dictionary using items() methods
print('-------------')
items = student.items()

print('before changes')
print(items)

student["name"] = "Hari"

print('after changes')
print(items)


# check if key is present 
if 'rollno' in student:
  print('yes roll number is present')
else:
  print('sorry rollnumber is not present')

# change/update values of the dictionary
student['age'] = 15
print('-------------')
print(student)

student.update({"status": True})
print('-------------')
print(student)

# add items in dictionary
student["rollno"] = 10
print('-------------')
print(student)

student.update({"gender": "Male"})
print('-------------')
print(student)

# Remove item with key from dictionay
student.pop('status')
print('-------------')
print(student)

# remove last item from dictionary
student.popitem()
print('-------------')
print(student)

# delete item with key from dictionary
del student['age']
print('-------------')
print(student)

# clear dictionary
student.clear()
print('-------------')
print(student)

# delete dictionary
# del student
# print('-------------')
# print(student)