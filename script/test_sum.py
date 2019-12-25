"""
求两个数的和---使用数据文件sum.yaml
"""
import os
import sys

import allure

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
    # Serverity的严重级别（）
    @allure.step("我是步骤的描述，第一步……第二步……")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @pytest.mark.parametrize("a, b, c", data_01())
    def test_sum(selfa, a, b, c):
        """
        判断两个数的和是否和预期的一致
        :return:
        """
        # 添加步骤描述信息----allure报告--和step搭配使用，对step的进一步说明
        allure.attach("文件名字", "文件的具体内容，具体步骤的描述信息")
        assert a + b == c
