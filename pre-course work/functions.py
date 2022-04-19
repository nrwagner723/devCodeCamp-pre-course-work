# demo video
# add 2 nums
def add_two_nums(num1, num2):
    return num1 + num2

sum = add_two_nums(3, 5)
print(sum)

# print user name 
my_name = 'Natalie'

def print_name(name):
    print(name)

print_name('Mike')
print_name(my_name)

# get user input & print
def get_first_name():
    first_name = input('What is your first name?')
    print(f'First Name: {first_name}')

get_first_name()

# task 
def run_calculations():
    result1 = add_two_numbers(200, 50)
    print(result1)
    result2 = subtract_two_numbers(20, 5)
    print(result2)
    result3 = mutliply_and_divide(4, 5, 10)
    print(result3) 

def add_two_numbers(num1, num2):
    result = num1 + num2
    return result

def subtract_two_numbers(num1, num2):
    result = num1 - num2
    return result

def mutliply_and_divide(num1, num2, num3):
    result = (num1 * num2) / num3
    return result

run_calculations()