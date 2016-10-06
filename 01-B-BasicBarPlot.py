
# Preliminaries
import pandas as pd
from bokeh.charts import Bar, output_file, show

# Create A Simple Data Set
dict = {'sec': {u'A': 10, u'B': 20}}
df = pd.DataFrame(dict)
df

# Setup an output location
output_file("bar.html")

# Render the Bar Plot
p = Bar(df)

# Present the Bar Plot
show(p)
