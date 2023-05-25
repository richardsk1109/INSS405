def predict_weight(age, gender, length):
    if age == "0-6 months":
        if gender == "female":
            weight_range = (5, 16)
        elif gender == "male":
            weight_range = (5, 17)
    elif age == "6-12 months":
        if gender == "female":
            weight_range = (16, 19)
        elif gender == "male":
            weight_range = (17, 21)

    min_length = 20
    max_length = 30

    # Check if the input length is within the range
    if length < min_length or length > max_length:
        return "Invalid length. Please provide a length between 20 and 30 inches."

    # Calculate the weight based on the length
    length_range = (min_length, max_length)
    normalized_length = (length - length_range[0]) / (length_range[1] - length_range[0])
    predicted_weight = weight_range[0] + normalized_length * (weight_range[1] - weight_range[0])

    return predicted_weight


# Example usage
age = input("Enter the age of the baby (0-6 months or 6-12 months): ")
gender = input("Enter the gender of the baby (female or male): ")
length = float(input("Enter the length of the baby in inches (20-30 inches): "))

predicted_weight = predict_weight(age, gender, length)
print("Predicted weight for the baby or toddler: {} pounds".format(predicted_weight))
