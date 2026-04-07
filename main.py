from input_processor import input_processor
from command_parser import command_parser
from validator import validator

# taking in user input
command = input("Enter your command: ")

# input processing
tokens = input_processor(command)
# print("Tokens generated: ", tokens)

# parsing through the tokens and producing an intermediate representation
ir = command_parser(tokens)
# print("The output is as follows:\n", ir)

# validating the ir
ir = validator(ir)
# print("Validated ir is:", ir)

# error correction
if not ir.errors:   # empty list
    # warning correction
    if not ir.warnings:   # empty list
        pass # call executor
    else:
        if len(ir.warnings) > 1:
            print("Warnings Encountered!")
            for i, warning in enumerate(ir.warnings, start=1):
                print(str(i) + ".", warning)
        else:
            print("Warning Encountered:", ir.warnings[0])
    
    # call executor
else:
    if len(ir.errors) > 1:
        print("Error Encountered!")
        for i, error in enumerate(ir.errors, start=1):
            print(str(i) + ".", error)
    else:
        print("Error Encountered:", ir.errors[0])