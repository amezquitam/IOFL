
from Set import Set


class SymbolTooLong(Exception): pass


class Alphabet(Set):

    def __init__(self, name: str, symbols: set[str]):
        # ensure thar every single string in the set is a character
        for symbol in symbols:
            if len(symbol) != 1:
                raise SymbolTooLong()
    
        self._name = name
        self._symbols = symbols
    
    @property
    def name(self):
        return self._name

    @property
    def symbols(self):
        return self._symbols
    
    def elements(self):
        return self.symbols
