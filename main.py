from choose_gens import choose_generations
from game import game
from prints import help
import sys

def main() -> int:
    print("Welcome to the Pokemon Wordle!")
    print("Type 'help' for instructions, 'exit' to leave or press 'Enter' to start the game.")
    aux = input()

    while aux != 'help' and aux != 'exit' and aux != '':
        print("\nInvalid input. Try again.")
        aux = input()
        
    if aux == 'help':
        help()
        print("If you want to see this again, type 'help'.")
        print("Press 'Enter' to start the game.")
        input()
    elif aux == 'exit':
        sys.exit(1)
        
    play_again = True
    while play_again:
        print("Choose the generations you want the pokemon to be from (1-9): ")
        gens = choose_generations()
        if gens == [0, 0]:
            return 0
        else:
            game(gens)

        print("Do you want to play again? (y/n)")
        aux = input()
        while aux != 'y' and aux != 'n':
            print("\nInvalid input. Try again.")
            aux = input()

        if aux == 'n':
            play_again = False
        
    return 0


if __name__ == "__main__":
    main()