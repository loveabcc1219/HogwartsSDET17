
# -*- coding: utf-8 -*-
import pytest
import yaml

from pythoncode.Calculator import Calculator


def get_datas():
    with open("../datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas['add']['datas'], datas['add']['ids']

class TestCalc(object):
    datas,ids = get_datas()

    def setup_class(self):
        print("开始计算...")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算！")

    # @pytest.mark.parametrize("a,b, result", [
    #     [1,1,2],
    #     [100,200,300],
    #     [1,0,1]
    # ])
    @pytest.mark.parametrize("a,b,result", datas, ids=ids)
    def test_add(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert  result == self.calc.add(a,b)

    # todo: 相除功能
    def test_div(self):
        pass


if __name__ == '__main__':
    datas = get_datas()
    print(datas)