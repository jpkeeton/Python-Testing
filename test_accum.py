"""
This module contains basic uni tests for the accum module.
Purpose: Demo pytest framework by example...

"""

# --------------------------
# Imports
# --------------------------

import pytest
from Stuff.accum import Accumulator


# --------------------------
# Tests
# --------------------------

# verify start count = 0
def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0


# verify adding 1
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1


# verify adding 3
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


# copied from https://github.com/AndyLPK247/tau-intro-to-pytest/blob/example/5-classes/tests/test_accum.py
# as I couldn't read his screen
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10


"""
Functional Test Case Creation
    Arrange - Arrange assets for a test, like a setup procedure
    Act - Act by exercising the target behavior
    Assert - Assert that expected outcomes happen
"""
