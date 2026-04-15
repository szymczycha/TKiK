from enum import Enum, auto

class TokenType(Enum):
    equalSign = auto()
    
    leftParen = auto()
    rightParen = auto()
    
    plusSign = auto()
    minusSign = auto()
    multSign = auto()
    divSign = auto()
    
    number = auto()
    id = auto()
    
    EOF = auto()

class Token:
    def __init__(self, token_type: TokenType, value):
        self.token_type = token_type
        self.value = value

    # string representation for debugging
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"{self.token_type.name, self.value}"