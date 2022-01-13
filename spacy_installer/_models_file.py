from pathlib import Path
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


