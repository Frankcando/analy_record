#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Frank'

# #this code is to analysis

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import os
import requests
import csv

from datetime import datetime

global File_detail, File_day

File_detail = '1534239306_tradedetail.csv'
File_day = 'day_day.csv'

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
        #print(df_day[0:3])
        print("read end")

if __name__ == "__main__":
    read_data()






