# -*- coding:utf-8

# ocnftest.py 文件名固定，不能改
import datetime
from typing import List

import pytest


@pytest.fixture(scope="session")
def login():
    print("登录操作")
    now = datetime.datetime.now()
    yield now
    print("登出操作")

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)


    for item in items:
        # 用例名称支持中文
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # 自动加标签
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)

    # 翻转用例执行顺序
    items.reverse()

