# def call_payoff(spot,strike):
#     payoff=max(spot-strike,0)
#     return payoff
# print(call_payoff(10,20))
# for p in range (90,110):
#     #print(call_payoff(p,100))
#     p=call_payoff(p,100)
#     print(p)
# def bond_pricing(face=100,rate=0.05,years=5):
#     p=face/((1+rate)**years)
#     print(p)
# bond_pricing()
# bond_pricing(face=200)
# bond_pricing(rate=0.10)
# bond_pricing(years=10)
# def stats_def(numbers):
#     minimum=min(numbers)
#     maximum=max(numbers)
#     average=sum(numbers)/len(numbers)
#     return minimum,maximum,average
# data=[1]
# for i in range(2,11):
#     data.append(i)
# minimum_data, maximum_data, average_data =stats_def(data)
# print("Minimum is : ",minimum_data)
# print("Maximum is : ",maximum_data)
# print("Average is : ",average_data)
def test():
    x=10
    print(x)
test()
print(x)