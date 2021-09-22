'''
Wap to print the largest sum of the items in the lists 
list1= [12, 25, 89, 63, 40]  and list2 = [11, 25, 69, 78, 10]
'''

def calculateListSum (list) :
  sum  = 0
  for item in list: 
    sum = sum + item
  
  return sum

def compareSum (sum1, sum2): 
  if sum1 >= sum2:
    greatest = sum1
  else:
    greatest = sum2

  print('the greatest sum is ' + str(greatest))

def displayMessage (list, sum): 
  print ('The sum of ' + str(list) + ' is ' + str(sum))

list1 = [12, 25, 89, 63, 40, 50, 85]
list2 = [11, 25, 69, 78, 10]

sum1 = calculateListSum(list1)
displayMessage(list1 , sum1)

sum2 = calculateListSum(list2)
displayMessage(list2 , sum2)

compareSum(sum1 , sum2)
