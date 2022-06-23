print("Let's play a simple game of hide and seek!")
print("Can you find the 'ME.py' file using the find command in this directory?")

x = input("> ")

if x == "find . -name 'ME.py' -print":
    print("You found it!")
else:
    print("Didn't find it.")
