import random
tails=0
heads=0
for _ in range (1000000):
    if  random.random() >0.5 :
        heads+=1
    else :
        tails+=1
print("Number of heads is : ",heads)
print("Number of tails is : ",tails)