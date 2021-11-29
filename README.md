# Python Science Project Template

This is an example of a (mainly) Python repository that can be used for scientific software development.

## Guides

- [Storing and importing project parameters](py_src/param/README.md)
- [Virtual environments and package management in Python for scientific projects](conda/README.md)
- [Git Routines](docs/Git%20Routines.md)
- [VS Code set up: recommended extensions and settings](docs/Visual%20Studio%20Code%20Setup.md)
- [Basics of Python packaging](py_src/README.md)
- [Python Scripts vs Python Packages](scripts/README.md)
- [Atoms of a data pipeline: an introduction to pipeline tasks](py_src/tasks/README.md)
- [Unit tests](tests/README.md)

## GitHub

### Actions

Github actions run on every push and they ensure that all coding standards are met and all tests passed.

- Coding standards are based on Rubin: <https://developer.lsst.io/python/style.html>
    - `.github/workflows/run_flake8.yaml` is the GitHub action responsible for enforcing coding standards.
    - `.github/workflows/run_pytest.yaml` is the GitHub action for running unit tests.
- `scripts/run-integration-test.sh` is responsible for running integration tests.

### Use git for code only, not for data

`git` and GitHub are only intended to version control source code (text files). Do not version control `*.jpeg` or `*.png` images, `*.pdf` documents, or data that constantly changes and is only machine-readable; it would significantly slow down `git` and would use limited GitHub resources. In such circumstances, ignore non-textual files under [`.gitignore`](.gitignore) or use [`git lfs`](https://git-lfs.github.com/).

## Installation

```sh
git clone https://github.com/Miladiouss/py-sci-proj-template.git
conda env create --name sci-proj-dev --file conda/environment.yaml
conda activate sci-proj-dev
pip install -e .
```

The above are the instructions for cloning this repository, setting up a conda environment from [conda/environment.yaml](conda/environment.yaml), and installing the packages under [`py_src`](py_src/). The conda environment also includes [`scripts`](scripts/) dependencies (in addition to the packaging requirements) while pure packaging requirements (excluding the script dependencies) are listed under [`setup.cfg`](setup.cfg). The [`setup.cfg`](setup.cfg) file also includes packaging information, styling guidelines, package data, testing requirements and more. Python packaging is rapidly evolving at the time of this writing. At the time of this writing, Python packaging is rapidly evolving and at the moment it is recommended that `setup.py` would remain as simple as possible while tabulating the setup requirements using a `setup.cfg` file.

## Authors

- Tatiana Goldina at Caltech > IPAC
- Milad Pourrahmani at Caltech > IPAC
