# Standard library imports
from pathlib import Path

# Related third party imports

# Local application/library specific imports
from data_obj import Data
from tasks import Task1


test_root = Path(__file__).parent.parent


def get_sample_data() -> Data:
    sample_file = test_root / "data/small.csv"
    assert sample_file.exists(), f"Sample file {sample_file} does not exist."
    return None


def test_task1():
    data = get_sample_data()
    task = Task1()
    output = task.run(data)
    assert output
