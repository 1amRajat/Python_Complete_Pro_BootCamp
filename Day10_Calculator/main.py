def add(num1, num2):
    res = num1 + num2
    return res


def sub(num1, num2):
    res = num1 - num2
    return res


def mul(num1, num2):
    res = num1 * num2
    return res


def div(num1, num2):
    res = num1 / num2
    return res


action = {'+': add, '-': sub, '*': mul, '/': div}
prog_continue_ind = True
first_num = float(input("Whats the first number? :"))
for keys in action:
    print(keys)

while prog_continue_ind:
    user_action = input("Pick an operation: ")
    second_num = float(input("Whats the next number?: "))
    selected_func = action[user_action]
    result = selected_func(first_num, second_num)
    print(f"{first_num}{user_action}{second_num} = {result}")

    continuity_input = input(f"Type 'Y' to continue calculating with {result}, or 'n' to end the calculation: ")
    if continuity_input.lower() == 'y':
        prog_continue_ind = True
        first_num = result
    else:
        prog_continue_ind = False
        print("Thank you for using the calculator!")
