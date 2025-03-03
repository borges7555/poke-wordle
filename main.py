from choose_gens import choose_generations
from game import game
from prints import help

def main() -> int:
    print("Welcome to the Pokemon Wordle!")
    print("Type 'help' for instructions, 'exit' to leave or press 'Enter' to start the game.")
    aux = input()

    if aux == 'help':
        help()
        print("If you want to see this again, type 'help'.")
        print("Press 'Enter' to start the game.")
        input()
    elif aux == 'exit':
        return 0

    print("Choose the generations you want the pokemon to be from (1-9): ")
    gens = choose_generations()
    if gens == [0, 0]:
        return 0
    else:
        game(gens)
        
    return 0


if __name__ == "__main__":
    main()