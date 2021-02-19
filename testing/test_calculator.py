
# -*- coding: utf-8 -*-
import pytest
import yaml

from pythoncode.Calculator import Calculator


def get_datas(name, type='int'):
    with open("../datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)

    mydata = datas[name][type]['datas']
    ids = datas[name][type]['ids']
    return mydata, ids

@pytest.fixture(scope="module")
def get_instance():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_calc_datas_with_fixture(request):
    return (request.param)

def test_param(get_calc_datas_with_fixture):
    print(get_calc_datas_with_fixture)

class TestCalc(object):

    add_int_data = get_datas("add", "int")
    print(add_int_data[1])
    add_float_data = get_datas("add", "float")
    div_int_data = get_datas("div", "int")
    div_float_data = get_datas("div", "float")
    div_0_data = get_datas("div", "div0")



    @pytest.mark.parametrize("a,b,result", add_int_data[0], ids=add_int_data[1])
    def test_add_int(self, get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert  result == get_instance.add(a,b)

    # @pytest.mark.parametrize("a,b,result", add_int_data[0], ids=add_int_data[1])
    def test_add_int_fixture(self, get_instance, get_calc_datas_with_fixture):
        f = get_calc_datas_with_fixture
        assert f[2] == get_instance.add(f[0], f[1])

    @pytest.mark.parametrize("a,b,result", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == get_instance.add(a, b)

    @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])
    def test_div(self,get_instance, a, b, result):
        assert get_instance.div(a, b) == result

    @pytest.mark.parametrize("a,b,result", div_0_data[0], ids=div_0_data[1])
    def test_div_0(self, get_instance, a, b, result):
        with pytest.raises(ZeroDivisionError):
            result = a/b



if __name__ == '__main__':
    pass