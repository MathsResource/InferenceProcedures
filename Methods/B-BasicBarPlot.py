# Preliminaries
import pandas as pd

# Import all the main commands that we will use here
from bokeh.charts import Bar, output_file, show

# Create A Simple Data Set
dict = {'sec': {u'A': 8, u'B': 12, u'C': 15, u'D': 14}}
df = pd.DataFrame(dict)
df

# Setup an output location
output_file("MyBasicBarPlot.html")

# Render the Bar Plot - Very Basic to start off with
p = Bar(df)

# Present the Bar Plot
show(p)
