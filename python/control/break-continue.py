'''
With the break statement we can stop the loop even if the while condition is true:
'''
i = 1
while i < 10:
  if i == 3:
    break
  print(i)
  i+=1

'''
With the continue statement we can stop the current iteration, and continue with the next:
'''
# print('----------------')
# j= 1
# while j< 6:
#   j+=1
#   if j== 3:
#     continue
#   print(j)

print('----------------')
j = 10
for i in range(10):
  if i == 3:
    continue
  print(i)
  print('hello')
  print('hi')