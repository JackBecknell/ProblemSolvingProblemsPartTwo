#TEST ZONE
#END TEST ZONE


#To be a good problem solver, it is important to be able to break problems down. One way to go about this is to write 
# out the steps it will take to solve the problem. These steps are written down in English in a manner that are easily
#  explainable to someone who may not be technical. The idea is that in order to code something out, you first need to
#  have a good understanding of what it is you are attempting to solve.

#For each of the three problem solving problems below, write out the steps it will take to go about solving the problem.
# For example, once you are done writing out the steps for the “happy numbers” problem, you would then write out the
# code to solve the problem. You would then repeat the process for each ensuing problem. Ideally, this will be a good 
# habit that you will develop and carry forward with you for all problems you encounter at devCodeCamp and beyond.

#1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number

#b. A happy number is a number defined by the following process: starting with any positive integer, replace the number 
# by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number
# is 19

#c. Write a method that determines if a number is happy or sad
#Below is our list we continualy add our sums into until we find out if the original number is happy or not.


checks_for_failures = []
#Below is our function we use to compare our next sum vs the numbers that have already been added to it.
def check_sum_then_convert_to_string(sum):
    if sum == 1:
        print('This IS a happy number!!! (:')
    elif sum in checks_for_failures:
        print('Sorry this is NOT a happy number ):')
    else:
        checks_for_failures.append(sum)
        sum = str(sum)
        convert_string_to_integer_list(sum)
    
#Below is out initial function used to convert the inputed string value into a list of integers. Should only be called once.
def convert_string_to_integer_list(num):
        list_of_digits = list(num)
        length = len(list_of_digits)
        for index in range(length):
            number = int(list_of_digits[0])
            list_of_digits.pop(0)
            list_of_digits.append(number) 
        square_each_number(list_of_digits)

#Below is our function that squares each number that is in list format
def square_each_number(integer_list):
    length = len(integer_list)
    for index in range(length):
        number = integer_list[0]
        squared_number = number * number
        integer_list.pop(0)
        integer_list.append(squared_number)
    check_sum_then_convert_to_string(sum(integer_list))

convert_string_to_integer_list(input("Insert number to check if it's happy: "))


#2. Prime Numbers

#a. A prime number is a number that is only divisible by one and itself.
        
#b. Write a method that prints out all prime numbers between 1 and 100
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
               
        
                
                    
    return full_list_of_primes
                    

prime_numbers_1_through_100 = find_the_prime_nums([num for num in range(101)])
print(prime_numbers_1_through_100)
#3. Fibonacci

#a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest 
# is the series 1, 1, 2, 3, 5, 8, etc.

#b. Write a method that does the Fibonacci sequence starting at 1

#c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs