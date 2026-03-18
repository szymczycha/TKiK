smallLeters = "qwertyuiopasdfghjklzxcvbnm"
bigLetters = smallLeters.upper()
digits = "1234567890"
ignored = " \n"


def matchToken(token):
    print(f"token: {token}")

    if token == "=":
        return ("equalSign", "=")
    if token == "(":
        return ("leftParen", "(")
    if token == ")":
        return ("rightParen", ")")
    if token == "+":
        return ("plusSign", "+")
    if token == "-":
        return ("minusSign", "-")
    if token == "*":
        return ("multSign", "*")
    if token == "/":
        return ("divSign", "/")
    
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
        return ("number", int(token))
    matchesId = True
    if token[0] in digits:
        matchesId = False
    for char in token:

        if char not in (digits + smallLeters + bigLetters):
            matchesId = False
            break
    if matchesId:
        return ("id", token)


    return None