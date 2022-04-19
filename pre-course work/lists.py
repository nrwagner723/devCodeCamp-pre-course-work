# demo video
first_names = ['natalie', 'maria', 'raymond']
print(first_names)

first_names.append('tori')
print(first_names)

print(first_names[0])

first_names[3] = 'tommy'
print(first_names)

popped = first_names.pop()
print(popped, first_names)

first_names.remove('maria')
print(first_names)

for name in first_names:
    print(name)

def determine_drive(list_ages):
    counter = 0
    for age in list_ages:
        if age >= 16:
            counter += 1
    total_people = len(list_ages)
    print(f'{counter}/{total_people} can drive')

ages = [5, 19, 7, 58, 34, 14]
determine_drive(ages)

# task
def add_odd(nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total += num
    return total

numbers = [12, 67, 35, 28, 99, 102]
print(add_odd(numbers))

