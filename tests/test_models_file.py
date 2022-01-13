import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from spacy_installer._models_file import ModelsFile


class TestModelsFile(unittest.TestCase):
    def test_default_path(self):
        md = ModelsFile()
        self.assertIsNotNone(md.path)

    def test(self):
        with TemporaryDirectory() as tds:
            file = Path(tds) / "temp.txt"
            mf = ModelsFile(file)
            self.assertEqual(mf.read_lines(), [])
            mf.add('a')
            self.assertEqual(mf.read_lines(), ['a'])
            mf.add('line 2')
            mf.add('non unique')
            mf.add('line three')
            mf.add('non unique')
            self.assertEqual(
                mf.read_lines(),
                ['a', 'line 2', 'non unique', 'line three'])
            mf.remove('non unique')
            self.assertEqual(
                mf.read_lines(),
                ['a', 'line 2', 'line three'])