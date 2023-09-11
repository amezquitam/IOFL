
from abc import abstractclassmethod


class Set:

    @abstractclassmethod
    def elements(self) -> set[str]:
        pass

    def union(self, other: 'Set'):
        return self.elements().union(other.elements())
    
    def intersection(self, other: 'Set'):
        return self.elements().intersection(other.elements())

    def diference(self, other: 'Set'):
        return self.elements().difference(other.elements())
