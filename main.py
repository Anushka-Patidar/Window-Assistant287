import sys
# importing the modules parts of the file
from input_processor import input_processor
from command_parser import command_parser
from validator import validator
from executor import execution



# taking in user input
command = input("Enter your command: ")

# input processing
tokens = input_processor(command)
print("Tokens generated: ", tokens)



# parsing through the tokens and producing an intermediate representation
ir = command_parser(tokens)
print("The CommandIR:\n", ir)

# validating the ir
ir = validator(ir)
print("Validated CommandIR is:", ir)



# reporting errors and stopping execution
# no errors
if not ir.errors:       # empty list
    pass        # out of conditional
# errors present: FATAL
else:
    if len(ir.errors) > 1:
        print("Errors Encountered!")
        for i, error in enumerate(ir.errors, start=1):
            print(str(i) + ".", error)
    else:
        print("Error Encountered:", ir.errors[0])
    sys.exit("Ending the Execution!")


# providing warnings
# no warnings generated
if not ir.warnings:   # empty list
    pass        # out of the conditional
# warnings present
else:
    if len(ir.warnings) > 1:
        print("Warnings Encountered!")
        for i, warning in enumerate(ir.warnings, start=1):
            print(str(i) + ".", warning)
    else:
        print("Warning Encountered:", ir.warnings[0])
    



# executing the command
execution(ir)