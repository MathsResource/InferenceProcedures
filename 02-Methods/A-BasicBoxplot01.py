from bokeh.charts import BoxPlot, output_file, show
from bokeh.sampledata.autompg import autompg as df

# origin = the source of the data that makes up the autompg dataset
title = "MPG by Cylinders"

# N.B. "label" and "values"
box_plot = BoxPlot(df, label=['cyl'], values='mpg',title=title)

#Notice that Outliers Are Present
output_file("myFirstBasicBoxplot.html", title="boxplot_01.py example")

show(box_plot)
