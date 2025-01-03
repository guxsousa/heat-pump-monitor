
class CustomOpen(object):
    """
    A context manager for opening and closing files.

    Attributes:
        file (file object): The file object that is opened.

    Methods:
        __enter__(): Returns the opened file object.
        __exit__(ctx_type, ctx_value, ctx_traceback): Closes the file.
    """

    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()
