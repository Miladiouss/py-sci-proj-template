import yaml
from importlib.resources import open_text
from types import SimpleNamespace
from dataclasses import dataclass


def _construct_bands_dict(**kwargs):
    param_dict = yaml.safe_load(
        open_text('param', 'Parameters.yaml'))
    cat_a = SimpleNamespace(**param_dict['category_A'])
    return cat_a
