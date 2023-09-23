# Task1: Declaring and Assigning Variables

name = 'RUsman'  # First initial name + Last name is assigned to the variable name
age = 24  # value 24 is stored in variable age
is_student = True  # Value True (Boolean) Answering the answer to the variable is_student
height = 60  # 60 is stored in variable height

print(name, age, is_student, height, sep = '\n')  # Printing the values of the variables on different line.


# Task2: Working with Numbers

num1 = 45   # assigning 45 to variable num1
num2 = 45.625   # assigning 45.625 to variable num2
sum_result = num1 + num2   # assigning sum of num1 and num2 to the variable sum_result

print("The sum of 45 ad 45.625 is: {}".format(sum_result))  # Display the result of the computation


# Task3: String Manipulation

sentence = 'Programming is sweet when you understand the language and I chose Python because it is easy to understand'  # the string is assign to variable sentence
lower_sentence = sentence.lower()  # converting the variable sentence to lowercase characters
censoring_the_word_understand =lower_sentence.replace('understand', '*****')  # Replacing all the word "understand" with *****

print(sentence)  # Display the original sentence as the output
print(censoring_the_word_understand)  # Display the censoring sentence as the output

#Task4: Working with Boolean Values

is_raining = False   # assigning the boolean False to the variable is_raining
is_sunny = True      # assigning the boolean True to the variable is_sunny
is_windy = False     # assigning the boolean False to the variable is_windy
is_good_weather = is_raining and is_sunny  # assigning the output of it is raining and sunny at the same time to the variable is_good_weather

print(f'This is good weather for me: {is_good_weather}')  # Display the output

# Task5: List Manipulation and Slicing

fruits = ['Mangoes', 'Banana', 'Pineapple', 'Apple', 'Oranges']  # Creating a list of fruits and store it in a variable fruits
print(fruits[:3])  # display the list output
added_fruits = ['Coconut', 'Dates', 'Tangerine']  # Creating an additional list of fruits and store it in a variable added_fruits
fruits.extend(added_fruits)   # adding the added_fruits to the variable fruits using the extend() method
print(fruits)   # Display the output

