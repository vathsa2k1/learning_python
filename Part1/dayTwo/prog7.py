def call_payoff(spot,strike):
    return max(spot-strike,0)
strike=100
for spot in range(80,121):
    print(f"Spot:{spot}, Payoff:{call_payoff(spot,strike)}")
print("Done")