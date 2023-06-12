# Functions

# Function that requests user for input, quits if input equals exit, or runs evaluate_answer method. 
def request_input():
    global word
    word = str(input ("Enter string to test for palindrome or 'exit':"))
    if word == "exit":
        exit()    
    else:
        evaluate_answer()

# Function that evaluates whether user input is a palindrome and prints appropriate response.    
def evaluate_answer():
    reversed_word = word[::-1]
    if word == reversed_word:
        print("palindrome")
    else:
        print("not palindrome")

# Calls request_input function.
x = 1
while (x > 0):
    request_input()