# def russianDoll(doll):                             # in this reverse values will get printed because of recursion as print statement will get executed after
#     if doll == 1 :                                 # all the recursio calls, as we have studied in stack memory.
#         print('all dolls are opened')              
#     else:
#         russianDoll(doll-1)
#         print(doll)

# russianDoll(5)



# FACTORIAL

# import sys 

# sys.setrecursionlimit(10000)      # for increasing recursion call limits


# def factorial(n):
#     assert n>=1 and int(n) == n,'The number input must be positive value only greater than 1.'

#     if n == 1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)


# print(factorial(3))



# # FIBONACCI 

# def fibonacci(n) :
#     assert n>=0  and int(n)==n,' The number must be positive integer only'

#     if n ==1 or n==0 :
#         return n

#     else :
#         return fibonacci(n-1) + fibonacci(n-2)
    

# print(fibonacci(3))


# sum of digits

# def sum(n):
#     if n<10 :
#         return n
#     else :
#         return n%10 + sum(n//10)

# print(sum(61))




#POWER OF NUMBER

# def number(base, power):
#     assert power >=0 and int(base) == base and int(power) == power, 'exponent should be positive integer only'
#     if power == 1:
#         return base
#     elif power == 0:
#         return 1
#     else:
#         return base*((base)**(power-1))


# print(number(-3.78,3.676))




#GCD of two numbers
# EUCLIDEAN ALGO

def GCD(a,b):
    assert int(a) == a and int(b) == b ,'The number must be integer only'
    if a<0:
        a=a*-1
    if b<0:
        b=b*-1
    if a%b == 0 :
        return a
    else:
        return GCD(b, a%b)

print(GCD(48,-1.8))