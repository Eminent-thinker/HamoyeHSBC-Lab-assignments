# Part 1: Function Defination and Invocation

def calculate_average(num1, num2):
    '''Takes two parameters: num1 and num2 and calculate the average of the two numbers.'''
    total = num1 + num2   # Adding the two numbers together amd store the result in the variable total
    average = total/2     # Divide the total by 2 to get their average
    return average
    
print(calculate_average(7, 3))   # Calling the function


# Part 2: Return Values and Variable Assignment

def find_maximum(num1, num2, num3):
    '''Takes three parameters: num1, num2 and num3 and return the maximum value among the three numbers'''
    list_of_num = list((num1, num2, num3))  # casting the two numbers in a list
    return max(list_of_num)               # using max() method to return the maximum number among the three

max_value = find_maximum(20, 50, 100)     # Invoke the function and store the return value in a variable max_value
print(max_value)                          # Display the output


# Part 3: Multiple Functions

def calculate_factorial(num):
    '''Takes a single parameter: num then calculate and return the factorial of the given number'''
    result = 1     # Initiate the result variable with 1 so as to tackle 0!
    for x in range(1,num+1):   # Looping through the range of the given number.
        result *=  x           # Multiply the output of each iteration by the result and also store the output in the result variable as well.
    return result              # return the result after looping through all the ranges of numbers

factorial_result = calculate_factorial(3)   # Calling the function in a variable factorial_result
print(factorial_result)

def calculate_power(base, exponent):
    '''Takes two parameters: base, exponent then calculate and return the result of raising the base to the power of exponent'''
    result = base ** exponent  # calculate the base raise to the power of exponent and store the output in the variable result
    return result              # return the result

power_result = calculate_power(2, 10)   # Invoking the function and store the return value in the varaible power_result
print(power_result)                     # dispaly the output

# Part 4: Recursion


def calculate_fibonacci(n):
    '''The Fibonacci sequence is a series of numbers in which each number is the sum of the two that precede it. Starting at 0 and 1 then 1,2,3,5,
    8,13,21,34 and so on {refers to the fibonacci_sequence function below}. This function will calculate and only return the number at nth term''' 
    if n == 0:    # base condtion that tells the function what to return once n equals 0
        return 0
    elif n == 1:  # base condtion that tells the function what to return once n equals 1
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)  # return the sum of the fibonacci resuslts of the two numbers that precede the
                                                                    # current one.

fibonacci_result = calculate_fibonacci(10)    # calling the function and store the return value in a fibonacci result variable
print(fibonacci_result)                       # display the output



def fibonacci_sequence(n):
    '''The Fibonacci sequence is a series of numbers in which each number is the sum of the two that precede it. Starting at 0 and 1 then 1,2,3,5,
#   8,13,21,34 and so on. This function will calculate and return the sequence with given number of nth term.'''
    sequence = [0,1]    # initiate the sequence list with 0 and 1
    for x in range(1,n):   # looping through the range of 1 and the given parameter n
        series = sequence[x] + sequence[x-1]  # adding the number in the sequence list at indices x and x-1 then store the result in series varable
        sequence.append(series)    # append the value in the series variable at the end of the sequence list
    return sequence    # return the result


sequence_result = fibonacci_sequence(10)   # Invoke the function and store the return value in a variable sequence_result
print(sequence_result)    # display the output

        


# Part 5: 

def is_prime(num):
    '''Takes a parameter: num and return True if the number is prime and False otherwise'''
    if num == 1:   # Exclude 1 from the prime number as many forks used to believe
        return False
    else:
        flag = True  # setting flag to be True
        for x in range(2, num):   # looping through the range of 2 and the given number
            if num % x == 0:    # check if the number modulus x equals 0 (i.e remainder of division operation between the number and x)
                flag = False    # setting flag to be False if the above condition is True
        if flag == False:  # check if the value of the variable flag equals False from the above condition
            return False   # return False if any number in the range of 2 and the number can successfully divide the number without remainder
        else:
            return True    # return True otherwise


for i in range(1,100):  # looping through the range of 1 and 100
    if is_prime(i) == True:  # passing the value of i as a parameter to the function is_prime() and check if its return value equals True
        print(i)     # display the number as the output
    
