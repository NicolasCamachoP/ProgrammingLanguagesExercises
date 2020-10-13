import re

def mult_3_5_checker(number):
    if re.fullmatch(r"^1(([0,3,6,9][0,2,5,8])|([1,4,7][0,1,4,5,7])|([2,5,8][0,3,5,6,9]))", number):
        return True
    else:
        print(f"F en {number}")
        return False
    #End if
#End def

def check_mult_list(multiples):
    allCorrect = True
    i = 0
    while i < len(multiples) and allCorrect:
        allCorrect = mult_3_5_checker(str(multiples[i]))
        i += 1
    #End while
    return allCorrect
#End def
#------------------------------------------------------------------------------

multiples = [i for i in range(100, 200) if i%3 == 0 or i%5 == 0]

if check_mult_list(multiples):
    print("Todos los elementos de la secuencia fueron aceptados")
else:
    print("La secuencia no fue aceptada")
#End if


#Eof - Parcial.py


