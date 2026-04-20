import sys
from input_processor import input_processor
from command_parser  import command_parser
from validator       import validator
from executor        import execution


# ─── Pipeline ────────────────────────────────────────────────────────────────

command = input("Enter your command: ")

tokens = input_processor(command)
# DEBUG print("tokens:", tokens)

# if no command provided
if not tokens:
    sys.exit("No Command Provided. Ending Execution!")

ir     = command_parser(tokens)
ir     = validator(ir)


# ─── Error Gate ──────────────────────────────────────────────────────────────

if ir.errors:
    if len(ir.errors) > 1:
        print("Errors Encountered!")
        for i, error in enumerate(ir.errors, start=1):
            print(f"  {i}. {error}")
    else:
        print("Error Encountered:", ir.errors[0])
    sys.exit("Ending the Execution!")


# ─── Warnings ────────────────────────────────────────────────────────────────

if ir.warnings:
    if len(ir.warnings) > 1:
        print("Warnings Encountered!")
        for i, warning in enumerate(ir.warnings, start=1):
            print(f"  {i}. {warning}")
    else:
        print("Warning Encountered:", ir.warnings[0])


# ─── Execution ───────────────────────────────────────────────────────────────

execution(ir)
