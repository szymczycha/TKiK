from helper.functions import file_scanner
print("Filename: ")
filename = input()

tokens = file_scanner(filename)

print("tokens: ")
print(tokens)
