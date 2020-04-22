"""
Unit and regression test for the mars package.
"""

# Import package, test suite, and other packages as needed
import mars
import pytest
import sys

def test_mars_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mars" in sys.modules
