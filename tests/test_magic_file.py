import os
import tempfile
import unittest
import mimetypes

from python_magic_file import MagicFile, NotBinaryFileException

class MagicFileTest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(NotBinaryFileException, MagicFile, 'test')

    def test_text_file(self):
        with tempfile.SpooledTemporaryFile() as text_file:
            text_file.write('Hello world'.encode('utf-8'))
            
            magic_file = MagicFile(text_file)

            self.assertEqual(magic_file.get_extension(), '.txt')
            self.assertTrue('.txt' in magic_file.get_extensions())
            self.assertTrue('ASCII text' in magic_file.get_name())

    def test_add_type_to_mimetypes_module(self):
        MagicFile.add_type_to_mimetypes_module('video/x-m4v', '.m4v')
        self.assertTrue('.m4v' in mimetypes.types_map)

    def test_py_file(self):
        py_file_path = os.path.join(os.getcwd(), 'tests', 'test_magic_file.py')
        with open(py_file_path, 'rb') as py_file:
            magic_file = MagicFile(py_file)
            
            self.assertEqual(magic_file.get_extension(), '.py')
            self.assertTrue('.py' in magic_file.get_extensions())
            self.assertTrue('Python script' in magic_file.get_name())

if __name__ == '__main__':
    unittest.main()
