# RowPlot-Histogram

from bokeh.charts import Histogram, output_file, show
from bokeh.layouts import row
from bokeh.sampledata.autompg import autompg as df

##################################################

hist = Histogram(df, values='mpg', title="Auto MPG Histogram", plot_width=400)

# Compare Both Data Specifications

hist2 = Histogram(df, values='mpg', label='cyl', color='cyl', legend='top_right',
                  title="MPG Histogram by Cylinder Count", plot_width=400)

#################################################

output_file('hist.html')
show(row(hist, hist2))
