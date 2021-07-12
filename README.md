# Hepsiburada_Task
Hepsiburada Data Scientist Task

![version](https://img.shields.io/badge/version-v1.0.0-green.svg?style=plastic)

Association Rule Mining
An open source framework for recommendation of ten items, to the customers who added maximum three items to their cart. Backbone of the model relies on FPGrowth that is located under Spark MLlib-FPM : https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html. The library mainly finds the frequently bought together items, based on the items that are added to carts. 


## Run
0. Requirements:
   * Install python3
   * pandas==1.3.0
   * pyspark==3.1.2
1. Running:
  You can give maximum three individual items with their product code. Sample input :
    `python3.6 getItem.py --firstItem "HBV00000OE7D4" --secondItem "HBV00000OE7UF" --thirdItem "HBV00000OE7J7"`
2. Rules of the basket analysis are generated with the following hyper-parameters : 
    `minSupport= 0.0006, minConfidence= 0.0006`
3. In order to create a new rule list with a different hyper-parameters, please type:
    `python3.6 recomm.py --minSupport 0.007 --minConfidence 0.004`
4. In the case of no rule based descendent item is found, the code will present the ten items that are added to the cart the most frequently. 


Sample inputs and coressponding frequently bought together items that are recommended with scores, in descending order:
```
kubra@it-lunix:~/PycharmProjects/Hepsiburada$ /usr/bin/python3.6 getItem.py --firstItem "HBV00000OE7D4" --secondItem "HBV00000OE7UF" --thirdItem "HBV00000OE7J7"
Items that are added to the cart: 
 2803  Maydanoz 
 8291  Havuç 500 gr 
 5558  Göbek Salata Adet 

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
Sample inputs and top ten added to the carts items, since no frequently bought together items could be found, as will in descending order based on their count :  
```
kubra@it-lunix:~/PycharmProjects/Hepsiburada$ /usr/bin/python3.6 getItem.py --firstItem "HBV00000OE7D4" --secondItem "HBV00000NE24H"
Items that are added to the cart: 
 2803  Maydanoz 
 8657  Carrefour Yeşil Mercimek 1 kg 

                  category      subcategory                               name  score
7259  Et, Balık, Şarküteri       Kırmızı Et                 Dana Biftek 250 gr    0.0
4869        Meyve ve Sebze            Sebze                       Patates 1 kg    0.0
4358        Meyve ve Sebze            Sebze               Domates Pembe 500 gr    0.0
73          Meyve ve Sebze            Sebze              Domates Salkım 500 gr    0.0
2068        Meyve ve Sebze            Meyve                       Çilek 250 gr    0.0
3392  Et, Balık, Şarküteri       Kırmızı Et    Dana Kıyma (%14-%20 Yağ) 250 gr    0.0
2556        Meyve ve Sebze            Meyve                 Limon Lamas 500 gr    0.0
4994  Et, Balık, Şarküteri       Kırmızı Et      Dana Kıyma (%5-%7 Yağ) 250 gr    0.0
8362             İçecekler  Gazlı İçecekler  Beypazarı Doğal Maden Suyu 200 ml    0.0
695   Et, Balık, Şarküteri       Kırmızı Et                Dana Kuşbaşı 500 gr    0.0


```

## Decision-Making Process
Since the data does not include any personal information (such as IP addresses of customers or cookie id's) or any eplicit feedback, collaborative algorithms are not appropriate technique to apply. Even though collaborative filterings (might be user-based, or item-based) are used for personalized recommendations, these models rely on feedback taken from the customer. If there is no explicit feedback, such as rating, implicit feedbacks can be produced (Please for further information, visit : `https://drive.google.com/file/d/1_4G1zuCgrGeh-d_4W1YcBmqsrDiTzdBG/view?usp=sharing`). 
