from typing import List

import lsystem.model.symbol as symbol


__all__ = ['Rule']


class Rule:
    
    
    def __init__(self, left_side: symbol.Symbol, right_side: List[symbol.Symbol]) -> None:
        super().__init__()
        
        is_symbol = [isinstance(x, symbol.Symbol) for x in right_side]
        
        if not isinstance(left_side, symbol.Symbol) or not all(is_symbol):
            raise TypeError('Left and right sight of a rule must consist of Symbol (NonTerminal/Terminal) characters.')
        
        self.left_side = left_side
        self.right_side = right_side
        
        
        
    def is_applicable(self, s: symbol.Symbol) -> bool:
        if not isinstance(s, symbol.Symbol):
            raise TypeError('Symbol is ')
        
        return self.left_side == s
        
        
        
    def __repr__(self) -> str:
        return f'<{self.__module__}.{self.__class__}, {hex(id(self))}>'
    
    
    
    def __str__(self) -> str:
        return f'{self.left_side} -> {"".join(self.right_side)}'
    
    
    
    def __eq__(self, __x: object) -> bool:
        
        if not isinstance(__x, Rule):
            return False
              
        return self.left_side == __x.left_side and self.right_side == __x.right_side
