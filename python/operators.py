# 20 + 30 = 50 
# 20 - 10 = 10
# ARITHEMATIC +, -, *, /, %, **, //
# ASSIGNMENT =, +=, -=, *=, /=, %=, 
# COMPARISION ==, !=, > <, >=, <=
# lOGICAL and, or, not

# Arithmetic operators
print (10+20) #30 additiion
print (11%3) # 2 remainder
print (11/3) # 3.666666 division
print (2*3) # 6 multiply
print (2**3) # 8 exponential (power) 2^3 = 2*2*2
print (11//2) #3 floor division

print('---------------------------------')
# assignment operators
a = 10
print (a) #10

a += 5
print (a) #15 a = a+5

a -= 10
print (a) #5 a = a-10

a *=5
print (a) #25 a = a*5

a /= 5
print (a) #5  a= a/5

a //=2 
print (a) #25  a = a//2  a/2= 2.5 a//2=2

# logical operator and or not returns True or False
print('---------------------------------')
print (0 < 1) # true
print (0 < 1 or 5 > 10) # true
print (0 < 1 and 5 > 10) # false
print (0 < 1 and 5 < 10) # true
print (not 0 < 1) # false

print('---------------------------------')
print('OR truth table ')

formattedResult = "{} or {} = {}"
print(formattedResult.format(0,0, 0 or 0))
print(formattedResult.format(0,1, 0 or 1))
print(formattedResult.format(1,0, 1 or 0))
print(formattedResult.format(1,1, 1 or 1))
