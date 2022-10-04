# python-magic-file
Small Python module to aid developers in getting file extensions from files.

### Purpose
The main motivation behind this package is to easily get the file extension from given file instead of trusting the arbitrary file extension in the filename, for example in a web application which accepts file uploads.

Example code to demonstrate this, using Flask:
```py
import os
from flask import Flask, abort, request
from python_magic_file import MagicFile
from werkzeug.utils import secure_filename
from werkzeug.security import safe_join

app = Flask(__name__)

# Insecure upload route since it blindly trusts user input.
@app.post('/upload')
def upload():
    file = request.files.get('file')

    if file is None:
        abort(400)

    filename, extension = os.path.splitext(
        secure_filename(file.filename.lower())
    )

    if extension not in ('jpg', 'jpeg', 'png'):
        abort(422)

    save_filename = f'{filename}.{extension}'
    save_path = safe_join(os.getcwd(), save_filename)
    file.save(save_path)

    return 'OK'

# More secure way, get_extension calls libmagic under the hood and returns the file extension based on file headers.
@app.post('/upload')
def upload():
    file = request.files.get('file')

    if file is None:
        abort(400)

    filename, _ = os.path.splitext(
        secure_filename(file.filename.lower())
    )

    extension = MagicFile(file.stream).get_extension()

    if extension not in ('.jpg', '.jpeg', '.png'):
        abort(422)

    save_filename = f'{filename}{extension}'
    save_path = safe_join(os.getcwd(), save_filename)
    file.save(save_path)

    return 'OK'
```

### Usage
```py
from python_magic_file import MagicFile

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

### Usage with Flask
```py
from python_magic_file import MagicFile
from flask import Flask, request

app = Flask(__name__)

@app.post('/upload')
def upload_file():
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return 'Missing file from request body!'

    magic_file = MagicFile(uploaded_file.stream)

    file_extension = magic_file.get_extension()

    if not file_extension:
        return 'File extension not supported!'

if __name__ == '__main__':
    app.run()

```
