from input_processor import input_processor
from command_parser import command_parser

# taking in user input
command = input("Enter your command: ")

# input processing
tokens = input_processor(command)
print("Tokens generated: ", tokens)

# parsing through the tokens and producing an intermediate representation
ir = command_parser(tokens)
print("The output is as follows:\n", ir)