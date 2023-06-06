# Global variables
word = input("Enter string to test for palindrome or 'exit':")
reversed_word = word[::-1]

# Function that evaluates whether user input is a palindrome and prints appropriate response.    
def evaluate_answer(word,reversed_word):
    if word == reversed_word:
        print("palindrome")
    elif word == "exit":
        print("bye bye")
    else:
        print("not palindrome")

evaluate_answer(word,reversed_word)

# Function that reverses the order of the value word.
# def reverse_word(word):
#     reversed_word = word[::-1]
#     return reversed_word

# Prompts user for input and saves its value as answer.
# answer = input ("Enter string to test for palindrome or 'exit':")
# request_user_input()

# reverse_answer(answer)
# evaluate_answer(answer,result)

# Evaluates whether user's input is a palindrome or not and prints appropriate response.
# if answer == result:
#     print("palindrome")
# else:
#     print("not palindrome")

# print(answer)
# print(answer[::-1])

# print(reverse_answer(answer))

# def reverse(answer):
#     result = ""
#     for i in range(len(text),0,-1):
#         result += text[i-1]
#     return (result) 
#     print(result)  

# palindrome = 

# if answer = 

# user_input_reversed = list(reversed(answer))
# print(user_input_reversed)

# value = user_input_reversed
# if user_input_reversed == answer:
#     result = "palindrome detected"
# print(result)

