# [spacy_installer](https://github.com/rtmigo/spacy_installer_py)

Experimental code for automating installing and uninstalling spacy models 
directly from the code (without using the command line).

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
