# Import Bokeh modules for interactive plotting
import bokeh.io as bi
import bokeh.plotting as bp

# Set up Bokeh for inline viewing
bi.output_notebook()

# Set up plot
p = bp.figure(width=650, height=400, x_axis_label='x', y_axis_label='dy/dx',
              tools='pan,wheel_zoom,box_zoom,resize,reset')

# Populate glyphs
p.circle((x[1:] + x[:-1]) / 2.0, deriv, color='gray', legend='fin. diff.')
p.line(x, deriv_exact, color='black', line_width=2, legend='exact')

# Position legend
p.legend.location = 'top_center'

# Display plot
bp.show(p)
