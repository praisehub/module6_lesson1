import numpy as np
#CREATING A LIST OF INTEGERS BETWEEN 5.5 AND 20.5
list1 = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list1)

#COUNTING THE EVEN AND ODD NUMBERS IN THE LIST
even_numbers = list(filter(lambda x: x%2 == 0, list1))
odd_numbers = list(filter(lambda x: x%2 !=0, list1))
print(f"EVEN NUMBERS BETWEEN 5.5 AND 20.5\n {'-' *100}")
print(even_numbers)
print(f"ODD NUMBERS BETWEEN 5.5 AND 20.5\n {'-' *100}")
print(odd_numbers)

#SQUARE AND CUBE OF EVERY NUMBER IN THE LIST
square_numbers = list(map(lambda x: x**2 , list1))
cube_numbers = list(map(lambda x: x**3, list1))
print(f"SQUARE OF NUMBERS IN THE LIST\n {'-' *100}")
print(square_numbers)
print(f"CUBE OF NUMBERS IN THE LIST\n {'-' *100}")
print(cube_numbers)
