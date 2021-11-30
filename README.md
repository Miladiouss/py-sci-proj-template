# Python Science Project Template

This is an example of a (mainly) Python repository that can be used for scientific software development.

## GitHub Actions

Coding standards are based on Rubin:
<https://developer.lsst.io/python/style.html>
`.github/workflows/run_flake8.yaml` is the GitHub action responsible for enforcing coding standards.
`.github/workflows/run_pytest.yaml` is the GitHub action for running unit tests.
`scripts/run-integration-test.sh` runs integration tests.

## Installation

```sh
git clone https://github.com/Miladiouss/py-sci-proj-template.git
conda env create --name sci-proj-dev --file conda/environment.yaml
conda activate sci-proj-dev
pip install -e .
```

## Useful Information

You can find more information under `docs/`:

- [Git and GitHub routines for version control](docs/Git%20Rutines.md)
- [Set up VS Code](docs/Visual%20Studio%20Code%20Setup.md)

## Authors

- Tatiana Goldina at Caltech > IPAC
- Milad Pourrahmani at Caltech > IPAC
