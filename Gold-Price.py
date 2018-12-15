"""
    Project
    Gold Price
    61070105
    61070108
    61070140
    61070246
"""
import pandas as pd
import pygal
from pygal.style import DarkStyle

def main():
    """
        READ csv.file  [Date, Price]
    """
    data = pd.read_csv('annual_csv.csv')
    lstdate = [] #--------->list for append.years<---------------
    lstprice = [] #-------->List for append Gold Price<----------
    #Create Data List

    for i in data.Date:
        lstdate.append(str(i))
    #print(lstdate)

    for j in data.Price:
        lstprice.append(float(j))
    #print(lstprice)
    #Plot Graph with Pygal
    #---------------------------------->Custom Graph<--------------------------------------

    chart = pygal.StackedLine(fill=True, interpolate='quadratic', y_title='Price(USD)',\
     x_title='Years since 1950', x_labels=lstdate, tooltip_border_radius=3, style=DarkStyle, \
     title = 'Gold Price', range=[1, 2000], plot_background='#E8537A')

    #----------------------------------->Data in Graph<------------------------------------
    chart.add('Gold Price(USD)', lstprice) #Gold Price graph
    #chart.add('Years', lstdate)

    chart.render_to_file('graphh.svg') #Render Graph for use



main()
