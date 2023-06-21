import re
import csv

# Read the raw file
file = open('website_content_2days.txt', 'r', encoding='utf-8')
content = file.read()

# Set your parameters
target = ["No","IDStockSummary","Date","StockCode","StockName","Remarks","Previous","OpenPrice","FirstTrade","High","Low","Close","Change","Volume","Value","Frequency","IndexIndividual","Offer","OfferVolume","Bid","BidVolume","ListedShares","TradebleShares","WeightForIndex","ForeignSell","ForeignBuy","DelistingDate","NonRegularVolume","NonRegularValue","NonRegularFrequency","persen","percentage"]
chars = ["[",",{","{","]"]

# Remove html relics
content = re.sub(r'{"draw".*?,"data":', '', content)

# Remove the repetitive parameter for each stock
for param in target:
    pattern = rf'"{param}".*?:'
    content = re.sub(pattern, '', content)

# Remove unnecessary characters and devide each stock with new line
for char in chars:
    strip = rf'\{char}'
    content = re.sub(strip,'', content)
    content = re.sub("}","\n", content)

# Write the content to a file
outFile =  open('sample_test.csv', 'w', encoding='utf-8')
top = ",".join(target)
outFile.write(f"{top}\n")
outFile.write(content.strip())






