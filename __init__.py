__all__ = ['MagicFile', 'MagicFileException', 'UnreadableFileException', 'NotBinaryFileException', 'NotSeekableFileException']

from .file import MagicFile
from .exceptions import MagicFileException, UnreadableFileException, NotBinaryFileException, NotSeekableFileException
