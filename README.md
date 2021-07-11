# Hepsiburada_Task
Hepsiburada Data Scientist Task

![version](https://img.shields.io/badge/version-v1.0.0-green.svg?style=plastic)

An open source framework for recommendation of ten items, to the customers who added maximum three items to their cart. 

## Run
0. Requirements:
   * Install python3
   * pandas==1.3.0
   * pyspark==3.1.2
1. Running:
  You can give maximum three individual items with their product code. Sample input :
    `python3.6 getItem.py --firstItem "HBV00000OE7D4" --secondItem "HBV00000OE7UF" --thirdItem "HBV00000OE7J7"`
2. Backbone of the model relies on FPGrowth that is located under Spark MLlib : https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html 
3. Rules of the basket analysis are generated with the following hyper-parameters : 
    `minSupport= 0.0006, minConfidence= 0.0006`
4. In order to create a new rule list with a different hyper-parameters, please type:
    `python3.6 recomm.py --minSupport 0.007 --minConfidence 0.004
`
