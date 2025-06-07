import os

import pytest
from magma_parser.parser import parse_file


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
def test_parse_file(name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parse_file(f"{current_dir}/testdata/{name}")
