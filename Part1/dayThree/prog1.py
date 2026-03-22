print("Srivathsa")
prices=[983,657,847,754,908]
print(prices)
data=["Srivathsa",'A',24,76.3]
print(data)
print("Appending : ")
prices.append(321)
data.append(173.2)
print(prices)
print(data)
print("popping : ")
prices.pop()
data.pop()
print(prices)
print(data)
print("Looping through the list : ")
for i in prices :
    print(i)
print("Length of the list prices is : ",len(prices))
print("Calculating the average price : ")
sum=0
for i in prices :
    sum+=i
print("The average price is : ",sum/len(prices))