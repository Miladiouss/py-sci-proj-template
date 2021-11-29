# Conda

Having a virtual environment and package management is a necessity for running and developing software; it allows for different projects to coexist on the same system without their dependencies interfering with one another. It also allows easy setup from one system to another.
There are many environment and package management solutions out there; venv, pip, conda, poetry are some of the popular options.
In the science community, however, conda tends to be more dominant. For this reason, we recommend installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (the lighter version of Anaconda that does not include any packages).

The Python dependencies are tabulated under `environment.yaml`.
These packages can be broken into the following catagories:

- Core
    - python >=3.8.5,<3.10
    - pip
- Development
    - autopep8 (for automated formatting)
    - flake8 (for styling)
    - alive-progress (progress bar for for loops)
    - click
    - deprecated
- Testing
    - pytest
    - pytest-flake8
    - pytest-openfiles
    - pytest-xdist
- Scientific
    - numpy
    - scipy (modeling, sampling, and more)
    - pandas (use for reading, writing and visualizing tabular data)
    - pyyaml (for reading and writing YAML files, similar to JSON)
- Astronomy Packages
    - astropy (mainly used for physical units)
    - astropy-healpix
    - healpy (for spherical maps)
- Visualization
    - ipykernel
    - plotly (modern alternative to Matplotlib)
    - dash (used by plotly)
    - dash-core-components (used by plotly)
    - dash-html-components (used by plotly)
    - dash-renderer (used by plotly)
    - dash-table (used by plotly)

Under `environment.yaml`, are examples of packages that can only be installed with `pip`. The following example shows two packages that must be installed from GitHub repositories directly:

```yaml
    - pip:
          - git+https://github.com/lsst/daf_butler@main
          - git+https://github.com/lsst/pex_config@main
```
