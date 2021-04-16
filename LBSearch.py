def lsearch(l1,n,item):
    f=0
    for i in range(n):
        if l1[i]==item:
            print(item," found at ",i+1," position")
            f=1
            break

    if(f==0):
        print(item," not found")

def bsearch(l1,n,item):
    last=n-1
    mid=0
    f=0
    b1=0
    while b1<=last:
        mid=(b1+last)//2
        if l1[mid]==item:
            print(item," found at position ",mid+1)
            f=1
            break
        elif l1[mid]<item:
            b1=mid+1
        else:
            last=mid-1
    if(f==0):
       print(item," not found ")

rep='y'
while(rep=='y'):
    print("1. Linear Search\n 2. binary Search")
    ch=int(input("Enter choice "))
    l=[]
    if(ch==1):
        n1=int(input("Enter the number of strings "))
        for i in range(0,n1):
            a=input("Enter the string ")
            l.append(a)

        item=input("Enter the string to search ")
        lsearch(l,n1,item)

    elif(ch==2):
        l=[]
        n1=int(input("Enter the number of strings "))
        for i in range(0,n1):
            a=input("Enter the string in ascending order ")
            l.append(a)

        item=input("Enter the string to search ")
        bsearch(l,n1,item)
        rep=input("Continue ")
