from scanner.helper.token import Token, TokenType

smallLeters = "qwertyuiopasdfghjklzxcvbnm"
bigLetters = smallLeters.upper()
digits = "1234567890"
ignored = ""


def matchToken(token):
    # print(f"token: '{token}'")
    if token == "=":
        return Token(TokenType.EQ, token)
    if token == "<":
        return Token(TokenType.LT, token)
    if token == "<=":
        return Token(TokenType.LE, token)
    if token == ">":
        return Token(TokenType.GT, token)
    if token == ">=":
        return Token(TokenType.GE, token)
    if token == "(":
        return Token(TokenType.leftParen, "(")
    if token == ")":
        return Token(TokenType.rightParen, ")")
    if token == "{":
        return Token(TokenType.leftBrace, "{")
    if token == "}":
        return Token(TokenType.rightBrace, "}")
    if token == "+":
        return Token(TokenType.plusSign, "+")
    if token == "-":
        return Token(TokenType.minusSign, "-")
    if token == "*":
        return Token(TokenType.multSign, "*")
    if token == "/":
        return Token(TokenType.divSign, "/")
    if token == "\n":
        return Token(TokenType.NEWLINE, "\n")
    if token == " ":
        return Token(TokenType.SPACE, " ")
    if token == ",":
        return Token(TokenType.COMMA, ",")
    if token == ".":
        return Token(TokenType.DOT, ".")
    if token == ";":
        return Token(TokenType.COLON, ";")
    if token == "&&":
        return Token(TokenType.LOGIC_AND, "&&")
    if token == "||":
        return Token(TokenType.LOGIC_OR, "||")
    if token == "&":
        return Token(TokenType.ADDRESS_OF_OPERATOR, "&")
    if token.lower() == "if":
        return Token(TokenType.IF, "if")
    if token.lower() == "else":
        return Token(TokenType.ELSE, "else")
    if token.lower() == "for":
        return Token(TokenType.FOR, "for")
    if token.lower() == "while":
        return Token(TokenType.WHILE, "while")
    if token.lower() == "begin":
        return Token(TokenType.BEGIN, "begin")
    if token.lower() == "end":
        return Token(TokenType.END, "end")
    if token.lower() == "int":
        return Token(TokenType.INT_TYPE, "int")
    if token.lower() == "float":
        return Token(TokenType.FLOAT_TYPE, "float")
    if token.lower() == "double":
        return Token(TokenType.DOUBLE_TYPE, "double")
    if token.lower() == "char":
        return Token(TokenType.CHAR_TYPE, "char")
    if token.lower() == "bool":
        return Token(TokenType.BOOL_TYPE, "bool")
    if token.lower() == "void":
        return Token(TokenType.VOID_TYPE, "void")
    
    if token[0] == '"' and token[-1] != '"' and '"' not in token[1:]:
        return Token(TokenType.UNFINISHED_STRING, token)
    if token[0] == '"' and token[-1] == '"':
        return Token(TokenType.STRING, token)
    
    
    matchesNumber = True
    beforeDot = True
    beforeE = True
    if token[0] not in digits or token[-1] not in digits:
        # not a number
        matchesNumber = False

    for char in token:
        if char not in digits:
            matchesNumber = False
            break
    if matchesNumber:
        return Token(TokenType.number, int(token))
    
    matchesId = True
    if token[0] in digits:
        matchesId = False
    for char in token:

        if char not in (digits + smallLeters + bigLetters):
            matchesId = False
            break
    if matchesId:
        return Token(TokenType.id, token)


    return Token(TokenType.UNKNOWN, token)

def peek(file):
    currentPos = file.tell()
    nextChar = file.read(1)
    file.seek(currentPos)
    return nextChar


def scan_for_token(f):
    currentToken = ""
    currChar = f.read(1)

    while currChar != "":
        # print(currChar, peek(f))
        if currChar in ignored:
            currChar = f.read(1)
            continue
        currentToken += currChar
        if peek(f) == "":
            return matchToken(currentToken)
        
        if matchToken(currentToken + peek(f)).token_type == TokenType.UNKNOWN:
            return matchToken(currentToken)
        
        currChar = f.read(1)

    return Token(TokenType.EOF, "")
        

def file_scanner(filename) -> list[Token]:
    
    tokens = []
    with open(filename, "r") as f:

        currentToken = ("Start", "")
        while True:
            currentToken = scan_for_token(f)
            
            if currentToken.token_type == TokenType.EOF:
                break

            tokens.append(currentToken)
    return tokens