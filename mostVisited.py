#!/usr/bin/python3.6
# Kubra Tas July 2021


import pandas as pd
import json
import os


with open(os.getcwd() + '/data/data/events.json', 'r', encoding='utf-8') as f:
    prd = json.load(f)
df = pd.io.json.json_normalize(prd["events"])

df2 = df.groupby("productid").count().sort_values(by="event",ascending=False)[:10] #group by the data, sort values and return 10 most added
df2.to_csv(os.getcwd() + "top10mostVisited.csv")
