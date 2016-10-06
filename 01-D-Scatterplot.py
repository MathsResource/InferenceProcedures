from bokeh.sampledata.autompg import autompg as df
from bokeh.charts import Scatter, output_file, show

scatter = Scatter(df, x='mpg', y='hp', color='cyl', marker='origin',
                  title="Auto MPG", xlabel="Miles Per Gallon",
                  ylabel="Horsepower")

output_file('scatter.html')
show(scatter)
