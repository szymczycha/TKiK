from scanner.scanner import Scanner
from scanner.helper.token import Token, TokenType
class ColoredSyntaxGenerator():
    @staticmethod
    def color_to_html(filename, out_filename):
        tokens = Scanner.tokens_from_file(filename)
        out = """<!doctype html><html lang="pl"><body style=\"white-space:pre;background-color: #333333;font-family: Consolas;\">"""

        for token in tokens:
            if token.token_type == TokenType.NEWLINE:
                out += "<br/>"
                continue
            out += f"""<span style=\"color:{Token.getColorForType(token.token_type)};\">{token.value}</span>"""

        out += """</body></html>"""
        with open(out_filename, "w") as out_file:
            out_file.write(out)