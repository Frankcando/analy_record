#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Frank'

# #this code is to analysis

import configparser
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import os
import requests
import csv

from datetime import datetime

global File_detail, File_day
global StatTimeInCsv#在交易列表里的第一笔交易的开始日期
File_detail = ''
File_day = ''
start_date = ''
end_date = ''

start_moeny = 0 #init money
service_change = 0.001
Slippage = 0.0005

def read_data():
    print("begin to read data")

    try:
        with open(File_detail) as obj_detail:
            print('nothing, only test')

        with open(File_day) as obj_day:
            print('nothing,only test')

    except FileNotFoundError:
        print("file no exist")
    else:
        print("begin to read data")
        df_detail = pd.read_csv(File_detail, encoding='utf-8')
        df_day = pd.read_csv(File_day,encoding='utf-8')
        strdatetime = str(df_detail.loc[0][1])
        strdate = strdatetime[0:8]
        #对detail做循环 选取当天所有的交易
        for index ,row in df_detail.iterrows():
               print("ok")


        print("read end")

# def calc():

def init():
    cf = configparser.ConfigParser()
    cf.read('setting.ini')

    File_detail = cf.get("baseconf", "File_detail")
    File_day = cf.get("baseconf", "File_day")
    start_date = cf.get("baseconf", "start_date")
    end_date = cf.get("baseconf", "end_date")
    start_moeny = cf.getfloat("baseconf", "start_money")

    if File_detail =="":
        print('File_detail is empty')
    elif File_day =="":
        print('File_day is empty')
    elif start_date =="":
        print('start_date is empty')
    elif end_date =="":
        print('end_date is empty')
    elif start_moeny == 0:
        print('start_moeny is 0!!')
    else:
        print(" all setting is ok!")


if __name__ == "__main__":
    init()
    read_data()






