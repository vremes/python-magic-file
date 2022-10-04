from os import SEEK_SET
from typing import Union
from warnings import warn
from mimetypes import guess_extension, add_type, guess_all_extensions

from magic import from_buffer

from .utils import is_binary
from .exceptions import NotBinaryFileException

class MagicFile:
    """Class for extracting file extension from given file."""
    def __init__(self, file_like_object) -> None:
        # Check if file is open in binary mode
        # as it is required for accurate results
        if is_binary(file_like_object) is False:
            raise NotBinaryFileException(f'File {file_like_object} is not in binary mode.')

        self._file_like_object = file_like_object

    def get_extension(self, buffer: int = 2048) -> Union[str, None]:
        """Returns the file extension or None."""
        mime = self._mime_from_buffer(buffer)
        extension = guess_extension(mime)
        if not extension:
            warn(f'File extension for mimetype "{mime}" is None, consider adding an extension for this mimetype using MagicFile.add_type_to_mimetypes_module or mimetypes.add_type call.')
        return extension

    def get_extensions(self, buffer: int = 2048) -> list:
        """Returns a list of file extensions."""
        mime = self._mime_from_buffer(buffer)
        extensions = guess_all_extensions(mime)
        if not extensions:
            warn(f'File extension list for mimetype "{mime}" is empty, consider adding an extension for this mimetype using MagicFile.add_type_to_mimetypes_module or mimetypes.add_type call.')
        return extensions

    def _mime_from_buffer(self, buffer: int = 2048, mime: bool = True) -> str:
        """Returns mimetype from buffer."""
        self._file_like_object.seek(SEEK_SET)
        mime = from_buffer(self._file_like_object.read(buffer), mime)
        self._file_like_object.seek(SEEK_SET)
        return mime

    @staticmethod
    def add_type_to_mimetypes_module(type: str, extension: str):
        """Adds given type and extension to mimetypes module."""
        return add_type(type, extension)
