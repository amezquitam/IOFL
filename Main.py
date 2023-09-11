from Alphabet import Alphabet
from Language import Language
from Functions import *
from os import system
from time import sleep


def main():
    alphabets: dict[str, Alphabet] = {}
    languages: dict[str, Language] = {}
    should_exit = False

    functions: list[Function] = [
        DefineAlphabet(alphabets),
        DefineLanguage(alphabets, languages),
        GetAlphabets(alphabets),
        GetLanguages(languages),
    ]

    while not should_exit:
        system('cls')
        print(' - Choose an action  -   ')

        for idx, function in enumerate(functions, 1):
            print(f'{idx}. {function.message}')
        
        try:
            action_index = int(input('> ')) - 1
        except:
            print(' -   Invalid entry   -   ')
            sleep(1.5) # in seconds
            continue
        
        try:
            functions[action_index].action()
        except:
            print('Error at realize the operation')
            sleep(1.5)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)