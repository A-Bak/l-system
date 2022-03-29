from __future__ import annotations
from typing import List

from .rule import Rule




class Symbol(str):
    
    
    def __init__(self, character: str) -> None:
        super().__init__()
        
        if not isinstance(character, str):
            raise ValueError('Symbol is not a character (subclass of str).')
        
        self.value = character
        
        
        
    def apply_rule(self, rule: Rule) -> List[Symbol]:
        
        if not self.value == rule.left_side:
            raise ValueError(f'Symbol {self.value} does not match the left side {rule.left_side} of the rule {rule}.')
        
        return rule.right_side
        
        
    def __repr__(self) -> str:
        return self.__str__()
    
    
    
    def __str__(self) -> str:
        return self.value
    
    
    
    def __eq__(self, __x: object) -> bool:
        return super().__eq__(__x)
    
    