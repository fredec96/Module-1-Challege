def Author():
    print('Hello, my name is Cole Frederick')
Author()

import csv
from pathlib import Path

print('\n ---------- Part 1: Automate the Calculations ---------- \n')

''' This section automates calculations for the given loan portfolio summaries and prints all calculations 
    with descriptive messages.'''

loan_costs = [500, 600, 200, 1000, 450]

'''The `len` function is used to calculate the total number of loans in the list and assign the value to the 
    variable 'number_of_loans'. An f string is then used to print 'number_of_loans' with a descriptive message.'''
number_of_loans = len(loan_costs)
print(f'The number of loans is: {number_of_loans}')


'''The `sum` function is used to calculate the total of all loans in the list and assign the value to the variable 
    'loan_cost_total'. An f string is then used to print 'loan_cost_total' with a descriptive message.'''
loan_cost_total = sum(loan_costs)
print(f'The total cost of the loans is: ${loan_cost_total}')


'''The sum of all loans represented by the 'loan_cost_total' variable is divided by the 'number_of_loans' variable 
    to assign a value to the 'average_loan_amount' variable. An f string is then used to print the 'average_loan_amount' 
    with a descriptive message.'''
average_loan_amount = (loan_cost_total / number_of_loans)
print(f'The average loan amount is: ${average_loan_amount}')


print('\n ---------- Part 2: Analyze Loan Data  ---------- \n')


'''This section analyzes the given loan to determine the investment evaluation.
    'present_value', is calculated to determine what this loan would be worth. 
    An if statement is then used to and a decide if the 'present_value' is greater than or equal to the 'loan_price'.
    If the present_value is greater than or equal to the cost of the loan, it is determined to be worth buying. Else
    it is too expensive. An f string is then used to print the results with a descriptive message. If the loan is worth 
    buying, net_present_value is calculated and included in the f string to display the expected profit of buying the loan'''

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# get() is used to extract the future value on the loan from the loan dictionary.
future_value = loan.get('future_value', '')
print(f'The Future Value of the loan is: ${future_value}')

# get() is used to extract the remaining months on the loan from the loan dictionary.
remaining_months = loan.get('remaining_months', '')
print(f'Remaining months on the loan: {remaining_months}')


''' The forumula for Present Value to calculate the 'present_value' of the loan. A minimum required return of 20% is used as the discount rate.'''
discount_rate = .20
present_value = (future_value / (1 + (discount_rate/12)) ** remaining_months)

#An f string is used to print the present value, which is turned into a float
print(f'The Present Value of the Loan is: ${present_value:.2f}')



''' #This section uses a conditional statement to decide if the loan is worth buying. If the present value is greater than or equal to the cost of buying the loan, 
    it is determined to be worth at least the cost to buy it. Else, the loan is too expensive and will not be proffitable to buy. How profitable buying the loan
    would be is represented by the variable 'net_present_value' which is calculated by subtracting the loan price from the present_value.'''

# net_present_value is the profitability of buying the loan, get() is used to retrieve the 'loan_price' from the loan.
net_present_value = present_value - loan.get('loan_price', '')

# if statement is used to decide if the loan is worth buying, get() is used to retrieve the 'loan_price' from the loan.
if present_value >= loan.get('loan_price', ''):
    # If the loan is worth buying an f string is used to print the fact, along with the expected profit
    print(f'This loan is worth at least the cost to buy it, the expected profit is: ${net_present_value:.2f}')
else:
    print('This loan is too expensive and not worth the price')


print('\n ---------- Part 3: Perform Financial Calculations ---------- \n')

'''Calculate the present value for the loan given the following loan data
    Two different coding methods are presented, both come to the same result'''

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
'''First Method: Parameters 'future_value' and 'remaining_months' are not defined in the function. This method directly follows 
    the Challenge instruction. After discussing with my professor it is the better option than Method 2'''

# his function is used to calculate present value.
def calculate_loan_present_value(future_value, remaining_months, annual_discount_rate):
    new_loan_present_value = (future_value / (1 + (annual_discount_rate/12)) ** remaining_months)
    print(f'The Present Value of the Loan is: ${new_loan_present_value:.2f}')
    return new_loan_present_value

# Call the calculate_loan_present_value function
calculate_loan_present_value(new_loan['future_value'], new_loan['remaining_months'], 0.2)



'''Second Method: Parameters 'future_value' and 'remaining_months' are defined in the function by including 'dic' parameter. 
    I spoke with the professor, who said in a larger real world use case scenario this method would move too much data by calling 
    the entire dictionary. I had already finished coding both methods so I wanted to include my work.'''

#1. This function is used to calculate present value. The variable new_loan_present_value_2 is created for the second method.
def calculate_loan_present_value_2(dic, annual_discount_rate):
    new_loan_present_value_2 = ((dic['future_value']) / (1 + (annual_discount_rate/12)) ** (dic['remaining_months']))
    print(f'The Present Value of the Loan is: ${new_loan_present_value_2:.2f}')
    return new_loan_present_value_2

#Call the calculate_loan_present_value_2 function
calculate_loan_present_value_2(new_loan, 0.2)

print('\n ---------- Part 4: Conditionally Filter Lists of Loans ---------- \n')

"""Part 4 uses a loop to iterate through a series of loans and select only the inexpensive loans. 
    A second loop is used to print the loans indivually. """

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

'''Create an empty list called `inexpensive_loans` to be filled later. Idex position 0 is given 
    an arbitrary value so the loans can later be printed using their index positions as a numbering system''' 
inexpensive_loans = [0]


'''This section uses an if statement inside of a for loop to itentify loans with a price 
    that is less than or equal to 500, then appends the qualified loan to the `inexpensive_loans` list'''
for loan in loans:
    if loan['loan_price'] <= 500:
         inexpensive_loans.append(loan)
         

'''This section numbers and individually prints the loans contained inside of the 'inexpensive_loans" list. 
    A for loop is used to sort through the loans in 'inexpensive_loans' individually, and the index 
    position is used to number the loans when printed in the f string. Index position 0 has been given 
    an arbitrary value and skipped so that the loan numbers begin at 1'''
for loan in (inexpensive_loans):
    if inexpensive_loans.index(loan) > 0: 
        print (f"Inexpensive loan Number {inexpensive_loans.index(loan)}: {loan}")



print('\n ---------- Part 5: Save the Results ---------- \n')

# Part 5 outputs the list of inexpensive loans to a new csv file


# Set the header for the CSV file containing the inexpensive loans
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the file path for the CSV file containing the inexpensive loans
output_path = Path("inexpensive_loans.csv")


'''Use the csv library and `csv.writer` to write the header row, followed by each row of 
    `loan.values()` from the `inexpensive_loans` list.'''
with open(output_path, "w") as csvfile:
    # Create a csvwriter
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header to the CSV file
    csvwriter.writerow(header)

    '''Write the values of each dictionary inside of `inexpensive_loans` list
        as a row in the CSV file. Index position 0 in 'inexpensive_loans' is skipped 
        because it was used for formatting purposes in part 4'''
    for loan in inexpensive_loans:
        if inexpensive_loans.index(loan) > 0: 
            csvwriter.writerow(loan.values())



# Need to finish comments on section 2-4, copy and paste comments to word to spell check