import datetime

import pytest

###########################################################################

@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun():
    print(datetime.datetime.now())
    assert  1 == 2

def test_assume():
    print("1", datetime.datetime.now())
    pytest.assume(1 == 4)
    print("2", datetime.datetime.now())
    pytest.assume(2 == 4)
    print("3", datetime.datetime.now())