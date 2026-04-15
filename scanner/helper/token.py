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
    

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value