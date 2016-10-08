# Diamonds
import os
import numpy as np

os.getcwd()

# Task
# - How many cases are there in Diamond Data Set?
# - Create a Two Way Frequency Table for Cut and Color


import pandas as pd

diamonds = pd.read_csv("diamonds.csv")

diamonds.tail(5)

diamonds.shape


diamonds.describe()


byCutColor = diamonds.groupby(["cut","color"])


output = byCutColor["carat"].count()


# byCutColor["carat"].count().unstack()

len(output)

# Remove Index
# - http://stackoverflow.com/questions/20107570/removing-index-column-in-pandas
