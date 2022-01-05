class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File is already open")
        self.open = True
        print("opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("File is already close")
        self.opened = False
        print("closed")


class FileStream(Stream):

    def read():
        print("Reading data from file")


class NetworkStream(Stream):

    def read():
        print("Reading data from Network")
