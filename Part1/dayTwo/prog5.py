strike=100
for spot in range(80,121):
    #print("Payof at expiry when spot is ", i ," is : ",max(i-strike,0))
    payoff=max(spot-strike,0)
    print(f"Spot:{spot}, Payoff:{payoff}")
print("Done")