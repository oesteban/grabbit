import pytest
from grabbit import Structure
from os.path import join, dirname
from pprint import pprint


def test_full():
    json_file = join(dirname(__file__), 'specs', 'test.json')
    data_dir = join(dirname(__file__), 'data', '7t_trt')
    struct = Structure(json_file, data_dir)
    result = struct.get(filters={'subject': '[1234]', 'run': '1'})