n=int(input("Enter a num:"))
for i in range(0,n):
    for j in range(0,i+1):
        print(n,end="")
    n=n-1        
    print("\n")        