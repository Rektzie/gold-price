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


def main():
    """
        READ csv.file  [Date, Price]
    """
    data = pd.read_csv('monthly_csv.csv')
    lstdate = []
    lstprice = []
    #Create Data List
    for i in data.Date:
        lstdate.append(str(i))
    print(lstdate)
    for j in data.Price:
        lstprice.append(float(j))
    print(lstprice)



main()
