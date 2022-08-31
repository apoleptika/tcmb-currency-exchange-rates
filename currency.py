
from datetime import datetime
import sys
from xml.etree.ElementTree import parse
# if you want you can install and use package Requests,  pip install requests
# we using Python standart module urllib.request
from urllib.request import urlopen
# if you need install package Tabulate,  pip install tabulate
from tabulate import tabulate
# if you need install package Pandas,  pip install pandas
import pandas as pd
# import file arguments.py
import arguments as param


date1 = ""
date2 = ""
# create empty list
first_currency_list = []
last_currency_list = []
# url = urlopen('https://www.tcmb.gov.tr/kurlar/202112/01122021.xml')
url = 'https://www.tcmb.gov.tr/kurlar/'


def firstdate_get_data():        
    date1 = datetime.strptime(param.firstdate, '%d.%m.%Y')
    year_month = str(date1.year) + f'{date1.month:02d}'
    day_month_year = f'{date1.day:02d}' +  f'{date1.month:02d}' + f'{date1.year}' + ".xml"  
    global data_url
    data_url = url + year_month +'/'+ day_month_year
        
    try:
        xmlUrl = urlopen(data_url)
        xmldoc = parse(xmlUrl)
        print("")
        print(date1.strftime('%d.%m.%Y'), "- first date data is OK.")
        print("TCMB Currency Exchange Rates Url : ", data_url)
    except:
        print("")
        print(date1.strftime('%d.%m.%Y'), "- first date data is NOT OK.")
        print("Error. Central Bank of the Republic of Türkiye, no data on this date, " + date1.strftime('%d.%m.%Y'))
        print("")
        sys.exit(2)

    for item in xmldoc.iterfind('Currency'):
        code = item.attrib["CurrencyCode"]
        # isim = item.findtext('Isim')   
        name = item.findtext('CurrencyName')
        # forex_buying = item.findtext('ForexBuying')
        forex_selling = item.findtext('ForexSelling')
        if not forex_selling: 
            forex_selling=0
        # add values to List
        first_currency_list.append([code, name, forex_selling])
       

def lastdate_get_data():
    date2 = datetime.strptime(param.lastdate, '%d.%m.%Y')
    year_month = str(date2.year) + f'{date2.month:02d}'
    day_month_year = f'{date2.day:02d}' +  f'{date2.month:02d}' + f'{date2.year}' + ".xml"  
    data_url = url + year_month +'/'+ day_month_year
       
    try:
        xmlUrl = urlopen(data_url)
        xmldoc = parse(xmlUrl)
        # print("")
        print(date2.strftime('%d.%m.%Y'), "- last date data is OK.")
        print("TCMB Currency Exchange Rates Url : ", data_url)
        # print("")
    except:
        print(date2.strftime('%d.%m.%Y'), "- last date data is NOT OK.")
        print("Error. Central Bank of the Republic of Türkiye, no data on this date, " + date2.strftime('%d.%m.%Y'))
        print("")
        sys.exit(2)

    for item in xmldoc.iterfind('Currency'):
        code = item.attrib["CurrencyCode"]
        # isim = item.findtext('Isim')   
        name = item.findtext('CurrencyName')
        # forex_buying = item.findtext('ForexBuying')
        forex_selling = item.findtext('ForexSelling')
        if not forex_selling:
            forex_selling=0
        last_currency_list.append([code, name, forex_selling])


# create empty Pandas data frames
panda_df1 = pd.DataFrame()
panda_df2 = pd.DataFrame()
result_df = pd.DataFrame()

if not param.firstdate:
    print("No first date data")
    sys.exit(2)
else:
    firstdate_get_data()
    panda_df1 = pd.DataFrame(first_currency_list)
    # rename column header names in Panda Data Frame
    panda_df1.columns = ['Code', 'Name', 'OldValue']

if not param.lastdate:
    print("No last date data.")
    # sys.exit(2)
else:
    lastdate_get_data()
    panda_df2 = pd.DataFrame(last_currency_list)
    # rename column header names in Panda Data Frame    
    panda_df2.columns = ['Code', 'Name 2', 'NewValue']
    # delete unnecessary column in Pandas Data Frame
    del panda_df2["Name 2"]

if (param.firstdate) and (param.lastdate):
    result_df = pd.merge(panda_df1, panda_df2, how="left", on=["Code"])
    # create calculated column in Pandas Data Frame
    result_df['Percent %'] = ((result_df['NewValue'].astype(float) / result_df['OldValue'].astype(float) ) -1) *100
    print("")
    print(tabulate(result_df, headers=["Code", "Name", "OldValue TL", "NevValue TL", "Percent %"], tablefmt="simple"))
    print("")

if (param.firstdate) and (not param.lastdate):
    print("")
    print(tabulate(panda_df1, headers=["Code", "Name", "Value TL"], tablefmt="simple"))
    print("")

