def Author():
    print('Hello my name is Cole Frederick')
Author()

import csv
from pathlib import Path

print('\n ---------- Part 1: Automate the Calculations ---------- \n')


loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print(f'The number of loans is: {number_of_loans}')

loan_cost_total = sum(loan_costs)
print(f'The total cost of the loans is: ${loan_cost_total}')

average_loan_amount = (loan_cost_total / number_of_loans)
print(f'The average loan amount is: ${average_loan_amount}')

print('\n ---------- Part 2: Analyze Loan Data  ---------- \n')

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get('future_value', '')
print(f'The Future Value of the loan is: ${future_value}')

remaining_months = loan.get('remaining_months', '')
print(f'Remaining months on the loan: {remaining_months}')


annual_discount_rate = 12 
present_value = (future_value / (1 + (.20/annual_discount_rate)) ** remaining_months)
print(f'The Present Value of the Loan is: ${present_value:.2f}')


if present_value >= loan.get('loan_price', ''):
    print('This loan is worth at least the cost to buy it')
else:
    print('This loan is too expensive and not worth the price')


print('\n ---------- Part 3: Perform Financial Calculations ---------- \n')

