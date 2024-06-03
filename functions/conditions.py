def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)
        

# Check if an operation istrue or false
def print_even_numbers(n):
    numbers =range(n)
    for number in numbers:
        if number %2 ==0:
          print(number)


# We can can combine the if statement with an optional else statement.
# The code in the else statement is executed if the preceeding if statement return false
def odd_or_even(n):
    numbers =range(n)
    for number in  numbers:
        if number % 2 ==0:
            print(f"{number}is even")
        else:
            print(f"{number}is odd")

# Elif statement allows us to do more than one comparision
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 3 ==0:
            print(f"{number} is divisible by 3")
        elif number % 5 ==0:
            print(f"{number} is divisible by 5")
        elif number % 7 ==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not diviible by 3, 5, 7")


# while loop
# Continues iterating as long as the set condition is true
def count_down(n):
    x =0 
    while n>x:
        print(n)
        n-=1


# while loop
# Break
# Stop the while loop even if the set condition is still true 
def count_down_to_five(n):
    x = 0
    while n > x:
        print(n)
        if n==5:
            break
        n-=1


# While loop
# Continue
# Skips the remainder of the current iteration and jumps to the next iteration of the while loop 
def divisible_by_seven(n):
    x = 1
    while x <= n:
        x+=1
        if x% 7!=0:
            continue
        print(f"{x} is divisible by 7")


# Using while, continue and if statement, write a function that prints all odd numbers between 0 and 100
# Create a function named fizzbuzz.For numbers divisible by 3 it prints fizz
# for numbers divisible by 5 it prints buzz
# for all the other numbers it prints fizzbuzz
# Use if, elif else
def divisibility(n):
    for num in range(n):
     if num%3==0 and num%5 ==0:
         print("fizzbuzz")
        #  continue
     elif num%3==0:
        print("fizz")
        # continue
     elif num%5==0:
         print("buzz")
         continue
     print(num)

    


       