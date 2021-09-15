'''
Write a Python script to sort (ascending and descending) a dictionary by value.
'''
import operator
number = {10: 20, 2: 3, 3: 40, 0: 48} # 0:48, 1
 
asc_sorted_data = dict(sorted(number.items(), key = operator.itemgetter(1)))
dsc_sorted_data = dict(sorted(number.items(), key = operator.itemgetter(1), reverse=True))
print(number)
print('ascending orer by value ')
print(asc_sorted_data)
print('descending orer by value ')

print(dsc_sorted_data)
