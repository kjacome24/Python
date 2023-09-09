
x = input("Please type an integer from 2 to 1000:")

def extrap (y):
        while not y.isdigit() or int(y) >= 2001 or int(y) <= 1:
            y = input("Please type an integer from 2 to 1000:")
        else:
            y = int(y)
            ###Code for pair numbers
            divy = y % 2 == 0 
            if divy:
                print("Número par")
            else:
                print("Número no es par")
            ###Code for prime numbers
            countx = 0
            vardivz = []
            for x in range (1,y+1):
                divx = y % x == 0
                if divx:
                    countx = 1 + countx
                    vardivz.append(x)
                else:
                    countx = countx
            if countx == 2:
                print("Es un número primo")
            else:
                print("No es un número primo")
            print("Conjunto de divisores:")
            for zx in range (0,len(vardivz)):
                print(vardivz[zx])
            ####

extrap(x)

######Long code agains errors
# print("Please type an integer from 2 to 1000")
# x = input()

# def extrap (y):
#     while True:
#         try:
#             while not y.isdigit() or int(y) >= 2001 or int(y) <= 1:
#                 y = input("Please type an integer from 2 to 1000")
#             else:
#                 y = int(y)
#                 print("All good")
#                 break
#         except:
#             continue
#             # print("error")
# extrap(x)

######example
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
