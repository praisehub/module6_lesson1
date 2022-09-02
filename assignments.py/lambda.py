#add 2
from tabnanny import check


print((lambda x : x + 2)(10))
#generating a list and add 2
#figures = [lambda x=x : x+2 for x in range(2,10)]
#for figure in figures:
 #print(figures())
 
figures = [(lambda x:x+2)(x)for x in range(1,10)]
print(figures)

# #using conditional statements
# check_A_grade = lambda grade : 'got an A' if grade >= 90 else 'did not get an A'

# print(check_A_grade(90))
# print(check_A_grade(10))

# #defining function n
# def myfunc(n):
#     return lambda a : a ** n
# square = myfunc(2)

# cube = myfunc(3)

# print(square(11))
# print(cube(11))
# #square of a number

# print((lambda a, n : a**n)(3,2))


