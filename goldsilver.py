# https://medium.com/@raiyanquaium/how-to-web-scrape-using-beautiful-soup-in-python-without-running-into-http-error-403-554875e5abed
# https://goldprice.org/gold-price-today/2017-10-15
# Gümüş Altın Paladium Platin fiyat bilgileri 15.10.2017 tarihinden sonra mevcut, bu tarihten önce bilgi yok  

# pip install beautifulsoup4
from bs4 import BeautifulSoup as soup
# if you need install package Tabulate,  pip install tabulate
from tabulate import tabulate
# if you need install package Pandas,  pip install pandas
import pandas as pd
from urllib.request import Request, urlopen 
from datetime import datetime
# import file arguments.py
import arguments as param


gold_url= 'https://goldprice.org/gold-price-today/'
gold_date1 = ""
gold_firstdate = ""
gold_date2 = ""
gold_lastdate = ""

def first_metal_price_usd(precious_metal):
    # if you want to change global variable value, you have to use global keyword 
    global gold_date1
    gold_date1 = datetime.strptime(param.firstdate, '%d.%m.%Y')
    global gold_firstdate
    gold_firstdate = str(gold_date1.year) + "-" + f'{gold_date1.month:02d}' + "-" + f'{gold_date1.day:02d}'
    url_goldprice = gold_url + gold_firstdate
    try:
        html_url= url_goldprice
        # you have to use headers={'User-Agent': 'Mozilla/5.0'}) to prevent error message 
        req = Request(html_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        page_soup = soup(webpage, 'html.parser')
        containers = page_soup.find("table","table table-hover table-bordered").find("tbody").find("td", text=precious_metal).find_next_sibling("td").text
    except:
        containers = "0"
    return containers


def last_metal_price_usd(precious_metal):
    global gold_date2
    gold_date2 = datetime.strptime(param.lastdate, '%d.%m.%Y')
    global gold_lastdate
    gold_lastdate = str(gold_date2.year) + "-" + f'{gold_date2.month:02d}' + "-" + f'{gold_date2.day:02d}'
    url_goldprice = gold_url + gold_lastdate
    try:
        html_url= url_goldprice
        # you have to use headers={'User-Agent': 'Mozilla/5.0'}) to prevent error message 
        req = Request(html_url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        page_soup = soup(webpage, 'html.parser')
        containers = page_soup.find("table","table table-hover table-bordered").find("tbody").find("td", text=precious_metal).find_next_sibling("td").text
    except:
        containers = "0"
    return containers


# --------------------------------------------------------------
# Gold, Silver, Platinum and Palladium prices
# --------------------------------------------------------------
# create empty Pandas data frames
panda_gold_df1 = pd.DataFrame()
panda_gold_df2 = pd.DataFrame()
result_gold_df = pd.DataFrame()
# create empty list
first_gold_list = []
last_gold_list = []


if not param.firstdate:
    print("No Gold Silver first date data")
    sys.exit(2)
else:
    price = first_metal_price_usd("Gold Price") 
    first_gold_list.append(["AU", "GOLD", price])
    price = first_metal_price_usd("Silver Price")
    first_gold_list.append(["AG", "SILVER", price])
    price = first_metal_price_usd("Platinum Price")
    first_gold_list.append(["PT", "PLATINUM", price])
    price = first_metal_price_usd("Palladium Price")
    first_gold_list.append(["PD", "PALLADIUM", price])
    panda_gold_df1 = pd.DataFrame(first_gold_list)
    # rename column header names in Panda Data Frame
    panda_gold_df1.columns = ['Symbol', 'Name', 'OldValue']
    print("")
    print(gold_date1.strftime('%d.%m.%Y'), "first Gold and Silver data url : ", gold_url + gold_firstdate)


if not param.lastdate:
    print("No Gold Silver last date data.")
    # sys.exit(2)
else:
    # lastdate_get_data()
    price = last_metal_price_usd("Gold Price") 
    last_gold_list.append(["AU", "GOLD", price])
    price = last_metal_price_usd("Silver Price")
    last_gold_list.append(["AG", "SILVER", price])
    price = last_metal_price_usd("Platinum Price")
    last_gold_list.append(["PT", "PLATINUM", price])
    price = last_metal_price_usd("Palladium Price")
    last_gold_list.append(["PD", "PALLADIUM", price])
    panda_gold_df2 = pd.DataFrame(last_gold_list)
    # rename column header names in Panda Data Frame    
    panda_gold_df2.columns = ['Symbol', 'Name 2', 'NewValue']
    # delete unnecessary column in Pandas Data Frame
    del panda_gold_df2["Name 2"]
    print(gold_date2.strftime('%d.%m.%Y'), "last Gold and Silver data url : ", gold_url +  gold_lastdate)


if (param.firstdate) and (param.lastdate):
    result_gold_df = pd.merge(panda_gold_df1, panda_gold_df2, how="left", on=["Symbol"])
    # create calculated column in Pandas Data Frame,  1 Ounce = 31.103 Grams
    result_gold_df["First 1 Gram USD"] = (result_gold_df['NewValue'].astype(float) / 31.103)
    result_gold_df["Last 1 Gram USD"] = (result_gold_df['OldValue'].astype(float) / 31.103)
    result_gold_df['% (+|-)'] = ((result_gold_df['NewValue'].astype(float) / result_gold_df['OldValue'].astype(float) ) -1) *100
    print("1 Ounce = 31.103 Grams")
    print("")
    print(tabulate(result_gold_df, headers=["Symbol", "Name", "First 1 Ounce USD", "Last 1 Ounce USD", "First 1 Gram USD","Last 1 Gram USD", '% (+|-)'], tablefmt="simple", numalign="right"))
    print("")    

if (param.firstdate) and (not param.lastdate):
    # create calculated column in Pandas Data Frame,  1 Ounce = 31.103 Grams
    panda_gold_df1["1 Gram USD"] = (panda_gold_df1['OldValue'].astype(float) / 31.103)
    print("1 Ounce = 31.103 Grams")
    print("")
    print(tabulate(panda_gold_df1, headers=["Symbol", "Name", "1 Ounce USD", "1 Gram USD"], tablefmt="simple", numalign="right"))
    print("")    

# 0 oz	0 Grams	
# 1 oz	31.103 Grams	
# 2 oz	62.207 Grams	
# 3 oz	93.31 Grams




