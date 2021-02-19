import pytest


@pytest.fixture()
def login():
    print("登录操作")

@pytest.fixture()
def get_username(login):
    username = "Hermine"
    print(username)
    return username

def test_search(get_username):
    print("搜索")



def test_cart():
    print("购物")



def test_order():
    print("下单")