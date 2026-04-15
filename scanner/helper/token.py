from enum import Enum, auto

class TokenType(Enum):
    EQ = auto()
    GE = auto()
    GT = auto()
    LE = auto()
    LT = auto()
    
    leftParen = auto()
    rightParen = auto()
    leftBrace = auto()
    rightBrace = auto()
    leftBracket = auto()
    rightBracket = auto()

    COMMA = auto()
    DOT = auto()
    COLON = auto()

    LOGIC_AND = auto()
    LOGIC_OR = auto()

    ADDRESS_OF_OPERATOR = auto()

    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    BEGIN = auto()
    END = auto()

    UNFINISHED_STRING = auto()
    STRING = auto()

    INT_TYPE = auto()
    FLOAT_TYPE = auto()
    DOUBLE_TYPE = auto()
    CHAR_TYPE = auto()
    BOOL_TYPE = auto()
    VOID_TYPE = auto()

    plusSign = auto()
    minusSign = auto()
    multSign = auto()
    divSign = auto()
    
    number = auto()
    id = auto()
    
    SPACE = auto()
    NEWLINE = auto()
    EOF = auto()

    UNKNOWN = auto()

nawiasy = [TokenType.leftParen, TokenType.rightParen,
           TokenType.leftBrace, TokenType.rightBrace,
           TokenType.leftBracket, TokenType.rightBracket]

keywords = [TokenType.IF, TokenType.ELSE, TokenType.FOR,
            TokenType.WHILE, TokenType.BEGIN, TokenType.END]

types = [TokenType.INT_TYPE, TokenType.BOOL_TYPE, TokenType.CHAR_TYPE,
         TokenType.VOID_TYPE, TokenType.FLOAT_TYPE, TokenType.DOUBLE_TYPE]

ignore_coloring = [TokenType.SPACE, TokenType.NEWLINE, TokenType.EOF]

class Token:
    def __init__(self, token_type: TokenType, value):
        self.token_type = token_type
        self.value = value

    @staticmethod
    def getColorForType(token_type: TokenType):
        match token_type:
            case TokenType.UNKNOWN | TokenType.UNFINISHED_STRING:
                return "red"
            case type if type in nawiasy:
                return "yellow"
            case type if type in keywords:
                return "magenta"
            case type if type in types:
                return "#2869cb"
            case TokenType.id:
                return "#9cdcfe"
            case TokenType.number:
                return "#5dffa0"
            case TokenType.STRING:
                return "#CC5017"
            case _:
                return "white"

    # string representation for debugging
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"{self.token_type.name, self.value}"