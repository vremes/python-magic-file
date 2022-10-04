# python-magic-file
Small Python module to aid developers in getting file extensions from files.

### Usage
```py
from magic_file import MagicFile

# HTML file.
with open('path/to/file.html', 'rb') as f:
    magic_file = MagicFile(f)
    print(magic_file.get_extension()) # .html

# File with unknown file extension.
with open('path/to/file.m4v', 'rb') as f:
    magic_file = MagicFile(f)

    # UserWarning: File extension for mimetype "video/x-m4v" is None, consider adding an extension for this mimetype using MagicFile.add_type_to_mimetypes_module or mimetypes.add_type call.
    print(magic_file.get_extension()) # None

# File with unknown file extension
# but the extension is registered manually.
MagicFile.add_type_to_mimetypes_module('video/x-m4v', 'm4v')

with open('path/to/file.m4v', 'rb') as f:
    magic_file = MagicFile(f)
    print(magic_file.get_extension()) # .m4v
```
