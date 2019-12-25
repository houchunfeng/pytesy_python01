"""
获取数据
"""
import os

import yaml


class GetData:

    def get_yml_data(self, yml_name):
        """
        返回yaml文件数据
        :param yml_name:yaml的文件名
        :return:
        """
        with open("./data/" + os.sep + yml_name, "r", encoding="utf-8") as f:
            result = yaml.safe_load(f)
            print("yaml_data:" , result)
            return result
            # return yaml.safe_load(f)

    def get_json_data(self, json_name):
        """
        json数据文件
        :param json_name: json的文件名字
        :return:
        """
        return json_name
