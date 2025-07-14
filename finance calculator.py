
"""Display "How may we assist?"
Display "1. INVESTMENT"
Display "2. BOND"

Get user input for 'option'

IF option is '1' THEN:
    Display "You chose INVESTMENT"
    Get investment amount, interest rate, and investment period
    Display "Choose A for Simple Interest or B for Compound Interest"
    Get user choice
    
    IF choice is 'A' THEN:
        Calculate Simple Interest
        Display Simple Interest and Total Amount
    
    ELSE IF choice is 'B' THEN:
        Calculate Compound Interest
        Display Compound Interest and Total Amount
    
ELSE IF option is '2' THEN:
    Display "You chose BOND"
    Get bond value, interest rate, and loan period
    Calculate monthly repayment, total repayment, and total interest
    Display repayment details

ELSE:
    Display "Invalid selection. Choose 1 for Investment or 2 for Bond."""


print("How may we assist?")
print("1. INVESTMENT")
print("2. BOND")

# Attain user input
option = input("Enter 1 or 2: ")

if option == '1':
    print("\nYou chose option 1: INVESTMENT.")
    investment_amount = float(input("Enter amount to be invested: R "))
    interest_rate = float(input("Enter interest rate (%): ")) / 100
    investment_period = int(input("Enter the investment period (in years): "))
    
    print("\nPlease choose an option below:")
    print("A. S.I - Simple Interest")
    print("B. C.I - Compound Interest")

    # Attain 2nd phase user input
    choice = input("Enter A or B: ")

    if choice == "A":
        print("\nYou chose choice A: Simple Interest")
        # Calculate Simple Interest
        interest_amount = investment_amount * interest_rate * investment_period
        # Calculate total amount after interest
        total_amount = investment_amount + interest_amount
        print(f"\nSimple Interest: R{interest_amount:.2f}")
        print(f"Total Amount: R{total_amount:.2f}")

    elif choice == "B":
        print("\nYou chose choice B: Compound Interest")
        # Calculate Compound Interest
        total_amount = investment_amount * (1 + interest_rate) ** investment_period
        interest_amount = total_amount - investment_amount
        print(f"\nCompound Interest: R{interest_amount:.2f}")
        print(f"Total Amount: R{total_amount:.2f}")

    else:
         print("selection not supported! Please choose A or B")
   

elif option == '2':
    print("\nYou chose option 2: BOND.")
    current_bond_amount = float(input("bond value: R "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): ")) / 100
    loan_period_years = int(input("Enter the loan period (in years): "))
    
    # Convert the annual interest rate to a monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12
    # Calculate the number of monthly periods (loan months)
    number_of_months = loan_period_years * 12

    print("\nCalculating monthly repayments...")

    # Calculate the monthly repayment using the formula for fixed repayments (annuity formula)
    try:
        monthly_repayment = (monthly_interest_rate * current_bond_amount) / (1 - (1 + monthly_interest_rate) ** -number_of_months)
        total_repayment = monthly_repayment * number_of_months
        total_interest_paid = total_repayment - current_bond_amount

        print(f"\nMonthly Repayment: R{monthly_repayment:.2f}")
        print(f"Total Repayment Over {loan_period_years} Years: R{total_repayment:.2f}")
        print(f"Total Interest Paid: R{total_interest_paid:.2f}")
    
    except ZeroDivisionError:
        print("Error: Interest rate cannot be 0.")
    except Exception as e:
        print(f"Error: {e}")

else:
    print("selection not supported! Please choose 1 for Investment or 2 for Bond.")
