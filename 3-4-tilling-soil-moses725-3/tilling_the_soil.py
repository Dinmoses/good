import math

print('Welcome to the Fertilizer Calculator! I will ask you for the length and width of four rectangular sections. Please enter your measurements in feet (numbers only, please). If you do not have a particular section, simply enter zero (0) for those dimensions! Press ENTER to start!')
# The beginning print statement has been written, WRITE YOUR CODE BELOW:

# TO-DO Collect dimensions

front_length = float(input("What is the length of the front section? "))
front_width = float(input("What is the width of the front section? "))
rear_length = float(input("What is the length of the rear section? "))
rear_width = float(input("What is the width of the rear section? "))
left_length = float(input("What is the length of the left section? "))
left_width = float(input("What is the width of the left section? "))
right_length = float(input("What is the length of the right section? "))
right_width = float(input("What is the width of the right section? "))

# TO-DO Calculate areas

front_area = front_length * front_width
rear_area = rear_length * rear_width
left_area = left_length * left_width
right_area = right_length * right_width

# TO-DO Total area
total_area = front_area + rear_area + left_area + right_area

# TO-DO Calculate the number of bags of fertilizer

actual_bags = total_area / 2000
bags_needed = math.ceil(actual_bags)

# TO-DO Calculate the cost of fertilizer

fertilizer_cost = bags_needed * 27

# TO-DO Calculate labor hours and cost

labor_hours = math.ceil(total_area / 2500)
labor_cost = labor_hours * 20


# TO-DO Total cost

total_cost = fertilizer_cost + labor_cost

# TO-DO Calculate the amount of nitrogen and potassium
nitrogen = actual_bags * 1
potassium = actual_bags * 0.125
# TO-DO Output the results
print(f"\nTotal area: {int(total_area)} sq. feet")
print(f"Bags of fertilizer required: {bags_needed}")
print(f"Cost of fertilizer: ${fertilizer_cost:.2f}")
print(f"Minimum hours required: {labor_hours}")
print(f"Cost of labor: ${labor_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Nitrogen applied to soil: {nitrogen:.3f} pounds")
print(f"Potassium applied to soil: {potassium:.3f} pounds")

