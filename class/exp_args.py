"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""
def sum_args(*numbers):
    print(sum(numbers))

sum_args(1,2,3,4,5,58,184,8654)


"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""

# def concat_strings(*args):
#     # Use the join method to concatenate all string arguments
#     concatenated_string = ''.join(args)
#     return concatenated_string
#
# # Example usage
# result = concat_strings("Hello", " ", "world", "!", " How", " are", " you", "?")
# print(result)  # Output: Hello world! How are you?

def concat_strings(*words):
    print(''.join(words))

concat_strings('hi','love')


"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""


def calculate_expenses(name, monthly_income, *variable_expenses, **fixed_expenses):
    # Calculate total variable expenses
    total_variable_expenses = sum(variable_expenses)

    # Calculate total fixed expenses
    total_fixed_expenses = sum(fixed_expenses.values())

    # Calculate remaining balance
    remaining_balance = monthly_income - total_variable_expenses - total_fixed_expenses

    # Print the result
    print(f"{name} tu saldo restante después de tus gastos es: ${remaining_balance:.2f}")


# Example usage
calculate_expenses("Amalia", 5000, 300, 150, 200, renta=1200, utiles=300, internet=50, gas=200)
