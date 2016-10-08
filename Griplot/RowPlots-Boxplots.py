from bokeh.charts import BoxPlot, output_file, show
from bokeh.layouts import row
from bokeh.sampledata.autompg import autompg as df

box = BoxPlot(df, values='mpg', label='cyl', title="Auto MPG Box Plot", plot_width=400)
box2 = BoxPlot(df, values='mpg', label='cyl', color='cyl',
               title="MPG Box Plot by Cylinder Count", plot_width=400)

output_file('box.html')
show(row(box, box2))
