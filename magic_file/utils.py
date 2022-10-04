from io import RawIOBase, BufferedIOBase

def is_binary(f) -> bool:
    """Checks if given file object is in binary mode or not."""
    # For file objects.
    if hasattr(f, 'mode'):
        return f.mode == 'rb'

    # For file-like objects without mode attribute.
    if isinstance(f, (RawIOBase, BufferedIOBase)):
        return True

    return False

def is_readable(f) -> bool:
    """Checks if given file object is readable."""
    if hasattr(f, 'readable'):
        return f.readable() is not False
    return False

def is_seekable(f) -> bool:
    """Checks if given file object is seekable."""
    if hasattr(f, 'seekable'):
        return f.seekable() is not False
    return False
