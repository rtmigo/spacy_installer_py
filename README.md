[![Generic badge](https://img.shields.io/badge/Python-3.6+-blue.svg)](#)
[![Generic badge](https://img.shields.io/badge/Tested_on-Linux%20|%20macOS%20|%20Windows-blue.svg)](#)

# [spacy_installer](https://github.com/rtmigo/spacy_installer_py)

Installing and removing [spaCy](https://spacy.io/) language models from Python 
code, without using the command line.


## Install this package

```bash
$ pip3 install git+https://github.com/rtmigo/spacy_installer_py#egg=spacy_installer
```

## Install spacy model

```python3
import spacy_installer

# load pre-installed model or install and load
model = spacy_installer.load_model('en_core_web_sm')
```

Or, install without loading.

```python3
import spacy_installer

# load pre-installed model or install and load
model = spacy_installer.install_model('en_core_web_sm')
```


## Uninstall spacy models

```python3
import spacy_installer

model = spacy_installer.uninstall_model('en_core_web_sm')
```

Uninstall all models installed by the installer:

```python3
import spacy_installer

model = spacy_installer.uninstall_all_models()
```
