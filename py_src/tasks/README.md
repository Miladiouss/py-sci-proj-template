# Atoms of a data pipeline: an introduction to pipeline tasks

A data pipeline consist of processes to transform the data where these processes may be sequential to one another or have a more complex relationship.

A powerful design patter for a data pipeline consist of **tasks** (modularized processes on data). Tasks take a **data object** as input and return a modified copy of the input data or an entirely different class of data (constructed from extracted information from the input data).

A task can be constructed as a Python class with a run method that always returns an instance of the `Output` class:

```py
from dataclasses import dataclass
import copy

@dataclass
class Output:
    data_out: Data


class Task1():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self, data: Data) -> Output:
        # Main algorithm
        data = data / len(data)
        # Copy the updated data object and pass it in an Output envelop
        data_out = copy.copy(data)
        output = Output(data_out=data_out)

        return output
```

The `Output` class is a container for everything that the `run` method may return, which must include a data object. In the example above:

1. The `run` method takes a data object (of kind `Data`) as its argument
2. Normalizer the data by the length of the data
3. Constructs a copy of data to avoid unintended modifications to the original data.
4. Constructs an output object from the `Output` dataclass (commonly used as data containers)
5. Returns the output object to the caller.

Once a set of tasks are developed, the can be assembled as a data pipeline via a module or a script.
