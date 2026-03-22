import time
nums=[x for x in range(0,1000001)]
t1_s=time.time()
s=0
for z in nums:
    s+=z
avg=s/len(nums)
t1_e=time.time()
print("Time for avg computation manually is : ",t1_e-t1_s)
t2_s=time.time()
avg=sum(nums)/len(nums)
t2_e=time.time()
print("Time for avg computation using sum function is  : ",t2_e-t2_s)