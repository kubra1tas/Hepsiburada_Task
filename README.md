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
    `python3.6 recomm.py --minSupport 0.007 --minConfidence 0.004`
5. In the case of no rule based descendent item is found, the code will present the ten items that are added to the cart the most frequently. 


Sample input and coressponding frequently bought together algorithms that are recommended with scores, in descending order:
```
kubra@it-lunix:~/PycharmProjects/Hepsiburada$ /usr/bin/python3.6 getItem.py --firstItem "HBV00000OE7J7" --secondItem "HBV00000OE7UF" --thirdItem "HBV00000OE7D4"
            category subcategory                   name     score
4247  Meyve ve Sebze       Sebze                Dereotu  0.522936
3522  Meyve ve Sebze       Sebze       Soğan Taze Demet  0.486239
2556  Meyve ve Sebze       Meyve     Limon Lamas 500 gr  0.477064
4869  Meyve ve Sebze       Sebze           Patates 1 kg  0.449541
3590  Meyve ve Sebze       Sebze                   Roka  0.422018
1321  Meyve ve Sebze       Sebze   Kıvırcık Salata Adet  0.403670
3794  Meyve ve Sebze       Sebze                   Nane  0.394495
5214  Meyve ve Sebze       Sebze       Salatalık 500 gr  0.339450
4358  Meyve ve Sebze       Sebze   Domates Pembe 500 gr  0.339450
73    Meyve ve Sebze       Sebze  Domates Salkım 500 gr  0.339450
```
