from config import key
import requests
import time
import csv

stocks = ["DIS","GOOGL","ME","NVAX","PFE"]

#Retrieving stock data from Polygon.io from March 29 2021 to March 25 2022
#Documentation from Polygon Aggregates https://polygon.io/docs/stocks/getting-started
for stock in stocks:
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    data = requests.get(url)
    jsonData = data.json()
    results = jsonData["results"]
    
    stockData = []

    for day in results:
        closingPrice = day["c"]
        timestamp = day["t"]
        #converting timestamp (in milliseconds) to commonly readable time format
        realTime= time.strftime("%Y-%m-%d",time.localtime(timestamp/1000))
        stockDict = {"date": realTime, "price": closingPrice}
        stockData.append(stockDict)

    #Creating .csv files using DictWriter
    with open(f"{stock}.csv", "w", newline="") as outfile:
        writer = csv.DictWriter(outfile,fieldnames=["date","price"])
        writer.writeheader()
        writer.writerows(stockData)

