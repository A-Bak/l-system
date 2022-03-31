from __future__ import annotations
from typing import List

import lsystem.model.word as word
import lsystem.model.rule as rule


__all__ = ['Symbol']


class Symbol(str):
    
    
    def __init__(self, character: str) -> None:
        super().__init__()
        
        if not isinstance(character, str):
            raise ValueError('Symbol is not a character (subclass of str).')
        
        self.value = character
        
        
        
    def apply_rule(self, rule: rule.Rule) -> word.Word:
        
        if not self.value == rule.left_side:
            raise ValueError(f'Symbol {self.value} does not match the left side {rule.left_side} of the rule {rule}.')
        
        return rule.right_side
        
        
        
    def __repr__(self) -> str:
        return self.__str__()
    
    
    
    def __str__(self) -> str:
        return self.value
    
    
    
    def __eq__(self, __x: object) -> bool:
        return super().__eq__(__x)
    
    
    
    def __hash__(self) -> int:
        return hash(self.value)
    