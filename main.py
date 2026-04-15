from scanner.scanner import Scanner
from coloring.colored_syntax_generator import ColoredSyntaxGenerator
print("Filename: ")
filename = input()

tokens = Scanner.tokens_from_file(filename)

print("tokens: ")
print(tokens)

out_filename = "test.html"

ColoredSyntaxGenerator.color_to_html(filename, out_filename)