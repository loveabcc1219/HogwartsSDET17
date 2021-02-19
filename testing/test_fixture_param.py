# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=['harry', 'hermine'], ids=["potter", "HHHH"])
def login(request):
    print("login")
    return request.param

def test_search(login):
    print(login)
    print("搜索")