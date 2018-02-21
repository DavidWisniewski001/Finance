# David Wisniewski
# 02/20/2018
# THis is a program that gets information from the the internet on
# a particular company
# These are the libraries you will need
import datetime as dt
import matplotlib.pyplot as pyplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import tkinter as tk
from googlefinance.client import

style.use('ggplot')
# Sets the style of the graph
param ={
    'q': ".TSLA", #Stock symbol
    'i': "86400", # #Interval size in seconds("86400" = 1 day)
    'x': "INDEXNASD",
    'p': "4Y"
}
start = dt.datetime(2000,1,1)
end = dt.datetime(2018, 1, 1)
# Grabs all of the data from the January 1st to 2000
# to January 1st 2018


# df stands for data frame
# The company name is Tesla for aka TSLA
#
df = web.DataReader('TSLA', "google", start , end)
print(df.head())
