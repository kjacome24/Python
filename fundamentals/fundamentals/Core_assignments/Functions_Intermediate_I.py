#1--------------------------------------------------------
#1a 
def funct10(listk):
    for i in range (0,len(listk)):
        if isinstance(listk[i],list):
            for x in range (0,len(listk[i])):
                if listk[i][x]==10:
                    listk[i][x] = 15
        elif listk[i]==10:
            listk[i] = 15
    return(listk)

print(funct10([[5,2,3], [10,8,9]]))

#1b
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

print(estudiantes)
def changelastname(listk):
    listk[0]['last_name'] = 'Bryant'
    return(listk)
print(estudiantes)
changelastname(estudiantes)
print(estudiantes)

#1c

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

def changename(dict1):
    dict1['fútbol'][0] = 'Andrés'
    return dict1

changename(directorio_deportes)
print(directorio_deportes)

#1d
#way 1
z = [ {'x': 10, 'y': 10} ]
def zfun(listk):
    for key, value in listk[0].items(): #this way brings key and value with built-in method
        if value == 20:
            listk[0][key] = 30

zfun(z)
print(z)

#Way 2
z = [ {'x': 50, 'y': 20} ]
def zfun(listk):
    for x in listk[0]:
        if listk[0][x] == 20:
            listk[0][x] = 30

zfun(z)
print(z)
#2--------------------------------------------------------

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudianteslist):
    for x in range (0,len(estudianteslist)):
        z=""
        for key, value in estudianteslist[x].items():
            y = (f'{key} - {value}')
            if key == "first_name":
                z += y + ", "
            else:
                z += y
        print(z)

iterateDictionary(estudiantes) 


#3--------------------------------------------------------
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(keyword,estudentlist):
    for x in range (0, len(estudentlist)):
        for i in estudentlist[x]:
            if i == keyword:
                print(estudentlist[x][i])


iterateDictionary2("first_name",estudiantes)


#4--------------------------------------------------------

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dict1):
    for x in dict1:
        print('\n' + str(len(dict1[x])),str(x))
        for i in dict1[x]:
            print(i)



printInfo(dojo)