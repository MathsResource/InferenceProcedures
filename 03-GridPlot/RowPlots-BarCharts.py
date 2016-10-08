from bokeh.charts import Bar, output_file, show
from bokeh.layouts import row

# best support is with data in a format that is table-like
data = {
    'sample': ['1st', '2nd', '1st', '2nd', '1st', '2nd'],
    'interpreter': ['python', 'python', 'pypy', 'pypy', 'jython', 'jython'],
    'timing': [-2, 5, 12, 40, 22, 30]
}

# x-axis labels pulled from the interpreter column, stacking labels from sample column
bar = Bar(data, values='timing', label='interpreter', stack='sample', agg='mean',
          title="Python Interpreter Sampling", legend='top_right', plot_width=400)

# table-like data results in reconfiguration of the chart with no data manipulation
bar2 = Bar(data, values='timing', label=['interpreter', 'sample'],
           agg='mean', title="Python Interpreters", plot_width=400)

output_file("stacked_bar.html")
show(row(bar, bar2))
