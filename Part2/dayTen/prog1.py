import time
start=time.time()
for i in range(1000000): 
    x=i*i
end=time.time()
print("Execution time is : ", end-start)