squares=[]
for i in range(5):
    squares.append(i**2)
print(squares)

squares_2=[]
squares_2=[x**2 for x in range(5)]
print(squares_2)

roots=[]
roots=[x**(1/2) for x in squares_2]
print("Printing Roots!")
print(roots)
print("Printing squares minus 100")
res=[x-100 for x in squares_2]
print(res)

## Choosing squares greater than 15 
squares_3=[x**2 for x in range(10)]
sub_squares=[x for x in squares_3 if x>15]
print(sub_squares)

## Call option payoff 
spot=[x for x in range(90,110)]
strike=100
payoff=[max(p-strike,0) for p in spot]
print(payoff)

# Nested list comprehension
matrix=[[i+j for j in range(3)] for i in range(3) ]
print(matrix)

### Dictionary Comprehension
prices =[x for x in range(100,110)]
print("Prices list : ",prices)
gg=enumerate(prices)
print(gg)
price_dict={i:p for i,p in gg}
print(price_dict)