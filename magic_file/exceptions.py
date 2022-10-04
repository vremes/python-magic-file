class MagicFileException(Exception):
    pass

class UnreadableFileException(MagicFileException):
    pass

class NotBinaryFileException(MagicFileException):
    pass

class NotSeekableFileException(MagicFileException):
    pass
