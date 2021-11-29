# Project Parameters

Scientific projects often depend on a number of parameters. These could be properties of an instrument, physical constants, or configurable parameters used for running computational experiments.
Throughout the life of a project, these parameters and requirements will constantly change. Separating these parameters from the programming logic is considered good practice for the following two reasons:

1. Tracking changes through version control becomes more clear.
2. Exporting parameters for different experiment runs becomes a matter of copying the file containing these parameters.

The YAML file format is the human-readable solution for storing such parameter data structures, an alternative to JSON or even CSV files depending on the circumstance. Consider looking at `Parameters.yaml` file as an example. `pyyaml` library is a convenient way to import such data structures as a Python dictionary. The `dict2obj.py` module can convert this (potentially nested) dictionary to a Python object since an object oriented representation is more human-readable:

```py
# data structured as a dictionary:
data['camera']['lens']['aperture']
```

```py
# data structured as attributes of an object:
data.camera.lens.aperture
```

For the object oriented representation to be possible, the YAML keys cannot contain whitespace.

`__init__.py` file makes these parameters available as an importable Python object where the developer has the opportunity to only make the relevant parameters available and assign preferred variable names. As shown in this file, it is best to explicitly list all the used parameters to let the user see the list of available variable with the help of their IDE autocompletion or recommendation system.
