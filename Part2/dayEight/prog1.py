x=10
y=0
#print(x/y)
# try:
#     res=x/y
# except:
#     print("Something seems wrong!!")
# try:
#     res=x/y
# except ZeroDivisionError:
#     print("Quotient seems to be zero!!")
# try:
#     x=float(input("Enter a number : "))
#     print("Number was entered ")
# except ValueError:
#     print("You didn't enter a number")
# try :
#     res=9/2
# except ZeroDivisionError:
#     print("Quotient is 0")
# else:
#     print("Result",res)
# try:
#     res=9/0
# except ZeroDivisionError:
#     print("Quotient is 0")
# finally:
#     print("Ending the execution !! Goodbye !!")
def multiplier(val):
    if val<10:
        raise ValueError("Val can't be less than 10!!")
    return val*10
x=float(input("Enter a number for val : "))
res=multiplier(x)
print(res)