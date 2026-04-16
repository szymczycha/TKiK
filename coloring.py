from scanner.scanner import Scanner
from coloring.colored_syntax_generator import ColoredSyntaxGenerator
import sys


if len(sys.argv) > 1:
    filename = sys.argv[1]
else: 
    print("Filename: ")
    filename = input()

tokens = Scanner.tokens_from_file(filename)

if len(sys.argv) > 2:
    out_filename = sys.argv[2]
else:
    out_filename = f"{filename}_colored.html"

ColoredSyntaxGenerator.color_to_html(filename, out_filename)