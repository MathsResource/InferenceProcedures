import scipy.special

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

p1 = figure(title="Normal Distribution (Mean=0, Std. Dev=0.5)",tools="save",
            background_fill_color="#E8CC1B")

###################################################
# NumPy Stuff Here
# Best Leave it Alone

mu, sigma = 0, 0.5

measured = np.random.normal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=50)

x = np.linspace(-3,3, 5000)
pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2
###################################################
p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
        fill_color="#B365AA", line_color="#F33649")
p1.line(x, pdf, line_color="#4A5B41", line_width=8, alpha=0.7, legend="PDF")
p1.line(x, cdf, line_color="Red", line_width=2, alpha=0.7, legend="CDF")


####################################################
# Exercises:
# - Try Changing the number of sample size and number of bins
# - Try Changing the Colour Schemes, Line-Widths and Alpha Levels
# - See What Happens when you remove " tools='save' " from "figure()".
# - Try Changing around the following options
####################################################

p1.legend.location = "top_left"
p1.xaxis.axis_label = 'x'
p1.yaxis.axis_label = 'Pr(x)'

#####################################################

output_file('UglyHistogram.html', title="Gaussian Distribution Example (Ugly)")

show(p1)
