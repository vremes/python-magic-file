# python-magic-file
Small Python module to aid developers in getting file extensions from files.

### Purpose
The main motivation behind this package is to easily get the file extension from given file instead of trusting the arbitrary file extension in the filename, for example in a web application which accepts file uploads.


### Usage

Some examples on how to use this module.

#### Get extension from file
```py
from python_magic_file import MagicFile

file_path = 'path/to/file'

with open(file_path 'rb') as f:
    magic_file = MagicFile(f)
    extension = magic_file.get_extension()
```

#### Get extensions from file
```py
from python_magic_file import MagicFile

file_path = 'path/to/file'

with open(file_path 'rb') as f:
    magic_file = MagicFile(f)
    extensions = magic_file.get_extensions()
```

#### Register unknown/non-standard mimetypes

There may be some cases where `get_extension()` emits a following warning:
> UserWarning: File extension for mimetype "video/x-m4v" is None, consider adding an extension for this mimetype using MagicFile.

We have to register file extension using `MagicFile.add_type_to_mimetypes_module` for `video/x-m4v` so `get_extension()` returns the registered extension instead of `None`.

`MagicFile.add_type_to_mimetypes_module` simply just calls `mimetypes.add_type`.

```py
from python_magic_file import MagicFile

# A dictionary of mimetype/extension pairs
new_types = {'video/x-m4v': '.m4v'}

for mimetype, extension in new_types.items():
    MagicFile.add_type_to_mimetypes_module(mimetype, extension)

with open('path/to/m4v-file.m4v', 'rb') as f:
    magic_file = MagicFile(f)
    extension = magic_file.get_extension() # .m4v
```

#### Get human readable name for file

```py
from python_magic_file import MagicFile

file_path = 'path/to/file.txt'

with open(file_path 'rb') as f:
    magic_file = MagicFile(f)
    human_readable_name = magic_file.get_name() # ASCII text, with no line terminators
```

#### Usage with Flask
```py
import os

from flask import Flask, request, abort
from python_magic_file import MagicFile

from werkzeug.utils import secure_filename
from werkzeug.security import safe_join

app = Flask(__name__)

# Allowed extensions for file uplaod
UPLOAD_ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

@app.post('/upload')
def upload_file():
    uploaded_file = request.files.get('file')

    if uploaded_file is None:
        abort(400)

    extension = MagicFile(uploaded_file.stream).get_extension()
    
    if extension not in UPLOAD_ALLOWED_EXTENSIONS:
        abort(400)

    filename, _ = os.path.splitext(secure_filename(uploaded_file.filename))

    save_path = safe_join(os.getcwd(), filename + extension)

    uploaded_file.save(save_path)

    return 'OK'

if __name__ == '__main__':
    app.run()

```
