
def calculate_letter_grade(mean):
    if mean >= 90:
        return "A"
    elif mean >= 80:
        return "B"
    elif mean >= 70:
        return "C"
    elif mean >= 60:
        return "D"
    elif mean >= 50:
        return "E"
    else:
        return "F"


num_users = 5
grades = []
for i in range(num_users):
    grade = float(input(f"Enter the final grade for user {i+i}: "))
    grades.append(grade)


mean_grade = sum(grades) /num_users


final_letter_grade = calculate_letter_grade(mean_grade)


print(f"Mean Grade: {mean_grade}")
print(f"Final Letter Grade: {final_letter_grade}")

