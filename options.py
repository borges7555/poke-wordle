from show_pic import show_picture
from prints import print_stats

def options(array: list[str], data: list):
    if array[1] in ['s', '-stats']:
        print_stats(array, data)
    if array[1] in ['p', '-picture']:
        show_picture(array[0].lower())
    '''
    if array[1] in ['d', '-dex]: # uma ajuda que diz os nomes dos pokemons de acordo com certos parametros
    
    if array[1] in ['l', '-list']: # lista os pokemons que contêm a string array[0]
    '''