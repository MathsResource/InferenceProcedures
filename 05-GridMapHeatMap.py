from bokeh.charts import HeatMap, bins, output_file, show

from bokeh.layouts import column, gridplot

from bokeh.sampledata.autompg import autompg

hm1 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'))

hm2 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'), values='cyl', stat='mean')

hm3 = HeatMap(autompg, x=bins('mpg'), y=bins('displ', bins=15),
              values='cyl', stat='mean')

hm4 = HeatMap(autompg, x=bins('mpg'), y='cyl', values='displ', stat='mean')

output_file("heatmap.html", title="heatmap.py example")

show(column(
  gridplot(hm1, hm2, hm3, hm4, ncols=2, plot_width=600, plot_height=600),
  )
)
