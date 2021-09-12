student = {
  "name": "Shyam",
  "address": "Mathura",
  "age": 10,
  "status": False,
  "interest": ["singing", "dancing", "travelling"]
}

# print all key
for key in student:
  # print('keys are...................')
  # print(key)

  # print('values are...................')
  # print(student[key])

  print(key + " = " + str(student[key]))

print('...................')
#loop through key and values
for key, value in student.items():
  print(key, value)