# following the documentation on https://docs.python.org/3/howto/argparse.html

# to run it: only keep which script you want to run, delete the rest.
# make sure you give the right arguments in the command line!!

import argparse

print("type 'python3 Ex4.argsparser.py --help for information'")

# general languages
parser = argparse.ArgumentParser()
parser.add_argument(
    "--hi",
    "--hello",
    help="Displays a greeting in a few different languages",
    action="store_true",
)

# english
parser.add_argument(
    "--hienglish",
    "--helloenglish",
    help="Displays a greeting in English",
    action="store_true",
)

# dutch
parser.add_argument(
    "--hidutch",
    "--hellodutch",
    help="Displays a greeting in Dutch",
    action="store_true",
)

# french
parser.add_argument(
    "--hifrench",
    "--hellofrench",
    help="Displays a greeting in French",
    action="store_true",
)

# chinese
parser.add_argument(
    "--hichinese",
    "--hellochinese",
    help="Displays a greeting in Chinese",
    action="store_true",
)

# spanish
parser.add_argument(
    "--hispanish",
    "--hellospanish",
    help="Displays a greeting in Spanish",
    action="store_true",
)

# hindi
parser.add_argument(
    "--hihindi",
    "--hellohindi",
    help="Displays a greeting in Hindi",
    action="store_true",
)

# korean
parser.add_argument(
    "--hikorean",
    "--hellokorean",
    help="Displays a greeting in Korean",
    action="store_true",
)

# swedish
parser.add_argument(
    "--hiswedish",
    "--helloswedish",
    help="Displays a greeting in Swedish",
    action="store_true",
)

# swedishfish
parser.add_argument(
    "--hiswedishfish",
    "--helloswedishfish",
    help="Displays a greeting in Swedish. A lot of times",
    action="store_true",
)

args = parser.parse_args()
if args.hi:
    print("Hello, Hallo, Bonjour, 你好, Hola, Namaste, 안녕하세요, Hej !")
elif args.hienglish:
    print("Hello!")
elif args.hidutch:
    print("Hallo!")
elif args.hifrench:
    print("Bonjour!")
elif args.hichinese:
    print("你好!")
elif args.hispanish:
    print("Hola!")
elif args.hihindi:
    print("Namaste!")
elif args.hikorean:
    print("안녕하세요!")
elif args.hiswedish:
    print("Hej!")
elif args.hiswedishfish:
    print(
        "Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej! Hej!"
    )
