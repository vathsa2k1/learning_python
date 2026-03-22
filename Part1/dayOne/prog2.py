entry,exit,qty=map(float,input("Enter the entry price , exit price and qty : ").split())
order_type=int(input("Enter 1 if long else 0 if short"))
if(order_type==1):
    PnL=qty*(exit-entry)
else:
    PnL=qty*(entry-exit)
print("PnL in this case is : ",f"{PnL:.3f}")