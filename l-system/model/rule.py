



class Symbol(str):
    
    
    def __init__(self, left_side: str, right_side: str) -> None:
        super().__init__()
        
        if not (isinstance(left_side, str) and isinstance(right_side, str)):
            raise ValueError('Symbol is not a character (subclass of str).')
        
        self.left_side = left_side
        self.right_side = right_side
        
        
        
    def __repr__(self) -> str:
        return f'<{self.__module__}.{self.__class__}, {hex(id(self))}>'
    
    
    
    def __str__(self) -> str:
        return f'{self.left_side} -> {self.right_side}'
    
    
    
    def __eq__(self, __x: object) -> bool:
        
        if not isinstance(__x, Symbol):
            return False
        
        return self.left_side == __x.left_side and self.right_side == __x.right_side