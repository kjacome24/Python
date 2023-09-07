#1 
def countdown(num):
    listk = []
    for i in range(num,-1,-1):
        listk.append(i)
    return listk

x = countdown(6)
print(x)

#2 
def print_return(listk):
    lenv = len(listk)
    if lenv==2:
        print(listk[0])
        return(listk[lenv-1])
    else:
        print("The list has more than two values")

x = print_return([1,2,3])
print(x)

#3
def first_length(listk):
    lenx = len(listk)
    first = listk[0]
    return(lenx+first)

print(first_length([1,2,3,4,5]))

#4 

def higher_than(listk):
    newlist = []
    if len(listk)>=2:
        valuex = listk[1]
        for i in listk:
            if i>valuex:
                newlist.append(i)
        print(len(newlist))
        return(newlist)
    else:
        return("False")

print(higher_than([2]))

#5 
def weight_value(a=0,b=0):
    if isinstance(a,int) and isinstance(b,int) :
        newlist = []
        for i in range (0,a):
            newlist.append(b)
        return(newlist)
    else:
        print("Any of the inputs is not an integer")

print(weight_value(6,2))

