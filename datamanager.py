# -*- coding:utf-8 -*- 
# Author : QX
# Data :2022/6/7 0:13
import pandas as pd


class DataManager():
    def __int__(self):
        self.sheet_name = None
        self.excel_path = None
        self.rows = None
        self.columns = None
        # 标题所在行
        self.title_row = 2
        # 多条件分隔符
        self.condition_sign = '|'
        # 数据池起始数据行
        self.data_start_row = 3
        self.excel_data = None

    def excel_init(self,excel_path,sheet_name):
        '''
        数据初始化
        :param excel_path:
        :param sheet_name:
        :return:
        '''
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        data = pd.read_excel(excel_path,sheet_name=sheet_name,dtype=str)
        data = data.where(data.notnull(),None)
        self.excel_data = data

    def get_data_list(self,data_condition,number=None):
        valid_data_list = []
        element_name = self.excel_data.values
        for i in element_name:
            row_data_dict = {}
            # 拼接成字典
            row_data_dict.update(dict(zip(self.excel_data.columns,i)))
            # 生成条件数组
            if self.condition_sign in data_condition:
                condition_list = data_condition.split(self.condition_sign)
            else:
                condition_list = []
                condition_list