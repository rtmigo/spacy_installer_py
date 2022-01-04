import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Optional, List


class ModelsFile:
    """Сохраняет в виде строк имена установленных пакетов spacy.

    Содержимое будет чем-то вроде:
    ```
        en_core_web_sm
        fr_core_news_sm
        es_core_news_sm
        de_core_news_sm
    ```
    """

    def __init__(self, path: Optional[Path] = None):
        if path is None:
            path = Path(__file__).parent / ".spacy_models.txt"
        self.path = path

    def write_lines(self, lines: List[str]):
        self.path.write_text('\n'.join(lines))

    def read_lines(self) -> List[str]:
        try:
            text = self.path.read_text()
        except FileNotFoundError:
            text = ""
        return text.splitlines()

    def add(self, package: str):
        if '\n' in package:
            raise ValueError(package)
        lines = self.read_lines()
        if not package in lines:
            lines.append(package)
            self.write_lines(lines)

    def remove(self, line: str):
        self.write_lines([l for l in self.read_lines() if l != line])


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
