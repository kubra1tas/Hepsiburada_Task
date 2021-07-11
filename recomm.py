#!/usr/bin/env python3


"""
    Code is taken from : https://towardsdatascience.com/market-basket-analysis-using-pysparks-fpgrowth-55c37ebd95c0

"""
import sys
import os
conf_path = os.getcwd()
sys.path.append(conf_path)
sys.path.append(conf_path + '\scripts\Setup')

from pyspark.sql import SparkSession, SQLContext
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import functions as F
import pyspark.sql.functions as psf
from pyspark.ml.fpm import FPGrowth
import  argparse


def print_hi(f, target_item):
    sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))
    spark = SparkSession(sc)

    df = spark.read.json(f, multiLine=True)
    df = df.select(psf.explode('events').alias('tmp')) \
    .select('tmp.*') #read input data and divide into columns automatically


    #df.show(10, truncate=False)
    #df.orderBy("sessionid","eventtime", ascending=False).show(truncate=False) #optional : order the data by sessionid and eventtime

    basketdata = df.dropDuplicates(['productid', 'sessionid']).sort('sessionid') # remove duplicate rows
    basketdata = basketdata.groupBy("sessionid").agg(F.collect_list("productid")).sort('sessionid') # groupby sessionid and aggregate by productid
    #print((df.count(), len(df.columns)), '\n',(basketdata.count(), len(basketdata.columns)))

    #basketdata.show()

    # Frequent Pattern Growth – FP Growth is a method of mining frequent itemsets using support, lift, and confidence.
    fpGrowth = FPGrowth(itemsCol="collect_list(productid)", minSupport=0.0006, minConfidence=0.0006)
    model = fpGrowth.fit(basketdata)
    # Display frequent itemsets.
    #model.freqItemsets.show()
    items = model.freqItemsets

    items.show()
    # Display generated association rules.
    #model.associationRules.show()
    rules = model.associationRules

    print((rules.count(), len(rules.columns)))
    # transform examines the input items against all the association rules and summarize the consequents as prediction
    model.transform(basketdata)
    transformed = model.transform(basketdata)

    transformed.show()

    result_pdf = rules.select("*").toPandas() #select every columns
    result_pdf.to_csv('rules_pdfItemsFreq2.CSV') #convert to csv and save the file

    #result_pdf.where(antecedent = target_item).show()

"""spark = SparkSession.builder.master('local[*]').getOrCreate()

multiline_df = spark.read.json(f, multiLine=True)
multiline_df.printSchema()
multiline_df = multiline_df.withColumn("events", multiline_df["events"].cast(StringType()))

#df = df.select(F.explode('element').alias('event', 'eventtime', 'price', 'productid', 'sessionid'))

#['event', 'eventtime', 'price', 'productid', 'sessionid']
df = df.withColumn("element", df["element"].cast(StringType()))

#print(df.select(df["element"], split(df["element"], ",  ").alias("ev")))

split_col = split(df.element, '\\,', )
df =  df.withColumn("element", split_col.getItem(0)).withColumn("event", split_col.getItem(1))
df.show()
"""
#df.printSchema()
#df.show(truncate=False)

"""
f = open(f)
data = json.load(f)

df = json_normalize(data['events'])


#data = pd.DataFrame.from_records(data)#, orient='index')

df.drop(['event', 'eventtime', 'price'], axis=1, inplace=True)



table = pd.get_dummies(df, columns=["productid"], drop_first=True).set_index(["sessionid"])
print(table)

onehot_encoder = OneHotEncoder(sparse=False)

frq_items = apriori(table, min_support=0.0005, use_colnames=True)
rules = association_rules(frq_items, metric="lift", min_threshold=1)
print(rules)
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('/home/kubra/PycharmProjects/Hepsiburada/data/data/events.json', input)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
