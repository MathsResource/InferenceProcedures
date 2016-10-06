#Import the necessary library components
from bokeh.charts import Bar, output_file, show

#use output_file to visualize it in html file
#use output_notebook to visualize it in notebook

# create a simple data set
myData = {"y": [1, 2, 3, 4, 5]}

# Output to HELLOWORLD.HTML
output_file("Hello World.html", title="my first bokeh example")

# create a simple bar with a title and axis labels
p = Bar(myData, title="Simple Bar Chart Example",width=400, height=400)

# show the results
show(p)
