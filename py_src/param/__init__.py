import yaml
from importlib.resources import open_text
from dataclasses import dataclass
from .dict2obj import obj


@dataclass()
class Params:
    """Contains list of project parameters read from the Parameters.yaml file.
    """
    _params_dict = yaml.safe_load(
        open_text('param', 'Parameters.yaml'))
    _params = obj(_params_dict)

    n_img: int = _params.category_A.n_img.value
    step_size: float = _params.category_B.step_size.value
