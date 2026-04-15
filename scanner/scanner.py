from helper.functions import file_scanner
class Scanner():
    @staticmethod
    def tokens_from_file(filename):
        return file_scanner(filename)