import math
import re

def suma (string):
    pattern = "(\-?\d+)"
    operandos = re.findall(pattern, string)
    if operandos != None:
        total = 0
        for i in range(len(operandos)):
            total += int(operandos[i])
        #End for
        return total
    else:
        return "Input mal formado!"
    #End if
#End def

def operation(string):
    expression = []
    size = 0
    expression.append("")
    vacio = False
    for i in range(len(string)):
        print(string[i])
        if string[i].isdigit():
            if i > 0:
                if (string[i-1] == '-'):
                    expression[size] += string[i-1]+string[i]
                else:
                    expression[size] += string[i]
                #End if    
            else:
                expression[size] += string[i]
            #End if
        elif string[i] != '-' and string[i] != '':
            size += 2
            expression.append( string [i] )
            expression.append("")
        #End if
    #End for
    print(expression)
    resultado = float(expression[0])
    i =1
    while(i < len(expression)):
        if (expression[i] == "+"):
            print(f'Resultado {resultado} operador {expression[i]} operando {expression[i+1]}')
            resultado += float(expression[i + 1])
        elif(expression[i] == "*"):
            resultado *= float(expression[i + 1])
        elif(expression[i] == "/"):
            resultado /= float(expression[i + 1])
        elif(expression[i] == "%"):
            resultado %= float(expression[i + 1])
        i += 2
    #End for
    return resultado
#End def
    
print('Ingrese la operación aritmética aritmética: ', end = '')
operacion = input()
print(f"El resultado de la operación es: {operation(operacion)}")