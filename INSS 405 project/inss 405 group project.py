def calculate_weight(age, gender, length):
    if age == "0-6 months":
        if gender == "girl":
            length_range = (21,25)
            weight_range = (5,16)
        elif gender == "boy":
            length_range = (21,26)
            weight_range = (5,17)
        else:
            return "Invalid gender"
    elif age == "6-12 months":
        if gender == "girl":
            length_range = (25, 29)
            weight_range = (16, 19)
        elif gender == "boy":
            length_range = (26,30)
            weight_range = (17,21)
        else:
            return "Invalid gender"
    else:
        return "Invalid age"

    if length < length_range[0] or length > length_range[1]:
        return "Invalid length. Please provide a length within the range."

    normalized_length = (length - length_range[0]) / (length_range[1] - length_range[0])
    predicted_weight = weight_range[0] + normalized_length * (weight_range[1] - weight_range[0])

    return predicted_weight

age = input("Enter the age of the baby (0-6 months or 6-12 months):")
gender = input("Enter the gender of the baby (boy or girl):")
length = float(input("Enter the length of the baby (in inches):"))

weight = calculate_weight(age, gender, length)
if isinstance(weight, str):
    print(weight)
else:
    print("weight for the baby:", weight)
