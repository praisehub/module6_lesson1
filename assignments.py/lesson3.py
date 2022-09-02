import numpy as np

#array of numbers between 1 and 100
num = [*range(1, 101)]
print(f"ARRAY OF NUMBERS BETWEEN 1 AND 100\n {'-' *100}")
print(num)

#generating the even numbers within the array
even_numbers = np.array([*filter(lambda x: x%2 == 0, num)])
print(f"EVEN NUMBERS WITHIN ARRAY\n {'-' *100}")
print(even_numbers)

#generating lcm of even numbers from the array
lcm_numbers = np.lcm.reduce(even_numbers)
print(f"LCM OF EVEN NUMBERS FROM ARRAY\n {'-' *100}")
print(lcm_numbers)