import math

# TO-DO Determine if number is even or odd
def is_even(number):
    return number % 2 == 0

# TO-DO Determine if number has perfect square root
def has_perfect_square_root(number):
    return int(math.sqrt(number)) == math.sqrt(number)

# TO-DO Determine all factors of number
def find_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

# Main loop
play = True
while play:
    try:
        num = int(input("Enter a whole number (i.e., an integer): "))
        
        print(f"\nThe number you entered is {num}.")
        print(f"{num} is an {'even' if is_even(num) else 'odd'} number.")
        print(f"{num} {'has' if has_perfect_square_root(num) else 'does not have'} a perfect square root.")
        print(f"The factors of {num} are {', '.join(map(str, find_factors(num)))}.\n")

        again = input("Would you like to enter another number? (Y/N): ").strip().lower()
        play = again == 'y'
    except ValueError:
        print("Oops! Please enter a valid whole number.\n")

print("\nThank you for playing!")

