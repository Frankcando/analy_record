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
from datetime import date, timedelta

#在交易列表里的第一笔交易的开始日期
File_detail = ''
File_day = ''
start_y = 0
start_m = 0
start_d = 0

end_y = 0
end_m = 0
end_d = 0

start_moeny = 0 #init money
service_change = 0.001
Slippage = 0.0005

df_detail =1
df_day =1
data_array = []

df_result = 1#保存每日账户总资产

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
    df_detail = pd.read_csv(File_detail, encoding='utf_8_sig',header=1)
    print(df_detail.loc[1][1])
    df_day = pd.read_csv(File_day,encoding='utf_8_sig')
    print(df_day.loc[1][1])

    print("read end")
    return 1

def gen_dates(bdate, days):
    day = timedelta(days=1)
    for i in range(days):
        yield bdate + day*i

def calc():

    line = len(df_detail)
    bdate = date(start_y, start_m, start_d)

    strEndTime = date(end_y, end_m, end_d)
    for d in gen_dates(bdate, 1000):
        #print(type(d))
        if str(d) == str(strEndTime):
            break

        #这里正式开始查找计算了,查找区间的每一天在交易明细表里是否出现过，即这一天是否有交易记录
        print(df_detail.head())



    #print(data_array)

    # for index, row in df_detail.iterrows():
    #     strdatetime = str(df_detail.loc[index]['时间'])
    #     strdate = strdatetime[0:8]
    #     print(strdate)



def init():
    cf = configparser.ConfigParser()
    cf.read('setting.ini')

    global  File_detail
    global File_day

    global start_y
    global start_m
    global start_d

    global end_y
    global end_m
    global end_d

    File_detail = cf.get("baseconf", "File_detail")
    File_day = cf.get("baseconf", "File_day")
    start_y = cf.getint("baseconf", "start_y")
    start_m = cf.getint("baseconf", "start_m")
    start_d = cf.getint("baseconf", "start_d")

    end_y = cf.getint("baseconf", "end_y")
    end_m = cf.getint("baseconf", "end_m")
    end_d = cf.getint("baseconf", "end_d")

    start_moeny = cf.getfloat("baseconf", "start_money")

    if File_detail =="":
        print('File_detail is empty')
        return  -1
    elif File_day =="":
        print('File_day is empty')
        return -1

    elif start_y ==0:
        print('start_y is empty')
        return -1
    elif start_m ==0:
        print('start_m is empty')
        return -1
    elif start_d ==0:
        print('start_d is empty')
        return -1

    elif end_y ==0:
        print('end_y is empty')
        return -1
    elif end_m ==0:
        print('end_m is empty')
        return -1
    elif end_d ==0:
        print('end_d is empty')
        return -1

    else:
        print(" all setting is ok!")
        return 1


if __name__ == "__main__":

    if  1== init():
         if 1== read_data():
             calc()






