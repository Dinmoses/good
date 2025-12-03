import math
# TO-DO Initialize the authorized variable
authorized = False
users = []
try:
    with open('authorized_users.txt', 'r') as file:
        data = file.readlines()
        for d in data:
            tmp = d.strip().split(",")
            user = {
                'username': tmp[0],
                'pass': tmp[1],
                'level': int(tmp[2])
            }
            users.append(user)
except FileNotFoundError:
    print("invalid credentials")
    exit()
# TO-DO Prompt user for username/password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
# TO-DO Compare input username and password with authorized users file
for user in users:
    if input_username == user['username'] and input_password == user['pass']:
        authorized = True
        break
# THEN, if authorized is True, run the code from tilling_the_soil.py by copying the necessary code in the BOTTOM 
if authorized:
    print("\nAccess granted. Running tilling_the_soil program...\n")

    # Main soil tilling code begins here
    print("Welcome to the Fertilizer Calculator!")
    print("I will ask you for the length and width of four rectangular sections. Please enter your measurements in feet (numbers only, please).")
    print("If you do not have a particular section, simply enter zero (0) for those dimensions!")
    print()
    # TO-DO Collect dimensions
    front_length = float(input("Length of front section: "))
    front_width = float(input("Width of front section: "))
    rear_length = float(input("Length of rear section: "))
    rear_width = float(input("Width of rear section: "))
    left_length = float(input("Length of left section: "))
    left_width = float(input("Width of left section: "))
    right_length = float(input("Length of right section: "))
    right_width = float(input("Width of right section: "))

    # TO-DO Calculate areas
    front_area = front_length * front_width
    rear_area = rear_length * rear_width
    left_area = left_length * left_width
    right_area = right_length * right_width
    # TO-DO Total area
    total_area = front_area + rear_area + left_area + right_area
    # TO-DO Calculate the number of bags of fertilizer
    bags_needed = math.ceil(total_area / 2000)
    # TO-DO Calculate the cost of fertilizer
    fertilizer_cost = bags_needed * 27
    # TO-DO Calculate labor hours and cost
    labor_hours = math.ceil(total_area / 2500)
    labor_cost = labor_hours * 20
    # TO-DO Total cost
    total_cost = fertilizer_cost + labor_cost
    # TO-DO Calculate the amount of nitrogen and potassium
    actual_bags = total_area / 2000
    nitrogen = actual_bags * 1 # pounds
    potassium = actual_bags * 0.125 # pounds
    
    # TO-DO Output the results
    print()
    print(f"Total area: {int(total_area)} sq. feet")
    print(f"Cost of fertilizer: ${fertilizer_cost}")
    print(f"Bags of fertilizer required: {bags_needed}")
    print(f"Minimum hours required: {labor_hours}")
    print(f"Cost of labor: ${labor_cost}")
    print(f"Total cost: ${total_cost}")
    print(f"Nitrogen applied to soil: {nitrogen:.3f} pounds")
    print(f"Potassium applied to soil: {potassium:.3f} pounds")

else:
    print("\nYou have entered invalid credentials, please find your password and start over")
    exit()