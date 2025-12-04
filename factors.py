# Program to find all factors of a number

# Ask the user to enter a number
number = int(input("Enter a number: "))

print("The factors of", number, "are:")

# Loop through numbers from 1 up to the entered number
for i in range(1, number + 1):
    # Check if 'i' divides evenly into 'number'
    if number % i == 0:
        print(i)