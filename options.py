from show_pic import show_picture
from prints import print_stats

def options(array: list[str], data: list):
    if array[1] in ['s', '-stats']:
        print_stats(array, data)
    if array[1] in ['p', '-picture']:
        show_picture(array[0].lower())
    if array[1] in ['l', '-list']:
        print("")
        for i in data:
            if array[0] in i[0].lower():
                print(i[0])
        print("")


def dex(data: list, guessed_right: list):
    print("")
    for pokemon in data:
        name, type1, type2, generation = pokemon[0], pokemon[1], pokemon[2], pokemon[3]
        if guessed_right[2] != 0:
            if generation == guessed_right[2]:
                if (type1 == guessed_right[0] or guessed_right[0] == "") and (type2 == guessed_right[1] or guessed_right[1] == ""):
                    print(name)
        else:
            if (type1 == guessed_right[0] or guessed_right[0] == "") and (type2 == guessed_right[1] or guessed_right[1] == ""):
                print(name)
    print("")