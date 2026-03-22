principal=1000
rate=25
time=8
si=principal*rate*time/100
ci=principal*(1+(rate/100))**time -principal
print("SI : ",f"{si:.3f}")
print("CI : ",f"{ci:.1f}")

entry =100
exit=190
qty=1250
PnL=qty*(exit-entry)
print("PnL : ",PnL)

p,r,t=map(float,input("enter p , r and t : ").split())
si=p*r*t/100
ci=p*(1+(r/100))**t -p
print("SI : ",f"{si:.3f}")
print("CI : ",f"{ci:.1f}")
