# Part 1: Nested Control Structures

from random import randint   # importing randint from randomm module to generate an integer within a specified range
random_num = randint(1, 10)  # generating an integer within 1-10
guess = 0                    # setting guess to 0 in order to initiate the variable for uninterruted comparison with the variable random_num

while guess != random_num:   # keep requesting for user guess until the user guess is equal to the random number then break
  guess = int(input('Enter your guess (1, 10): '))  # Getting the user guess
  if guess > random_num:     # checking if the user guess is greater than the generated random number
    print('Too high')        # display 'Too high' if the user guess is greater than the generated random number after the comparison
  elif guess < random_num:   # checking if the user guess is less than the generated random number
    print('Too low')         # display 'Too low' if the user guess is less than the generated random number after the comparison
  else:
    print(f'You guess right, the number is: {random_num}')  # Display the number if the user guess is correct



for i in range(1,6):  # creating a range of integers from 1,5
    if i == 2:        # checking if the current value of i is equal to 2
        print(232)    # display 232 if the above condition  is True
    elif i == 3:      # checking if the current value of i is equal to 3
        print(34543)  # display 34543 if the above condition  is True
    elif i == 4:      # checking if the current value of i is equal to 4
        print(4567543) # display 4567543 if the above condition  is True
    elif i == 5:       # checking if the current value of i is equal to 5
        print(567898765) # display 567898765 if the above condition  is True
    else:              # checking if all the conditions stated above are False
        print(1)       # display 1 if all the above conditions  are False



# Part 2: Conditional Expressions

num1 = int(input('Enter an integer: ')) # takes number as an input from the user and convert it an integer datatype
num2 = int(input('Enter another integer: '))   # takes number as an input from the user and convert it an integer datatype
if num1 > num2:  # comparing if num1 is greater than num2
    print('The largest number is: ', num1)   # Display the output if the condition is True
elif num1 < num2:   # comparing if num1 is less than num2
     print('The largest number is: ', num2)   # Display the output if the condition is True
else:     # Checking if the all the above conditions are False
    print('The two numbers are equal to', num1)  # Display this as an output



# 2.

score = int(input('Enter your score: '))   # Getting the score from the user
if score >= 90 and score < 101:   # Checking if the score is in between 90 and 100
    print('Your grade is A')      # Display A if the condition is True
elif score >= 80 and score < 89:  # Checking if the score is in between 80 and 89
    print('Your grade is B')      # Display B if the condition is True
elif score >= 70 and score < 79:  # Checking if the score is in between 70 and 79
    print('Your grade is C')      # Display C if the condition is True
elif score >= 60 and score < 69:  # Checking if the score is in between 60 and 69
    print('Your grade is D')      # Display D if the condition is True
elif score < 60 and score >=0:    # Checking if the score is in between 0 and 59
    print('Your grade is F')      # Display F if the condition is True
else:                             # Check if all the conditions stated above are False
    print('Invalid Score! Your score must be (0-100)')   # Display this as an output



# Part 3: Loop Patterns

size = int(input('Enter your diamond size (odd numbers): '))  # Getting the size of the diamond shape from the user
for x in range(1,size + 1, 2):  # looping through the user's specified size (start = 1[just to not include 0],
                                # stop = size +1[just to include the size itself] and step = 2[just to only return odd numbers])'''
    print(f"{'*' * x : ^{size}s}") # Display * as the current value of x then align the * to the centre, the cap(^) indicate the centre alignment
                                   # and the {size}s {s for string and it is optional though} creating the number of space in which the * should 
                                   # be taken. Overall, this print statement generate the first half of the diamond shape.
for x in range(size-2, 0, -2):     # the same as the first loop but in reverse order
    print(f"{'*' * x : ^{size}s}") # the same as the first print but in the reverse order as well and this generate the second half of the shape.