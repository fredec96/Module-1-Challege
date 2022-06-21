def Author():
    print('Hello, my name is Cole Frederick')
Author()

import csv
from pathlib import Path

print('\n ---------- Part 1: Automate the Calculations ---------- \n')

# Automate the calculations for the loan portfolio summaries.
    #1. Use the `len` function to calculate the total number of loans in the list.
    #2. Use the `sum` function to calculate the total of all loans in the list.
    #3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    #4. Print all calculations with descriptive messages.

loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print(f'The number of loans is: {number_of_loans}')

loan_cost_total = sum(loan_costs)
print(f'The total cost of the loans is: ${loan_cost_total}')

average_loan_amount = (loan_cost_total / number_of_loans)
print(f'The average loan amount is: ${average_loan_amount}')

print('\n ---------- Part 2: Analyze Loan Data  ---------- \n')

# Analyze the loan to determine the investment evaluation.
# Calculate a Present Value, or a "fair price" for what this loan would be worth 
# Decide if the present value represents the loan's fair value.

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
future_value = loan.get('future_value', '')
print(f'The Future Value of the loan is: ${future_value}')

remaining_months = loan.get('remaining_months', '')
print(f'Remaining months on the loan: {remaining_months}')


#2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
discount_rate = .20
present_value = (future_value / (1 + (discount_rate/12)) ** remaining_months)
print(f'The Present Value of the Loan is: ${present_value:.2f}')


#3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    #a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    #b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
net_present_value = present_value - loan.get('loan_price', '')
if present_value >= loan.get('loan_price', ''):
    print(f'This loan is worth at least the cost to buy it, the expected profit is: ${net_present_value:.2f}')
else:
    print('This loan is too expensive and not worth the price')


print('\n ---------- Part 3: Perform Financial Calculations ---------- \n')

# Calculate the present value for the loan given the following loan data
# Two different coding methods are presented, both come to the same result

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# First Method: Parameters 'future_value' and 'remaining_months' are not defined in the function
#1. Define a new function that will be used to calculate present value.
#2. Use the function to calculate the present value of the new loan.
    #a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
def calculate_loan_present_value(future_value, remaining_months, annual_discount_rate):
    new_loan_present_value = (future_value / (1 + (annual_discount_rate/12)) ** remaining_months)
    print(f'The Present Value of the Loan is: ${new_loan_present_value:.2f}')
    return new_loan_present_value

calculate_loan_present_value(new_loan['future_value'], new_loan['remaining_months'], 0.2)

# Second Method: Parameters 'future_value' and 'remaining_months' are defined in the function by including 'dic' parameter
#1. Define a new function that will be used to calculate present value.
#2. Use the function to calculate the present value of the new loan.
    #a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
def calculate_loan_present_value_2(dic, annual_discount_rate):
    new_loan_present_value_2 = ((dic['future_value']) / (1 + (annual_discount_rate/12)) ** (dic['remaining_months']))
    print(f'The Present Value of the Loan is: ${new_loan_present_value_2:.2f}')
    return new_loan_present_value_2

calculate_loan_present_value_2(new_loan, 0.2)

print('\n ---------- Part 4: Conditionally Filter Lists of Loans ---------- \n')

