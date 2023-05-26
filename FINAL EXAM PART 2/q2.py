import random as rand
def generate_rand_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(rand.randint(1,1000))
    return numbers

def sort_numbers(numbers):
    numbers.sort()
    return numbers

random_numbers = generate_rand_numbers(100)
sorted_numbers = sort_numbers(random_numbers)

print('sorted numbers:', sorted_numbers)





