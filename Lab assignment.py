#ASSIGNMENT-1
#read content from "ABC.txt" line by line and display on the screen:
def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

read_file_line_by_line('ABC.txt')


#Count and display the total number of words in "ABC.txt":
def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        print(f'Total number of words: {len(words)}')

count_words_in_file('ABC.txt')


#Count uppercase characters in "ABC.txt":
def count_uppercase_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()
        uppercase_count = sum(1 for char in text if char.isupper())
        print(f'Total uppercase characters: {uppercase_count}')

count_uppercase_characters('ABC.txt')


#Display words with less than 4 characters from "story.txt":
def display_short_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        short_words = [word for word in words if len(word) < 4]
        print('Words with less than 4 characters:', short_words)

display_short_words('story.txt')



#ASSIGNMENT-2
#Handle ZeroDivisionError:
def handle_zero_division(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f'Result: {result}')

handle_zero_division(10, 0)


#Prompt user to input an integer and raise ValueError for invalid input:
def prompt_integer_input():
    try:
        number = int(input("Enter an integer: "))
        print(f'You entered: {number}')
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

prompt_integer_input()

#Handle FileNotFoundError when opening a file:
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

open_file('non_existent_file.txt')


#Prompt user to input two numbers and raise TypeError if inputs are not numerical:
def prompt_two_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f'You entered: {num1} and {num2}')
    except ValueError:
        print("Error: Please enter valid numerical values.")

prompt_two_numbers()



