import datetime

import pytest


@pytest.fixture(scope="module")
def login():
    print("登录操作")
    now = datetime.datetime.now()
    yield now
    print("登出操作")

@pytest.fixture
def get_username(login):
    username = "Hermine"
    print(username)
    return username

def test_search():
    print("搜索")


def test_cart(login):
    print(login)
    print("购物")


def test_order(login):
    print("下单")