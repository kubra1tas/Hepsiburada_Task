#!/usr/bin/python3.6
#Kubra Tas July 2021

"""
    Code is adapted from : https://towardsdatascience.com/market-basket-analysis-using-pysparks-fpgrowth-55c37ebd95c0

"""
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import functions as F
import pyspark.sql.functions as psf
from pyspark.ml.fpm import FPGrowth
import argparse
import os

def recomm(file, minSupport, minConfidence):
    """
    :param f: json file link
    :param minSupport: "the minimum support for an itemset to be identified as frequent"
    :param minConfidence: "minimum confidence for generating Association Rule"
    :return: association rules list with antecedents and consequent items, specified with confidence scores
    """

    #start the spark session
    sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))
    spark = SparkSession(sc)

    #read the input file
    df = spark.read.json(file, multiLine=True)
    df = df.select(psf.explode('events').alias('tmp')) \
    .select('tmp.*') #read input data and explode into columns


    #df.show(10, truncate=False)
    #df.orderBy("sessionid","eventtime", ascending=False).show(truncate=False) #optional : order the data by sessionid and eventtime

    data = df.dropDuplicates(['productid', 'sessionid']).sort('sessionid') # remove duplicate rows
    data = data.groupBy("sessionid").agg(F.collect_list("productid")).sort('sessionid') # groupby sessionid and aggregate by productid

    #basketdata.show()

    # Frequent Pattern Growth – FP Growth is a method of mining frequent itemsets using support, lift, and confidence.
    fpGrowth = FPGrowth(itemsCol="collect_list(productid)", minSupport=minSupport, minConfidence=minConfidence)
    model = fpGrowth.fit(data)

    # Display frequent itemsets
    #model.freqItemsets.show()
    items = model.freqItemsets
    #items.show()

    # Display generated association rules.
    #model.associationRules.show()
    rules = model.associationRules

    result_pdf = rules.select("*").toPandas() #select every columns
    result_pdf.to_csv('rules_frqItems.csv') #convert to csv and save the file

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument('--minSupport', type=str, dest="minSupport", default=0.0006) #get minSupport prm with default val 0.006
    parser.add_argument('--minConfidence', type=str, dest="minConfidence", default=0.0006)

    minSupport = parser.parse_args().minSupport
    minConfidence = parser.parse_args().minConfidence

    recomm(os.getcwd() + '/data/data/events.json', float(minSupport), float(minConfidence))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
