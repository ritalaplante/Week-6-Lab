#Part 1: Nested For loops
# 1. Print a triangle of numbers: ask the user for an numerical input and then
# print out a triangle as follows: if the user input is 5 you should print:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

userNum = int(input("Enter a number: "))

for i in range(1, userNum + 1):
    for j in range(i):
        print(i, end = ' ')
    print()

# 2. Write a similar function, but instead print out the exponents. i.e if user
# input is 5 you want to print
# 1
# 2 4
# 3 9 27
# 4 16 64 256
# 5 25 125 625 3125

userNum2 = int(input("Enter a number: "))

for i in range (1, userNum2 + 1):
    for j in range(i):
        print (i ** (j + 1), end = ' ')
    print()

#3. Print week and day. Ask user to input a number of weeks and a number of days.
# for each week you want to print the days below it. For example: If weeks = 2 and
# days = 3 you want to print
# Week 1:
    # Day 1
    # Day 2
    # Day 3
# Week 2:
    # Day 1
    # Day 2
    # Day 3

weeks = int(input("Enter the number of weeks: "))
days = int(input("Enter the number of days: "))

for i in range(1, weeks + 1):
    print("Week: ", i)
    for j in range(1, days + 1):
        print("Day: ", j)

#Part 2: return values
# 1. Write a function that calculates the perimeter of a rectangle. This function
# should take in two side lenghts as arguments and return the perimeter value.

def calcPerim(a, b):
    perimeter = a + b
    return perimeter

def main ():
    side1 = int(input("Enter a side length: "))
    side2 = int(input("Enter another side length: "))

    perimeter = calcPerim(side1, side2)
    print(perimeter)

main()

# Write a function that reverses a string. Instead of printing the reversed string
# the function should return the reversed string which is printed in the main
# function.

def reverseString(s):
    reversedString = ""
    for c in s:
        reversedString = c + reversedString
    return reversedString

def main():
    userString = input("Enter a string you would like to reverse: ")
    reversedString = reverseString(userString)
    print(reversedString)

main()



