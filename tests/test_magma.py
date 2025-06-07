import glob
import os

import pytest
from magma import magma

@pytest.mark.parametrize(
    "name",
    [
        "groups_order_2_structured.magma",
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
    output_dir = f"{current_dir}/output/csv/{name}"
    
    os.makedirs(output_dir, exist_ok=True)
    clear_dir(output_dir)

    magma(input_file, output_dir, "csv")

    expected_output_dir = f"{current_dir}/testdata/expected_outputs/csv/{name}"
    expected_files = os.listdir(expected_output_dir)
    actual_files = os.listdir(output_dir)

    # check file names are equal
    assert expected_files == actual_files, "expected dir != actual dir"
    # check if file contents are equal
    for name in expected_files:
        with open(f"{expected_output_dir}/{name}", 'r') as f:
            expected_file = f.read()
        with  open(f"{output_dir}/{name}", 'r') as f:
            actual_file = f.read()

        assert expected_file == actual_file, f"expected {name} != actual {name}"
    
    clear_dir(output_dir)


@pytest.mark.parametrize(
    "name",
    [
        "bracoid_and_hgs.magma",
        "groups_order_2_4.magma",
    ]
)
def test_xlsx_output(name):    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = f"{current_dir}/testdata/{name}"
    output_dir = f"{current_dir}/output/xlsx/{name}"
    
    os.makedirs(output_dir, exist_ok=True)
    clear_dir(output_dir)

    magma(input_file, output_dir, "xlsx")

    expected_output_dir = f"{current_dir}/testdata/expected_outputs/xlsx/{name}"
    expected_files = os.listdir(expected_output_dir)
    actual_files = os.listdir(output_dir)

    # check file names are equal
    assert expected_files == actual_files, "expected dir != actual dir"
    # we can't check if file contents are equal for xlsx as they're binary and some random bytes are different :shrug:
    # so we don't clear the directory, so they can be checked manually if needed


def clear_dir(path: str):
    for f in glob.glob(f"{path}/*"):
        os.remove(f)
