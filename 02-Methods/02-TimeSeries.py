import pandas as pd

from bokeh.charts import TimeSeries, show, output_file
from bokeh.layouts import column

# read in some stock data from the Yahoo Finance API
AAPL = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
MSFT = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])
IBM = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2010",
    parse_dates=['Date'])

data = dict(
    AAPL=AAPL['Adj Close'],
    Date=AAPL['Date'],
    MSFT=MSFT['Adj Close'],
    IBM=IBM['Adj Close'],
)

tsline = TimeSeries(data,
    x='Date', y=['IBM', 'MSFT', 'AAPL'],
    color=['IBM', 'MSFT', 'AAPL'], dash=['IBM', 'MSFT', 'AAPL'],
    title="Timeseries", ylabel='Stock Prices', legend=True)

tspoint = TimeSeries(data,
    x='Date', y=['IBM', 'MSFT', 'AAPL'],
    color=['IBM', 'MSFT', 'AAPL'], dash=['IBM', 'MSFT', 'AAPL'],
    builder_type='point', title="Timeseries Points",
    ylabel='Stock Prices', legend=True)

output_file("timeseries.html")

show(column(tsline, tspoint))
