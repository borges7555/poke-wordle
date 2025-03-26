from show_pic import show_picture
from prints import print_stats

def options(array: list[str], data: list):
    if array[1] in ['s', '-stats']:
        print_stats(array[0], data)
        print("")
    elif array[1] in ['p', '-picture']:
        show_picture(array[0].lower())
    elif array[1] in ['l', '-list']:
        print("")
        for i in data:
            if array[0] in i[0].lower():
                print(i[0])
        print("")
    else:
        print("\nInvalid option.")


def dex(data: list, guessed_right: list, guessed_wrong_types: list, guessed_wrong_gens: list):
    print("")
    for pokemon in data:
        name, type1, type2, generation = pokemon[0], pokemon[1], pokemon[2], pokemon[3]
        if guessed_right[2] != 0:
            if generation == guessed_right[2]:
                if (type1 == guessed_right[0] or guessed_right[0] == "") and (type2 == guessed_right[1] or guessed_right[1] == "") and type1 not in guessed_wrong_types and type2 not in guessed_wrong_types:
                    print(name)
        else:
            if (type1 == guessed_right[0] or guessed_right[0] == "") and (type2 == guessed_right[1] or guessed_right[1] == "") and type1 not in guessed_wrong_types and type2 not in guessed_wrong_types and generation not in guessed_wrong_gens:
                print(name)
    print("")