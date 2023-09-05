#1
for i in range(0,151,1):
    print(i)

#2 
for i in range (5,1005,5):
    print(i)

#----------or-------- 
for i in range (1,101,1):
    div5 = i % 5 == 0 
    if div5:
        print(i)

#3
for i in range (1,101,1):
    div5 = i % 5 == 0 
    div10 = i % 10 == 0 
    if div5 and div10:
        print("Coding Dojo")
    elif div5:
        print("Coding")
    else:
        print(i)

#4
sumi = 0 
for i in range (0,500000,1):
    divpar = i % 2 == 0
    if not divpar:
        print(i)
        sumi = sumi + i 
print(sumi)

#5
for i in range (2018,0,-4):
    print(i)

#6 
lownum = -3
highnum = 18
mult = 3
listm = []

for i in range (lownum,highnum+1,1):
    mult2 = i % mult == 0

    if mult2:
        listm.append(i)
        print(i)


print(listm)