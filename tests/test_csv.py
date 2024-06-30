import glob
import os

import pytest
from magma_to_csv import magma

@pytest.mark.parametrize(
    "name",
    [
        "bracoid.magma",
        "bracoid_and_hgs.magma",
        "groups_order_2_4.magma",
        "groups_order_4.magma",
        "groups_order_16.magma",
    ]
)
def test_csv_output(name):    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{current_dir}/testdata/{name}"
    output_dir = f"{current_dir}/output/{name}"
    
    os.makedirs(output_dir, exist_ok=True)
    clear_dir(output_dir)

    magma(input_file, output_dir)

    expected_output_dir = f"{current_dir}/testdata/expected_outputs_csv/{name}"
    expected_files = os.listdir(expected_output_dir)
    actual_files = os.listdir(output_dir)

    # check file names are equal
    assert expected_files == actual_files, "expected dir != actual dir"
    # check if file contents are equal
    for name in expected_files:
        with open(f"{expected_output_dir}/{name}") as f:
            expected_file = f.read()
        with  open(f"{output_dir}/{name}") as f:
            actual_file = f.read()

        assert expected_file == actual_file, f"expected {name} != actual {name}"
    
    clear_dir(output_dir)


def clear_dir(path: str):
    for f in glob.glob(f"{path}/*"):
        os.remove(f)
        


