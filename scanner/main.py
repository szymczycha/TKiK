from helper.functions import scanner
print("Filename: ")
filename = input()

tokens = []
with open(filename, "r") as f:

    currentToken = ("Start", "")
    while True:
        currentToken = scanner(f)
        
        if currentToken == None:
            break

        tokens.append(currentToken)

print("tokens: ")
print(tokens)
