from io import RawIOBase, BufferedIOBase
from tempfile import SpooledTemporaryFile

def is_binary(f) -> bool:
    """Checks if given file object is in binary mode or not."""
    # For file-like objects without mode attribute.
    if isinstance(f, (RawIOBase, BufferedIOBase, SpooledTemporaryFile)):
        return True

    # For file objects.
    if hasattr(f, 'mode'):
        return f.mode == 'rb'

    return False
