"""
Unit and regression test for the mars package.
"""

# Import package, test suite, and other packages as needed
import mars
import pytest
import sys

np.random.seed(0)

def helper():
    return 5

def test_mars_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mars" in sys.modules

def test_floats():
    assert 2*2 == 4
    assert pytest.approx(2.123 + 4.332 + 1e-15, abs=1.e-14) == 6.455

@pytest.mark.xfail
def test_floats_fail():
    assert pytest.approx(2.123 + 4.332 + 1e-5, abs=1.e-7) == 6.455

def test_exeception():
    with pytest.raises(TypeError):
        val = []
        val += 1.234

@pytest.mark.parametrize("a,b,ans", [
(2, 2, 4),
(3.0, 4.0, 7.0),
])
def test_add(a,b,ans):
    assert a + b == ans

def test_really_long_time():

    value_1 = 5
    value_2 = 3
    value_3 = 6

    results = sum([value_1,value_2, value_3,value_1+3,value_1*value_3*value_3,value_1,value_1*value_3*value_1+value_1+value_1])

def test_Random_skip():
    if np.random.rand(1)[0]>0.5:
        raise pytest.skip("I skip")

def test_dictionary():
    inp = {
        "option1": ion
    }
