




def decor(fun):
    def inner():
        value = fun()
        return value+10
    return inner

'''def num():
    return 10
result_fun = decor(num)
print(result_fun())'''


''''@decor
def myfunction():
    return 20
print(myfunction())'''


@decor
def display():
    return 25
print(display)

import sys
sys.exit()


def sum(lst1,lst2):
    sum1=0
    sum2=0
    for i in lst1:
        sum1=sum1+i
    for i in lst2:
        sum2=sum2+i
    return  sum1+sum2

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
result = sum(lst1, lst2)
print(result)





import sys
sys.exit()

from functools import *
lst1 = [1,2,3,4,5]
result = reduce(lambda x,y:x*y,lst1)
print(result)

sum = reduce(lambda a,b:a+b, range(1,11))
print(sum)
lst2 = [6,7,8,9,10]

sum1 = reduce(lambda a,b:a+b,lst1)
sum2 = reduce(lambda a,b:a+b,lst2)
result=sum1+sum2
print(result)

import sys
sys.exit()

lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
lst3 = list(map(lambda x,y:x*y,lst1,lst2))
print(lst3)

import sys
sys.exit()

lst1 = [1,2,3,4,5]
new_list=list(map(lambda x:x**2,lst1))
print(new_list)



import sys
sys.exit()

def square(x):
    return x*x
lst = [1,2,3,4,5]
new_list= list(map(square,lst))
print(new_list)

import sys
sys.exit()


lst = [10,15,23,25,45,56,88,56,74,23,25,56]
new_list = list(filter(lambda x: (x%5==0),lst))
print(new_list)

import sys
sys.exit()


def even_function(x):
    if x%2==0:
        return True
    else:
        False
lst = [11,12,13,4,15,16,17,18]
even_list = list(filter(even_function,lst))
print(even_list)

import sys
sys.exit()

def even_function(x):
    if x%2==0:
        return True
    else:
        False
lst = [12,34,56,48,75,62,65,45]
even_list = list(filter(even_function,lst))
print(even_list)


import sys
sys.exit()


max_number = lambda x, y:x if x>y else y
print(max_number(10,156))


import sys
sys.exit()

f = lambda x:x*x
print(f(5))

f = lambda x,y,z:x+y+z
print(f(5,10,15))