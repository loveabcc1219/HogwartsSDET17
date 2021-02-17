
# -*- coding: utf-8 -*-
import pytest
import yaml

from pythoncode.Calculator import Calculator


def get_datas(name, type='int'):
    with open("../datas/calc.yml") as f:
        datas = yaml.safe_load(f)

    mydata = datas[name][type]['datas']
    ids = datas[name][type]['ids']
    return mydata, ids


class TestCalc(object):

    add_int_data = get_datas("add", "int")
    print(add_int_data[1])
    add_float_data = get_datas("add", "float")
    div_int_data = get_datas("div", "int")
    div_float_data = get_datas("div", "float")
    div_0_data = get_datas("div", "div0")

    def setup_class(self):
        print("开始计算...")
        self.calc = Calculator()


    def teardown_class(self):
        print("结束计算！")

    @pytest.mark.parametrize("a,b,result", add_int_data[0], ids=add_int_data[1])
    def test_add_int(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert  result == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,result", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result

    @pytest.mark.parametrize("a,b,result", div_0_data[0], ids=div_0_data[1])
    def test_div_0(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            result = a/b


if __name__ == '__main__':
    pass