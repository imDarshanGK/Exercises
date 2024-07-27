import math
def prime_check(nums):
    is_prime = True
    if nums == 1:
        is_prime = False
    for i in range(2,math.ceil(nums/2)+1):
        if nums % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("Not a prime number")
number = int(input("Enter a number>> "))
prime_check(number)
