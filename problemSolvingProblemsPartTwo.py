
#TASK 1: HAPPY NUMBERS 
# A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19
# Write a method that determines if a number is happy or sad
#LIST OF STEPS
# 1. Declare function 'convert_string_to_integer_list' with on parameter 'num'
# 2. Inside the function create a list ('list_of_digits') which converts the characters in the printed string into individual list items.
# 3. Start For loop to iterate over the index points in range of the length of your list
#   3.a. Inside the loop declare a variable equal to the integer value of the index point '0' in your list.
#   3.b. Pop the list of the index point 0.
#   3.c. Append the list with the variable with the new integer value.
# 4. Once the loop has fully iterated over the list, call the next 'square_each_number' function with your newly created list in the parameter.
# 5. Inside Our next function start a For loop to iterate for each index point over the range of the length of the list that was passed into the parameter.
#   5.a. declare a variable to equal the '0' index point.
#   5.b declare a second variable and set it to be equal to the value of the last variable that was declared squared.
#   5.c Pop the list of the index point 0.
#   5.d. Append the list with the variable with the new integer value.
# 6. Once the for loop has replaced the old values with the new values call the next function 'check_sum_then_convert_to_string' with the new list passed into the parameter.
# 7. Inside 'check_sum_then_convert_to_string' start an if/elif/else clause.
#   7.a. Set the if statemnt to check if the sum is equal to one.
#       7.a.a. If it is equal to one use string interpolation to print that the number is in fact equal.
#   7.b. Set the elif statment to check if the sum is in a list called 'check for failures' where we check to see if we are in an endless loop.
#       7.b.a. If the sum is in the list print 'Sorry number is not a happy number'
#   7.c. Set the else statment to send the integer of the sum to the 'check for failures list'
#   8.d. Convert sum into a string and then send it back to our first function to go around until the program returns the number either is or isn't a happy number.'



#Below is out initial function used to convert the inputed string value into a list of integers. Should only be called once.
def convert_string_to_integer_list(num):
        list_of_digits = list(num)
        for index in range((len(list_of_digits))):
            number = int(list_of_digits[0])
            list_of_digits.pop(0)
            list_of_digits.append(number) 
        square_each_number(list_of_digits)

#Below is our function that squares each number that is in list format
def square_each_number(integer_list):
    for index in range((len(integer_list))):
        number = integer_list[0]
        squared_number = number * number
        integer_list.pop(0)
        integer_list.append(squared_number)
    check_sum_then_convert_to_string(sum(integer_list))

#Below is our function we use to compare our next sum vs the numbers that have already been added to it.
checks_for_failures = []
def check_sum_then_convert_to_string(sum):
    if sum == 1:
        print(f'{original_number} IS a happy number!!! (:')
    elif sum in checks_for_failures:
        print(f'Sorry {original_number} is NOT a happy number ):')
    else:
        checks_for_failures.append(sum)
        sum = str(sum)
        convert_string_to_integer_list(sum)

original_number = (input("Insert number to check if it's happy: "))
convert_string_to_integer_list(original_number)


#TASK 2: Prime Numbers
# A prime number is a number that is only divisible by one and itself.       
# Write a method that prints out all prime numbers between 1 and 100
#LIST OF STEPS
# 1. Declare a funtion to find the prime numbers in a list that is passed in.
# 2. Inside the function declare a variable to store a new updated list with all the found prime numbers.
# 3. Then start a 'for' loop iterating over the numbers in the list that was passed in.
#   3.a. Start an if statement looking to see if the number is equal to 0 or 1 and if it is to 'continue'.
#   3.b. Set 'elif' to check if the number is 2, and if it is to send it to the list of prime numbers.
# 4. Declare a variable to the boolean False, this variable should only turn true when the number is either passed over or added to the list of prime numbers.
# 5. Start 'while' loop that runs as long as the previous variable is 'False".
#   5.a.Inside the while loop start a for loop that iterates over the 'range' of our list from the 2nd index to the one after whatever the current number is in the sequence.
#   5.b.Start an clause clause checking to see if the number 'modulos' the current index value is equal to zero.
#       5.b.a. Once the num % index finally = zero set an if statment checking to see if the current index value is equal to the current number.
#           5.b.a.a. If it is the number is a prime so use 'append' to send it to the list of prime numbers.
#           5.b.a.b. if it is not then the number is not a prime so use 'break' to escape the loop and move onto the next number.
# 6. Once all of the number in the list have either been determined to be a prime number or not use 'print' and string interpolation to pass in our new list and let the user know which numbers were prime.  

#Below is our function we call to go through a list and find all the prime numbers and return them.
def find_the_prime_nums(list):
    full_list_of_primes = []
    for num in list:
        if num == 0 or num == 1:
            continue
        elif num == 2:
            full_list_of_primes.append(num)  
            continue
        number_designated = False
        if num > 1:
            while number_designated == False:
                for index in range(2, num+1):
                    if (num % index == 0):
                        if (index) == num:
                            full_list_of_primes.append(num)
                            number_designated = True
                        else:
                            number_designated = True
                            break
    print(f'The prime numbers in your list are:{full_list_of_primes}.')                    
    return full_list_of_primes                   

prime_numbers_1_through_100 = find_the_prime_nums([num for num in range(101)])

#TASK 3: Fibonacci (I believe I did the hard version, but it seemed too easy so let me known if I actually just did the normal version)
# A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Write a method that does the Fibonacci sequence starting at 1
# HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user input
#LIST OF STEPS
# 1. Declare funtion to start a fibonacci sequence off of one 'start' number and set a parameter to recieve a user input number.
# 2. Inside the funtion declare your first variable and set it equal to the number passed in.
# 3. Declare a second variable also equal to the number that was passed in.
# 4. Declare a third variable with a null value.
# 5. Declare a fourth variable with a null value.
# 6. Declare a list set to a null value.
# 7. Start a 'while' loop, with the loop set to stop after a certain number of iterations.
#   7.a. Inside the while loop use '.extend' to add both the first and second variable values into the empty list.
#   7.b. Set the third variable equal to the first.
#   7.c. Set the fourth variable equal to the second.
#   7.d. Set the first varaible equal to the third.
#   7.e. Set the second variable equal to the fourth.
# 8. Wait for the while loop to iterate for the specified amount of times.
# 9. Return completed list.
# 10. Print completed list.'

def fibonaccinator (start_number):
    first_place_holder = start_number
    second_place_holder = start_number
    third_place_holder = None
    fourth_place_holder = None
    fibonacci_list = []
    while len(fibonacci_list) < 30:
        fibonacci_list.extend([first_place_holder, second_place_holder])
        third_place_holder = first_place_holder + second_place_holder
        fourth_place_holder = third_place_holder + second_place_holder
        first_place_holder = third_place_holder
        second_place_holder = fourth_place_holder
    return fibonacci_list

fibonaccified_number = fibonaccinator(int(input('Type in a number to recieve your Fibonacci sequence: ')))
print(f'Your Fibonacci sequence is:{fibonaccified_number}')