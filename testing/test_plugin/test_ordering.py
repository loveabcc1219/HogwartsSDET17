import pytest


@pytest.mark.run(order=2)
def test_order_a():
    print("aaaaaaaaa")

@pytest.mark.run(order=3)
def test_order_b():
    print("bbbbbbbbbb")

@pytest.mark.first
def test_order_c():
    print("ccccccccccc")

def test_order_d():
    print("dddddddddd")