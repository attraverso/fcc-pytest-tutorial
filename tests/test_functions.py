import pytest
import src.functions as fun
import time


def test_add():
    result = fun.add(1, 4)
    assert result == 5


def test_add_strings():
    result = fun.add("hello", " darkness")
    assert result == "hello darkness"


def test_divide():
    result = fun.divide(4, 2)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        fun.divide(4, 0)


# you can use this to tag your tests. "slow" here is your tag name
# you can then run only these by using `pytest -m slow`
@pytest.mark.slow
def test_slow():
    time.sleep(2)
    result = fun.add("hello", " darkness")
    assert result == "hello darkness"

# you can use the skip tag to skip running a test, and you can optionally provide a reason
# you will see the test listed as skipped in the results
@pytest.mark.skip(reason="This feature is currently broken")
def test_slow():
    time.sleep(2)
    result = fun.add("hello", " darkness")
    assert result == "hello darkness"

# you can use the xfail tag to mark tests that you know might fail
# you can optionally add the reason why they might fail
# they will be listed as xpassed in case of success, xfailed in case of failure
@pytest.mark.xfail(reason="We know dividing by zero will cause things to explode")
def test_divide_by_zero():
    fun.divide(4, 2)