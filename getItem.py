#!/usr/bin/python3.6
#Kubra Tas July 2021

import argparse
import pandas as pd
import json
import os





def getItemList(item1, item2, item3, df2):
    '''

    :param item1: the first item added to the cart
    :param item2: the second item added to the cart
    :param item3: the third item added to the cart
    :param df2: meta data, used for obtaining information about the items in the cart
    :return: a list that contains all possible order of the items, in a case of one the items or two of the items
     are not given
    '''
    ll = []
    if item1 != None and item2 != None and item3 != None: #check if three items are given


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
        print(">>>>>>Items that are added to the cart:", '\n',
              df2[df2["productid"] == item1].loc[:, ["name"]].to_string(header=False), '\n',
              df2[df2["productid"] == item2].loc[:, ["name"]].to_string(header=False), '\n',
              df2[df2["productid"] == item3].loc[:, ["name"]].to_string(header=False), '\n', )

    elif item3 == None and item1 != None and item2 != None: #check if the third item is not provided
        it7 = "', '".join([item1, item2])
        it8 = "', '".join([item2, item1])
        ll.append(it7)
        ll.append(it8)
        print(">>>>>>Items that are added to the cart:", '\n',
              df2[df2["productid"] == item1].loc[:, ["name"]].to_string(header=False), '\n',
              df2[df2["productid"] == item2].loc[:, ["name"]].to_string(header=False), '\n')
    else: #check if only the first item provided
        ll.append(item1)
        print(">>>>>>Items that are added to the cart:", '\n',
              df2[df2["productid"] == item1].loc[:, ["name"]].to_string(header=False))

    return ll
def getItem(data, mostVisited,df2, ll):
    """

    :param data: given cart data, in dataframe format
    :param mostVisited: items that are mostly added to the carts
    :param df2: meta data in dataframe format
    :param ll: permutations of input items
    :return: recommended items
    """
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
            print(">>>>>>Recommended Items:", '\n', resultDf)

    if len(val) == 0: #if there is no assiciation is found, return the mostly added items
        #mostly visited items sonuclarini gonder
        new = []
        for item in mostVisited["productid"]:
            item = item#.split("[\'")[1].split("\']")[0]
            new.append(df2[df2["productid"] == item].loc[:, ["category", "subcategory", "name"]])

        resultDf = pd.concat(new)
        resultDf["score"] = 0.0
        print(">>>>>>Recommended Items:", '\n', resultDf)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--firstItem', type=str, dest="item1", default=None, required=True)
    parser.add_argument('--secondItem', type=str, dest="item2", default=None)
    parser.add_argument('--thirdItem', type=str, dest="item3", default=None)

    item1 = parser.parse_args().item1 #acquire the first item
    item2 = parser.parse_args().item2  # acquire the second item
    item3 = parser.parse_args().item3  # acquire the third item

    items = []
    items.append(item1)
    items.append(item2)
    items.append(item3)



    data = pd.read_csv(os.getcwd() + "/rules_frqItems.csv", index_col=False).drop(["Unnamed: 0"], axis=1) #read rules data
    mostVisited = pd.read_csv(os.getcwd() + "/top10mostVisited.csv", index_col=False) #read mostly added to the cart data

    with open(os.getcwd() + '/data/data/meta.json', 'r', encoding='utf-8') as file: #read meta data
        prd = json.load(file)
    meta = pd.io.json.json_normalize(prd["meta"]) #expand meta data into columns


    itemList =  getItemList(item1, item2, item3, meta) #get all possible item permutations
    getItem(data, mostVisited, meta, itemList) #get recommended items

