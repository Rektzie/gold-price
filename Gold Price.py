"""
    Project : Gold Price Analysis
    Group : Fontok Sleepy
    My Data : Gold Price and Years since 1950
    Members : 61070105
              61070108
              61070140
              61070246

"""
#------------------>Import<---------------
import pandas as pd
import pygal
from pygal.style import Style

#-------------->Custom Graph<--------------
custom_style = Style(
  value_font_family='supermarket',
  font_family='supermarket',
  opacity='5',
  opacity_hover='.9',
  colors=('#E2A500', '#E2A500'),
  plot_background=('#EAE9E6'),
  background=('#EAE9E6')
  )
#------------->call Graph<------------------
def gold():
    """
        READ csv.file [Date, Price]
        Create List 'lstdate', 'lstprice'
    """
    data = pd.read_csv('annual_csv.csv')
    lstdate = []  #--------->list for append.years<---------------
    lstprice = [] #--------->List for append Gold Price<----------
#Create Data List
#------------------->run data in annual_csv.csv<-----------------------
    for i in data.Date:
        lstdate.append(str(i))
    #print(lstdate)

    for j in data.Price:
        lstprice.append(float(j))
    #print(lstprice)

#Plot Graph with Pygal
    #---------------------------------->Custom Graph<--------------------------------------
    chart = pygal.StackedLine(fill=True, show_x_labels=True, plot_background='F9BF17', y_title='ราคา(USD)',\
     x_title='ปี ค.ศ. 1950 จนถึงปัจจุบัน', x_labels=lstdate, tooltip_border_radius=3, style=custom_style, \
     title = 'ราคาทองหน่วยดอลลาร์สหรัฐตั้งเเต่ ค.ศ.1950 จนถึงปัจจุบัน', range=[1, 2000])   #Grpah Title

    #----------------------------------->Data in Graph<------------------------------------
    chart.add('ราคาทองในปี', lstprice, show_dots=True, dots_size=2) #Gold Price graph
    #chart.add('Years', lstdate)

    chart.render_to_file('graphh.svg') #Render Graph for use

gold()
