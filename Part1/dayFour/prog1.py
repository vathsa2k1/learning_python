market_Data={
    "spot":100,
    "vol":0.2,
    "rate": 0.05
}
print(market_Data)
print(market_Data["rate"])
market_Data["rate"]=0.06
print(market_Data)
market_Data["dividend"]=0.02
print(market_Data)
for key in market_Data:
    print(key)

for value in market_Data.values():
    print(value)

for key,value in market_Data.items():
    print(key, value)

#print(market_Data["strike"])
print(market_Data.get("strike"))
## default value
print(market_Data.get("strike",100))
print(market_Data)
print(market_Data.get("strike"))