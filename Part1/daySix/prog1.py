name="Srivathsa Anandgal"
print(name)
print(type(name))
print(name[0:6])
print(name[6:])
print(name.upper())
print(name.lower())
print(name)
sentence="Srivathsa Anandgal is from Hyderabad!!"
print(sentence.replace("Hyderabad","Mumbai"))
words=sentence.split()
sentence_2="Srivathsa, Anandgal is, from, Hyderabad!!"
words_2=sentence_2.split(",")
print(words_2)
f=321.789654
print("Normal print statement : ",f)
print(f"The f string way gives : {f}")
print(f"F string restricted to 2 decimals : {f:.2f}")
spot=100
strike=105
payoff=0
print(f"The spot is : {spot}, the strike is : {strike}, the patoff is : {payoff}")
price = 105
payoff = 5

print(f"Price: {price:>2}  Payoff: {payoff:>5}")## Spacing 