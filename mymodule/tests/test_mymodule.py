import pytest
from mymodule import Mymodule, sample_function

@pytest.fixture
def Mymodule_object():
    obj = Mymodule()
    return obj

def test_Mymodule_instance_has_sample_method(Mymodule_object):
    assert hasattr(Mymodule_object, "sample_method")

def test_mymodule_has_sample_function():
    assert sample_function() is None  # no return value
