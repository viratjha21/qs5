# To get a list from the number 1 to 100 which are divisible by 4 and 5
n=int(input("enter the number ="))
# L1=list(range(1,n))
# M1=[]
# for i in L1:
#     m=i*i*i
#     if m%4==0:
#         M1.append(i)
#     elif m%5==0:
#         M1.append(i)  
# print(M1)         
L=[]
M=[]
for i in range(1,n+1):
    L.append(i)
for j in L:
    s=j*j*j
    if s%4==0:
        M.append(j)
    elif s%5==0:
        M.append(j)
print(M)            

    
    
   

