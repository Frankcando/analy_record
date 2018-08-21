#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Frank yu'

# #这个代码是为了根据交易记录统计分析交易的各项数据，比如 最大回撤，年化收益率，夏普率等等

import pandas as pd
import os
import requests
import csv

from datetime import datetime

print("begin to analysis trading records")

FileName = 'D:\\GoPath\src\\re_doc\\1534239306_tradedetail.csv'
with open(FileName,'r', encoding='UTF-8') as file_obj:
    lines = file_obj.readlines()
    for line in lines:
        print(line)


print("analysis end")