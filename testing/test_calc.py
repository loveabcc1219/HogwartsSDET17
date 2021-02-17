
# -*- coding: utf-8 -*-


# 计算器：相加功能
import pytest


def add(a, b):
    return a+b


def test_add():
    assert add(1, 2) == 3

@pytest.mark.xxx222
def test_div():
    pass