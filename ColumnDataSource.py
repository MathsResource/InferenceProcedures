
import bokeh
import numpy as np
import bokeh.plotting as plt
plt.output_notebook()

bokeh.__version__

### '0.12.2'


source = plt.ColumnDataSource(
    data=dict(
        a = [1,2,3,4,5],
        b = [1,4,9,16,25],
        c = np.array([0,10,20,30,40]),
        size = [True, False, True, False, True],
    )
)
​
#######################################

type(source)

bokeh.models.sources.ColumnDataSource


print(source.data['size'])

#######################################

fig = plt.figure()
fig.scatter('a', 'b', source=source, size=((source.data['c']+10)/5))
plt.show(fig)
