"""
求两个数的和---使用数据文件sum.yaml
"""
import os
import sys

sys.path.append(os.getcwd())
import pytest

from base.get_data import GetData



def data_01():
    """
    读取文件的内容
    :return:
    """
    sum_list = []
    result = GetData().get_yml_data('sum.yml')
    for i in result.values():
        sum_list.append(tuple(i.values()))
        print("sum_list", sum_list)
    return sum_list


class TestSum:
    @pytest.mark.parametrize("a, b, c", data_01())
    def test_sum(selfa, a, b, c):
        """
        判断两个数的和是否和预期的一致
        :return:
        """
        assert a + b == c
