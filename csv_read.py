# -*- coding:utf-8 -*-

import csv
with open('csv_demo.csv','r') as f:
    data = csv.reader(f)
    headers = next(data)
    print(headers)