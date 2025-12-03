# TO-DO Calculate gross pay
def gross_pay(hourly_wage, hours_worked):
    return hourly_wage * hours_worked
    
# TO-DO Calculate withholding
def calculating_withholding(gross_pay):
    federal_tax = gross_pay * 0.10          # 10% Federal Tax
    state_tax = gross_pay * 0.05            # 5% State Tax
    social_security = gross_pay * 0.062     # 6.2% Social Security

    total_withholding = federal_tax + state_tax + social_security

    return federal_tax, state_tax, social_security, total_withholding

# TO-DO Calculate net pay
def calculating_net_pay(gross, total_withholding):
    return gross - total_withholding

# TO-DO Calculate discretionary income
def calculate_discretionary_income(revenue, expenses):
    return revenue + expenses
# TO-DO Create your menu and program
revenue = 0.0
expenses = 0.0

while True:
    print("1-Calculate net pay")
    print("2-Enter revenue or expense")
    print("3-Show discretionary income")
    print("4-Exit")

    choice = input("Choice: ")

    if choice == "1":
        try:
            hourly_wage = float(input("What is your hourly wage? "))
            hours_worked = float(input("How many hours did you work? "))
            gross = gross_pay(hourly_wage, hours_worked)
            fed_tax, state_tax, ss_tax, total_withheld = calculating_withholding(gross)
            net = calculating_net_pay(gross, total_withheld)

            print(f"\nGross Pay: ${gross:.2f} ({hours_worked} hours @ ${hourly_wage:.2f}/hr)")
            print(f"Federal tax: ${fed_tax:.2f}")
            print(f"State tax: ${state_tax:.2f}")
            print(f"Social security: ${ss_tax:.2f}")
            print(f"Net pay: ${net:.2f}")

        except ValueError:
            print("Please enter valid numeric input.")
    
    elif choice == "2":
        while True:
            name = input("Enter transaction name: ")
            try:
                amount = float(input("Enter amount (use negative sign for expense): "))
                if amount < 0:
                    expenses += amount
                else:
                    revenue += amount
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            another = input("Another? (Y/N): ").strip().lower()
            if another != "y":
                break
    
    elif choice == "3":
        discretionary = calculate_discretionary_income(revenue, expenses)
        print(f"\nRevenue: ${revenue:.2f} Expenses: ${expenses:.2f} Discretionary: ${discretionary:.2f}")

    elif choice == "4":
        print("Thanks for using Wise Finance!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")