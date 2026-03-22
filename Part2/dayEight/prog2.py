# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Quotient is zero !")
#         return None
def safe_divide(a,b):
    if b==0:
        return None
    return a/b
a,b=map(float,input("Enter two numbers for division : ").split())
print("The result of division is : ",safe_divide(a,b))