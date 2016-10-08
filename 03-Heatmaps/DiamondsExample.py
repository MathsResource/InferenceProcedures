# Diamonds
import os
import numpy as np
import pandas as pd

os.getcwd()

# Task
# - How many cases are there in Diamond Data Set?
# - Create a Two Way Frequency Table for Cut and Color



diamonds = pd.read_csv("diamonds.csv")
diamonds.tail(5)
diamonds.shape
diamonds.describe()
byCutColor = diamonds.groupby(["cut","color"])
output = byCutColor["carat"].count()
# byCutColor["carat"].count().unstack()

len(output)

###########################################################################################




byCutColor["carat"].count().unstack()



#################################################

myData = byCutColor["carat"].count()

myData2 = myData #  Two Copies - I want to show something off
################################################
type(myData)

myData2.reset_index

myData.index[1]

#################################################

collect=pd.DataFrame(columns=("V1","V2"))

for i in range(5):
    #print(myData.index[i])
    Temp1 = myData.index[i][0]
    Temp2 = myData.index[i][1]
    AddRow=pd.Series([Temp1,Temp2],index=["V1","V2"])
    print(AddRow)
    collect = collect.append(AddRow,ignore_index=True)
