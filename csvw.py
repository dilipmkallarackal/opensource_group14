import csv

def writetocsv():
    field = ['rno', 'name', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'avg']
    l = []
    n = int(input("Enter no of students:"))
    with open("Student.csv", "w", newline="") as fout:
        csvwriter = csv.writer(fout)
        csvwriter.writerow(field)
        for i in range(n):
            rows = []
            rno = int(input("rno:"))
            rows.append(rno)
            name = input("name:")
            rows.append(name)
            sub1 = int(input("sub1:"))
            rows.append(sub1)
            sub2 = int(input("sub2:"))
            rows.append(sub2)
            sub3 = int(input("sub3:"))
            rows.append(sub3)
            sub4 = int(input("sub4:"))
            rows.append(sub4)
            sub5 = int(input("sub5:"))
            rows.append(sub5)
            avg = (sub5 + sub4 + sub3 + sub2 + sub1) // 5
            rows.append(avg)
            #l.append(rows)
            csvwriter.writerow(rows)

        #csvwriter.writerow(l)


def readfromcsv():
    with open("Student.csv", newline="") as fin:
        reader = csv.reader(fin)
        ct = 0
        l = []
        for row in reader:
            #print(row)
            l.append(row)
            ct = ct + 1
        #print(ct)
        for i in range(1, ct):
            #print("For Loop, value of ct :" + str(ct) + " i:" + str(i))
            if float(l[i][7]) > 85:
                print(l[i])

writetocsv()

readfromcsv()
