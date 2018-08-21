#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Frank yu'

# #这个代码是为了根据交易记录统计分析交易的各项数据，比如 最大回撤，年化收益率，夏普率等等

import pandas as pd
import numpy as np
import os
import requests
import csv

from datetime import datetime

print("begin to analysis trading records")

FileName = '1534239306_tradedetail.csv'
f = open(FileName,'r' , encoding= 'utf-8')
df_detail = pd.read_csv(f)
print(str(df_detail))

FileName = 'btcusd_day_day.csv'
f = open(FileName, 'r', encoding='utf-8')
df_day = pd.read_csv(f)
print(str(df_day))



print("analysis end")