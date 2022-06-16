import argparse

print("Type --[animal of choice] to get some info on them!")

parser = argparse.ArgumentParser()

# cat
parser.add_argument(
    "--cat",
    help="displays info on cats",
    action="store_true",
)
# dog
parser.add_argument(
    "--dog",
    help="displays info on dogs",
    action="store_true",
)
# rabbit
parser.add_argument(
    "--rabbit",
    "--bunny",
    help="displays info on rabbits and bunnies",
    action="store_true",
)
# bird
parser.add_argument(
    "--bird",
    help="displays info on birds",
    action="store_true",
)
# hamster
parser.add_argument(
    "--hamster",
    help="displays info on hamsters",
    action="store_true",
)
# raccoon
parser.add_argument(
    "--raccoon",
    help="displays info on raccoons",
    action="store_true",
)
# gorilla
parser.add_argument(
    "--gorilla",
    help="displays info on gorillas",
    action="store_true",
)
# python
parser.add_argument(
    "--python",
    "--snake",
    help="displays info on pythons",
    action="store_true",
)
# squirrel
parser.add_argument(
    "--squirrel",
    help="displays info on squirells",
    action="store_true",
)
# horse
parser.add_argument(
    "--horse",
    help="displays info on horses",
    action="store_true",
)
# panda
parser.add_argument(
    "--panda",
    help="displays info on pandas",
    action="store_true",
)
# tiger
parser.add_argument(
    "--tiger",
    help="displays info on tigers",
    action="store_true",
)
# wolf
parser.add_argument(
    "--wolf",
    help="displays info on wolves",
    action="store_true",
)
# koala
parser.add_argument(
    "--koala",
    help="displays info on koalas",
    action="store_true",
)
# firefox
parser.add_argument(
    "--firefox",
    help="displays info on red pandas",
    action="store_true",
)
# shark
parser.add_argument(
    "--shark",
    help="displays info on sharks",
    action="store_true",
)
# dinosaur
parser.add_argument(
    "--dinosaur",
    help="displays info on dinosaurs",
    action="store_true",
)
# giraffe
parser.add_argument(
    "--giraffe",
    help="displays info on giraffes",
    action="store_true",
)
# fish
parser.add_argument(
    "--fish",
    help="displays info on fishes",
    action="store_true",
)

args = parser.parse_args()
if args.cat:
    print("Cats always land on their feet!")
if args.dog:
    print("Dogs are the perfect, loyal companions!")
if args.rabbit:
    print("they have large ears :)")
if args.bird:
    print("They can fly!")
if args.hamster:
    print("hamter")
if args.raccoon:
    print("trash goblins")
if args.gorilla:
    print("Haramber :(")
if args.python:
    print("ssssssnek")
if args.squirrel:
    print("phat gus :)")
if args.horse:
    print("They are usually quite large!")
if args.panda:
    print("They eat bamboo")
if args.tiger:
    print("They meow, just like cats!")
if args.wolf:
    print("Wolves are larger than you think they would be")
if args.koala:
    print("Sleep. Eat. Repeat.")
if args.firefox:
    print("They are sooooo cute")
if args.shark:
    print("sharp teeth!")
if args.dinosaur:
    print("They are extinct")
if args.giraffe:
    print("They have a very loooong neck")
if args.fish:
    print("blub blub blub lbub :)))))")
