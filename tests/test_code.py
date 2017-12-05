import numpy as np
import pytest

from some_module import integrate_trapz


# Test basic linear function is perfectly recovered
# There are plenty more tests we could write though!
def test_integrate_trapz_1():
    xs, ys = np.linspace(0, 10, 11), np.linspace(0, 10, 11)
    assert integrate_trapz(xs, ys) == 50


# Testing too much - ensuring it fails on weird input
# Normally this would be an AssertionException or a specific
# exception, not the general Exception class.
def test_integrate_trapz_failure():
    with pytest.raises(Exception):
        integrate_trapz("Some", "Values")
