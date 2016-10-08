# Simple Scatter plot from "plotting"

from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure, show, output_file
colormap = {"setosa": "red",
"versicolor": "green",
"virginica": "blue"}
flowers["color"] = flowers["species"].map(lambda x: colormap[x])
output_file("iris.html", title="iris.py example")

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = "Petal Length"
p.yaxis.axis_label = "Petal Width"
p.circle(flowers["petal_length"],
flowers["petal_width"],color=flowers["color"],
fill_alpha=0.2, size=10, )

show(p)

## Exercises
#
#- Try this plot out for different combinations of predictors variables.
#- Try out some different colour combinations for the colormap.
#- Try this out with a different data set : autompg.
#- You can use cyl and origin as grouping variables.
#- The levels of cyl are 4,6 and 8.
#- The levels of origin are 1,2 and 3.

# You Need: from bokeh.sampledata.autompg import autompg
