def inssort(d1,n):
    for i in range(n):
        temp=d1[i]
        j=i-1
        while j>=0 and temp[3]<d1[j][3]:
            d1[j+1]=d1[j]
            j=j-1
            print("While i:" + str(i) + "j:" + str(j))
        else:
            d1[j+1]=temp
            print("While i:" + str(i) + "j:" + str(j))

    for k in range(n):
            print(d1[k])

l=[]
print("\t\t\t Program using insertion sort")
n=int(input("Enter the number of products: "))
for i in range(n):
    row=[]
    id=int(input("Enter Product ID: "))
    name=input("Enter Name: ")
    qty=input("Enter Quantity ")
    price=float(input("Enter Price "))
    row.append(id)
    row.append(name)
    row.append(qty)
    row.append(price)
    l.append(row)

inssort(l,n)