import pandas as pd
import json
with open('data/data/events.json', 'r', encoding='utf-8') as f:
    prd = json.load(f)
df = pd.io.json.json_normalize(prd["events"])

df2 = df.groupby("productid").count().sort_values(by="event",ascending=False)[:10]
df2.to_csv("top10mostVisited.csv")