import pytest


@pytest.mark.parametrize("name",["刘德华","张学友"])
def test_print(name):
    print(name)