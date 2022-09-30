## Türkiye Cumhuriyeti Merkez Bankası döviz kurları ve <br/> Altın, Gümüş, Platin ve Palladium fiyatları
## Central Bank of the Republic of Türkiye exchange rates and <br/> Gold, Silver, Platinum and Palladium prices

Before start to using this Python app, you have to install Python and 2 packages. <br/>
 **download and install Python 3.10 from https://www.python.org/downloads/** <br/>
 **c:\> pip install tabulate** <br/>
 **c:\> pip install pandas** <br/><br/>
This simple Python app helping to get information from Central Bank of the Republic of Türkiye. <br/> 
App reads today's currency exchange rates.  <br/>
 **c:\> python currency.py** <br/><br/>
App reads specific date currency exchange rates. <br/>
 **c:\> python currency.py -f 23.08.2022** <br/><br/> 
App reads currency exchange rates of two dates and calculating % increase/deacrease between two values. <br/>
First date is 17.12.2022 and last date is 19.01.2022 <br/>
 **c:\> python currency.py -f 17.12.2021 -l 19.01.2022** <br/></br>
If you see **Error** message, is it meaning no currency information on this date. <br/>
This is happen mostly on weekends and public holidays. <br/>
 **c:\> python currency.py -f 17.05.2021 -l 31.08.2022** <br/>
17.12.2021 - first date data is OK.  <br/> 
TCMB Currency Exchange Rates Url :  https://www.tcmb.gov.tr/kurlar/202112/17122021.xml  <br/>
15.01.2022 - last date data is NOT OK. <br/>
**Error.** Central Bank of the Republic of Türkiye, no data on this date, 15.01.2022  <br/><br/>
TCMB currency exchange rates example:
<picture>
    <img alt="Central Bank of the Republic of Türkiye and exchange rates" src="https://github.com/apoleptika/tcmb-currency-exchange-rates/blob/main/tcmb-currency.png">
</picture>

You can also check **GOLD and SILVER** prices with another application.<br/>
For today's gold and silver prices. <br/>
**c:\> python goldsilver.py** <br/><br/>
For gold and silver prices for a given day. <br/>
**c:\> python goldsilver.py -f 31.08.2022** <br/><br/>
For gold and silver prices on two different dates <br />
**c:\> python goldsilver.py -f 05.01.2021 -l 30.08.2022** <br/><br/>
Gold and Silver example:
<picture>
    <img alt="Gold and Silver prices" src="https://github.com/apoleptika/tcmb-currency-exchange-rates/blob/main/gold-silver-prices.png">
</picture>

Aldin Romanov Aldinov
