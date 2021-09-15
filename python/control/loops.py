i = 1
while i < 6:
  print(i+1)
  i+=1

  # 1,3,5,7,9,11

print('-----------------------')
for n in range(1, 30, 3): 
  if n == 19:
    continue
  print(n)
else: 
  print('Iteration completed')

# nested loop
nature = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
print('-----------------------')

for n in nature:
  for f in fruits:
    # print(n, f)
    pass
