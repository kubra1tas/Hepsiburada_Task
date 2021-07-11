import argparse
import pandas as pd
import json

parser = argparse.ArgumentParser()
parser.add_argument('--firstItem', type=str, dest="item1", default=None)
parser.add_argument('--secondItem', type=str, dest="item2", default=None)
parser.add_argument('--thirdItem', type=str, dest="item3", default=None)
item1 = parser.parse_args().item1#.strip()
item2 = parser.parse_args().item2#.strip()
item3 = parser.parse_args().item3#.strip()

"""
item1 = "HBV00000OE7J7"
item2 = "HBV00000OE7UF"
item3 = "HBV00000OE7D4"
"""

items = []
items.append(item1)
items.append(item2)
items.append(item3)


data = pd.read_csv("rules_pdfItemsFreq2.CSV", index_col=False).drop(["Unnamed: 0"], axis=1)
mostVisited = pd.read_csv("top10mostVisited.csv", index_col=False)
ll = []
if item1 != None and item2 != None and item3 != None:
    it1 = "', '".join([item1, item2, item3])
    it2 = "', '".join([item2, item1, item3])
    it3 = "', '".join([item3, item2, item1])
    it4 = "', '".join([item1, item3, item2])
    it5 = "', '".join([item2, item3, item1])
    it6 = "', '".join([item3, item1, item2])
    ll.append(it1)
    ll.append(it2)
    ll.append(it3)
    ll.append(it4)
    ll.append(it5)
    ll.append(it6)

elif item1 == None and item2 != None and item3 != None:
    it9 = "', '".join([item3, item2])
    it10 = "', '".join([item2, item3])
    ll.append(it9)
    ll.append(it10)

elif item2 == None and item1 != None and item3 != None:
    it7 = "', '".join([item3, item1])
    it11 = "', '".join([item1, item3])
    ll.append(it7)
    ll.append(it11)

elif item3 == None and item1 != None and item2 != None:
    it8 = "', '".join([item1, item2])
    it12 = "', '".join([item2, item1])
    ll.append(it8)
    ll.append(it12)

else:
    if item1 != None:
        ll.append(item1)
    elif item2 != None:
        ll.append(item2)
    else:
        ll.append(item3)


with open('data/data/meta.json', 'r', encoding='utf-8') as f:
    prd = json.load(f)
df2 = pd.io.json.json_normalize(prd["meta"])


val = pd.DataFrame()
for res in ll:
    conf = data[data["antecedent"].str.contains(res)].drop_duplicates("consequent").sort_values("confidence", ascending=False).iloc[:11, :].reset_index(drop=True)
    if len(conf["antecedent"]) == 0:
        continue
    else:
        new = []

        for item in conf["consequent"]:
            item = item.split("[\'")[1].split("\']")[0]
            new.append(df2[df2["productid"] == item].loc[:, ["category", "subcategory", "name"]])

        resultDf = pd.concat(new)
        resultDf["score"] = conf["confidence"].values
        val = resultDf
        print(resultDf)

if len(val) == 0:
    #mostly visited items sonuclarini gonder
    new = []
    for item in mostVisited["productid"]:
        item = item#.split("[\'")[1].split("\']")[0]
        new.append(df2[df2["productid"] == item].loc[:, ["category", "subcategory", "name"]])

    resultDf = pd.concat(new)
    resultDf["score"] = 0.0
    val = resultDf
    print(resultDf)
