from typing import List, Set

import lsystem.model.symbol as symbol
import lsystem.model.alphabet as alphabet


class Word():
    
    def __init__(self, symbols: List[symbol.Symbo]) -> None:
        
        if not all(map(lambda x: isinstance(x, symbol.Symbol), symbols)):
            raise ValueError('Not a symbol. Word must consist of a List[Symbol].')
        
        self.symbols = symbols
    
    
    
    def in_alphabet(self, alphabet: alphabet.Alphabet) -> bool:
        
        for s in self.symbols:
            if s not in alphabet:
                return False
            
        return True
    
    
    
    def __repr__(self) -> str:
        return self.__str__()
    
    
    
    def __str__(self) -> str:
        return self.value
    
    
    
    def __eq__(self, __x: object) -> bool:
        return super().__eq__(__x)
    
    
    
    def __hash__(self) -> int:
        return hash(self.value)