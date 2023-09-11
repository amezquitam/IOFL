from Alphabet import Alphabet, SymbolTooLong
from Language import Language
from time import sleep
from abc import abstractclassmethod


class Function:

    @property
    def message(self) -> str:
        raise NotImplementedError()

    @abstractclassmethod
    def action(self) -> None:
        raise NotImplementedError()


class DefineAlphabet(Function):
    def __init__(self, alphabets: dict[str, Alphabet]):
        self.alphabets = alphabets

    @property
    def message(self):
        return 'Define new alphabets'

    # context: required data for realize actions
    def action(self):
        print('Instructions: Write " A = {a, b, c} " to define the A alphabet')
        print('              You can write various separed by semicolons ";".')
        user_entry = input('> ')
        user_entry_with_no_spaces = user_entry.replace(' ', '', -1)
        alphabets_entry = user_entry_with_no_spaces.split(';')

        there_errors = False

        for alphabet_entry in alphabets_entry:
            alphabet_name, alphabet_set_entry = alphabet_entry.split('=')
            alphabet_symbols = set(alphabet_set_entry.strip('{}').split(','))
            try:
                self.alphabets[alphabet_name] = Alphabet(alphabet_name, alphabet_symbols)
            except SymbolTooLong:
                there_errors = True
                print(f'error: Cannot add {alphabet_name} because contains symbols with more than a letter')
        
        if there_errors:
            sleep(2.5) # in seconds


class GetAlphabets(Function):
    def __init__(self, alphabets: dict[str, Alphabet]):
        self.alphabets = alphabets
    
    @property
    def message(self):
        return 'Show all defined alphabets'

    def action(self):
        print(' - Defined alphabets -')
        for alphabet in self.alphabets.values():
            print(f'{alphabet.name}: {alphabet.symbols}')
        input('press enter to continue...')
        

class DefineLanguage(Function):
    def __init__(self, alphabets: dict[str, Alphabet], languages: dict[str, Language]):
        self.alphabets = alphabets
        self.languages = languages

    @property
    def message(self):
        return 'Define new languajes'

    def action(self):
        print('Instructions: Write the name of the language(s) followed by ')
        print('              the equal sign, the name of the alphabet, ')
        print('              add a comma and the number of words to generate')
        print('              Example: " L = A, 9 "')
        print('                       " M = A, 7; N = B, 6 "')
        user_entry = input('> ')

        user_entry_with_no_spaces = user_entry.replace(' ', '', -1)
        languages_entry = user_entry_with_no_spaces.split(';')

        for language_entry in languages_entry:
            language_name, language_args = language_entry.split('=')
            alphabet_name, words_count_entry = language_args.split(',')

            try:
                words_count = int(words_count_entry)
            except:
                print(' -   invalid number  -   ')
                sleep(1.5) # in seconds
                return

            alphabet = self.alphabets.get(alphabet_name)
            if alphabet == None:
                print(f' -   undefined alphabet: ({alphabet_name})  -   ')
                sleep(1.5) # in seconds
                return

            self.languages[language_name] = Language(alphabet_name, alphabet, words_count)
        

class GetLanguages(Function):
    def __init__(self, languages: dict[str, Language]):
        self.languages = languages
    
    @property
    def message(self):
        return 'Show all defined languages'
    
    def action(self):
        print(' - Defined languages -')
        for language in self.languages.values():
            print(f'{language.name}: {language.words}')
        input('press enter to continue...')
        
