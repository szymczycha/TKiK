from helper.functions import matchToken, ignored
print("Filename: ")
filename = input()

tokens = []
with open(filename, "r") as f:

    currentToken = ""
    nextChar = f.read(1)
    while nextChar != "":
        if nextChar in ignored:
            nextChar = f.read(1)
            continue
        currentToken += nextChar
        if matchToken(currentToken) == None:
            tokens.append(matchToken(currentToken[:-1]))
            currentToken = nextChar
        
        nextChar = f.read(1)
    
    tokens.append(matchToken(currentToken))

print("tokens: ")
print(tokens)
