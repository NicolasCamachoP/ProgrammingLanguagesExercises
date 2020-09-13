import re


def read_lines(fileName):
    file = open(fileName)
    lines = file.readlines()
    file.close()
    return lines
#End def


##Solo acepta cuando el nombre y el dominio está conformado por letras
def mail_syntax_checker1(string):
    pattern = r'[A-Za-z]+@[A-Za-z]+(\.[A-Za-z]+)+'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
    #End if
#End def


##Acepta cuando el nombre tiene "_", "." y números intermedios sin repetir
##El dominio puede contener números
def mail_syntax_checker2(string):
    pattern = r'[A-Za-z]+[0-9\._]*[A-Za-z]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
    #End if
#End def


##Acepta rutas de archivo válidas
def file_path_checker(string):
    pattern = r'[A-Z]:(\\[a-zA-Z0-9_\.\s]+)+'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
    #End if
#End def


#Acepta URLs válidas
def url_checker(string):
    pattern = r'(https|http|ftp|gopher|mailto|mid|cid|news|nntp|prospero|telnet|rlogin|tn3270|wais)://[a-zA-Z0-9]*\.?[a-zA-Z0-9]+\.[a-zA-Z0-9]+/*.*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
    #End if
#End def


print('----Mails----')
lines = read_lines('correos.txt')
for line in lines:
    line = line.rstrip('\n')
    if mail_syntax_checker2(line):
        print(f'La dirección: {line} es correcta')
    else:
        print(f'La dirección: {line} es incorrecta')
#End for 
print('------------------------------------')
print('----File Paths----')
lines = read_lines('rutasArchivos.txt')
for line in lines:
    line = line.rstrip('\n')
    if file_path_checker(line):
        print(f'La ruta: {line} es correcta')
    else:
        print(f'La ruta: {line} es incorrecta')
#End for 
print('------------------------------------')
print('----URLs----')
lines = read_lines('URLs.txt')
for line in lines:
    line = line.rstrip('\n')
    if url_checker(line):
        print(f'La URL: {line} es correcta')
    else:
        print(f'La URL: {line} es incorrecta')
#End for 