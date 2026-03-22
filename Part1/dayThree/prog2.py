import random
prices=[100]
val=prices[0]
for _ in range(11):
    val=val+random.uniform(-5,5)
    prices.append(val)
print(prices)
print(max(prices))
print(min(prices))
total=0
for i in prices :
    total+=i
print("Length of list is : ",len(prices))
print("Average price over ",len(prices)," observations is : ",total/len(prices))