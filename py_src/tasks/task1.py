__all__ = ["Task1"]

# Standard library imports
from dataclasses import dataclass
import copy

# Local application/library specific imports
from data_obj import Data

# ==============================================================================


@dataclass
class Output:
    data_out: Data


class Task1():
    """Task1
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self, data: Data) -> Output:
        # Main algorithm
        pass
        # Copy the updated data object and pass it in an Output envelop
        data_out = copy.copy(data)
        output = Output(data_out=data_out)

        return output
