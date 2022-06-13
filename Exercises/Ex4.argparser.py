# following the documentation on https://docs.python.org/3/howto/argparse.html

# to run it: only keep which script you want to run, delete the rest.
# make sure you give the right arguments in the command line!!

import argparse

parser = argparse.ArgumentParser()
# used to specify which command-line options the program is willing to accept
parser.add_argument("echo", help="echo the string you use here")
# the parse_args() method actually returns some data from the options specified, in this case, echo
args = parser.parse_args()
print(args.echo)


print("OR")


parser = argparse.ArgumentParser()
# argparse treates the options we give it as strings, unless we tell it otherwise
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square ** 2, "is the square of the number you put in")


print("OR")


parser = argparse.ArgumentParser()
# new keyword: action, and we give it the value: store_true
# this means that, if the option is specified, assign the value True to args.verbose
parser.add_argument(
    "-v" "--verbose", help="increase output verbosity", action="store_true"
)
args = parser.parse_args()
if args.verbose:
    print("Verbosity turned on")


print("Now mine:")

parser = argparse.ArgumentParser()
parser.add_argument(
    "--hi",
    "--hello",
    help="Displays a greeting in a few different languages",
    action="store_true",
)
args = parser.parse_args()
if args.hi:
    print("Hello, Hallo, Bonjour, 你好, Hola, Namaste, Ahoj, Guten Tag, 안녕하세요, Hej !")
