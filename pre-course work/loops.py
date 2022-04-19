# task 1: create a while loop that will iterate 5 times
num = 4
positive = True
while positive == True:
    if num == -1:
        positive = False
        print('The number is no longer positive')
    else: 
        num -= 1
        print(num)

# task 2: using the input function, create a for loop that will print each character in a string
word = input('What is your favorite word?')

for x in word: 
    print(x)