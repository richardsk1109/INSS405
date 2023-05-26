def get_numbers(num_inputs):
    numbers=[]
    for i in range(num_inputs):
        number = float(input("Enter a number:"))
        numbers.append(number)
    return numbers

def calculate_mean(numbers):
    total = sum(numbers)
    mean = total/len(numbers)
    return mean

def calculate_mean(numbers):
    total = sum(numbers)
    return total

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n= len(numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n //2-1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median


num_inputs = 10
input_numbers = get_numbers(num_inputs)


mean = calculate_mean(input_numbers)


median = calculate_median(input_numbers)


total_sum= sum(input_numbers)


print('numbers:', input_numbers)
print('mean:',mean)
print('median:',median)
print('sum:',total_sum)







