from input_processor import input_processor

# taking in user input
command = input("Enter your command: ")

# input processing
tokens = input_processor(command)

# checking output
print("The output is as follows:\n", tokens)