def calculate_updated_balance(balance, annual_interest_rate, monthly_payment_rate):
    """
    Calculate the updated balance after one month of minimum payment and interest.
    """
    monthly_interest_rate = annual_interest_rate / 12.0
    minimum_payment = balance * monthly_payment_rate
    unpaid_balance = balance - minimum_payment
    updated_balance = unpaid_balance * (1 + monthly_interest_rate)
    return updated_balance, minimum_payment


def print_monthly_statement(month, balance, minimum_payment, updated_balance):
    """
    Print the monthly statement including the minimum payment and remaining balance.
    """
    print(f"Month: {month}")
    print(f"Minimum monthly payment: {round(minimum_payment, 2)}")
    print(f"Remaining balance: {round(updated_balance, 2)}")


def calculate_balance_after_one_year(balance, annual_interest_rate, monthly_payment_rate):
    """
    Calculate and print the balance after one year of making minimum payments.
    """
    total_paid = 0
    for month in range(1, 13):
        updated_balance, minimum_payment = calculate_updated_balance(balance, annual_interest_rate, monthly_payment_rate)
        print_monthly_statement(month, balance, minimum_payment, updated_balance)
        total_paid += minimum_payment
        balance = updated_balance

    print(f"Total paid: {round(total_paid, 2)}")
    print(f"Remaining balance: {round(balance, 2)}")


def main():
    """
    Main function to take user input and calculate the balance after one year.
    """
    balance = float(input("Enter the initial balance: "))
    annual_interest_rate = float(input("Enter the annual interest rate as a decimal: "))
    monthly_payment_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))

    calculate_balance_after_one_year(balance, annual_interest_rate, monthly_payment_rate)


if __name__ == "__main__":
    main()