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

#在交易列表里的第一笔交易的开始日期
File_detail = ''
File_day = ''
start_date = ''
end_date = ''

start_moeny = 0 #init money
service_change = 0.001
Slippage = 0.0005

df_detail =1
df_day =1

print("test test!")

def read_data():

    print("judge file exist")
    if False == os.path.isfile(File_detail):
        print("File_detail no exist")
        return -1
    if False == os.path.isfile(File_day):
        print("File_day no exist")
        return -1

    print("begin to read data")
    global  df_detail
    global  df_day
    df_detail = pd.read_csv(File_detail, encoding='utf-8')
    print(df_detail.loc[1][1])
    df_day = pd.read_csv(File_day,encoding='utf-8')
    print(df_day.loc[1][1])

    print("read end")
    return 1

def calc():
    strdatetime = str(df_detail.loc[0][1])
    strdate = strdatetime[0:8]
    print(strdate)
    # 对detail做循环 选取当天所有的交易
    #for index, row in df_detail.iterrows():

def init():
    cf = configparser.ConfigParser()
    cf.read('setting.ini')

    global  File_detail
    global File_day
    global start_date
    global end_date
    global start_moeny

    File_detail = cf.get("baseconf", "File_detail")
    File_day = cf.get("baseconf", "File_day")
    start_date = cf.get("baseconf", "start_date")
    end_date = cf.get("baseconf", "end_date")
    start_moeny = cf.getfloat("baseconf", "start_money")

    if File_detail =="":
        print('File_detail is empty')
        return  -1
    elif File_day =="":
        print('File_day is empty')
        return -1
    elif start_date =="":
        print('start_date is empty')
        return -1
    elif end_date =="":
        print('end_date is empty')
        return -1
    elif start_moeny == 0:
        print('start_moeny is 0!!')
        return -1
    else:
        print(" all setting is ok!")
        return 1


if __name__ == "__main__":

    if  1== init():
         if 1== read_data():
             calc()






