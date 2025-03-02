from show_pic import show_picture
from prints import print_stats

def options(array: list[str], data: list):
    if array[1] == 's':
        print_stats(array, data)
    if array[1] == 'p':
        show_picture(array[0].lower())
    '''
    if array[1] == '-d': # uma ajuda que diz os nomes dos pokemons de acordo com certos parametros
    '''