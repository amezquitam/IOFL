from Alphabet import Alphabet
from Set import Set
from random import randint


class Language(Set):
    def __init__(self, name: str, alphabet: Alphabet, num_of_words: int) -> None:
        self._name = name
        self._alphabet = alphabet
        self._words: set[str] = set()

        symbol_count = len(alphabet.symbols) - 1
        symbols = list(alphabet.symbols)

        while len(self._words) < num_of_words:
            word_len = randint(2, 10)
            word = ''
            for _ in range(word_len):
                random_symbol = symbols[randint(0, symbol_count)]
                word += random_symbol
            self._words.add(word)
    
    @property
    def words(self):
        return self._words

    @property
    def alphabet(self):
        return self._alphabet
    
    @property
    def name(self):
        return self._name

    def elements(self):
        return self.words
