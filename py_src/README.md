# About This Python project

The `py_src` directory contains subdirectories which will act as Python modules.
Each Python module must contain an `__init__.py` file.
for instance, this project contains two module with their own submodules:

- py_src
    - data_obj
        - data
        - utils
    - param
    - tasks
        - task1

The `__init__.py` must import the contents of its submodules. As an example, the `data_obj` module achieves this as follows:

```py
from .data import *
from .utils import *
```

There are alternative ways to package a Python project (see [this article](https://towardsdatascience.com/whats-init-for-me-d70a312da583)). This is the most common way with one caveat: no two imported objects can have the same name. To address this, it is important to keep the namespace clean by explicitly declaring which objects a submodule is exporting:

```py
__all__ = ['identity']
```

This will also improve the user experience by clarifying which entities are meant to be used by the users and which ones are the internal machinery of the module.

Internal dependencies of a module should be handled in a relative manner. As an example, consider `data.py` importing the `identity` function from the `utils.py` submodule:

```py
# data_obj/data.py importing a function from "utils" module through the __init__.py medium
from . import identity
```

This project can be available externally (think of your users who are not seeing your source code) after installation at the repository level:

```sh
pip install -e .
```

The `-e` option allows the source code to be changed without requiring another installation for the changes to take place.
Now, as long as the environment is active, the modules can be imported from anywhere:

```py
import data_obj
# or 
from data_obj import data
```

An installation is also necessary if the stand-alone modules depend on one another. In such a case, imports cannot be relative:

```py
# data_obj/data.py importing an object from the "param" module
from param import Params
```
