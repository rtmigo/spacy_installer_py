import subprocess
import sys

import spacy

from ._models_file import ModelsFile


def install_model(package: str):
    """Устанавливает модель spacy.

    Список возможных моделей: (https://spacy.io/models).

    Пример:
        install_model("en_core_web_sm")
    """
    spacy.cli.download(package)  # type: ignore
    ModelsFile().add(package)


def uninstall_model(package: str):
    """Удаляет ранее установленную модель spacy."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', package, '-y'])
    ModelsFile().remove(package)


def uninstall_all_models():
    """Удаляет все модели spacy, ранее установленные методом `install_model`.
    Названия таких моделей обычно сохранены в файле `ModelsFile`."""
    for package in ModelsFile().read_lines():
        uninstall_model(package)


def load_model(pkg: str):
    """Загружает модель spacy. Если она не установлена - скачивает
    и загружает."""
    try:
        return spacy.load(pkg)
    except OSError:
        install_model(pkg)
        return spacy.load(pkg)
