from helper.token import Token, TokenType

smallLeters = "qwertyuiopasdfghjklzxcvbnm"
bigLetters = smallLeters.upper()
digits = "1234567890"
ignored = " \n"


def matchToken(token):
    # print(f"token: '{token}'")
    if token == "=":
        return Token(TokenType.equalSign, "=")
    if token == "(":
        return Token(TokenType.leftParen, "(")
    if token == ")":
        return Token(TokenType.rightParen, ")")
    if token == "+":
        return Token(TokenType.plusSign, "+")
    if token == "-":
        return Token(TokenType.minusSign, "-")
    if token == "*":
        return Token(TokenType.multSign, "*")
    if token == "/":
        return Token(TokenType.divSign, "/")
    
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


    return None

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
        
        if matchToken(currentToken + peek(f)) == None:
            return matchToken(currentToken)
        
        currChar = f.read(1)
        

def file_scanner(filename):
    
    tokens = []
    with open(filename, "r") as f:

        currentToken = ("Start", "")
        while True:
            currentToken = scan_for_token(f)
            
            if currentToken == None:
                break

            tokens.append(currentToken)
    return tokens