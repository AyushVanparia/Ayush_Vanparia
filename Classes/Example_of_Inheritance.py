class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("File is already close")
        self.opened = False


class FileStream(Stream):

    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):

    def read(self):
        print("Reading data from Network")


fs = FileStream()
fs.open()
fs.read()
fs.close()
