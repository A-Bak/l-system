import lsystem.model.symbol as symbol


__all__ = ['Alphabet']


class Alphabet(set):
    
    
    def __init__(self) -> None:
        super().__init__()