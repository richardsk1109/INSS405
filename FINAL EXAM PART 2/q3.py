import random as rand

def generate_rand_integers():
    numbers=[]
    for i in range(100):
        number= rand.randint(1, 1000)
        numbers.append(number)
    return numbers

def print_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    for odd_num in odd_numbers:
        print(odd_num)

rand_integers = generate_rand_integers()
print('odd numbers:')
print_odd_numbers(rand_integers)