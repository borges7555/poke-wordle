from show_pic import show_picture
from prints import print_stats

def options(array: list[str], data: list, tries: int):
    if array[1] in ['s', '-stats']:
        print_stats(array, data)
    if array[1] in ['p', '-picture']:
        show_picture(array[0].lower())
    '''
    if array[1] in ['d', '-dex]: # uma ajuda que diz os nomes dos pokemons de acordo com certos parametros
        if tries > 2:
            print("You can only use this option after you have 2 tries left.")
        else:
    '''
    if array[1] in ['l', '-list']:
        print("")
        for i in data:
            if array[0] in i[0].lower():
                print(i[0])
        print("")