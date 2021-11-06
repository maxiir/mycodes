import random


num='0','1','2','3','4','5','6','7','8','9'

cod=''
cod_full=''

#opt1
def share():

    global cod
    global cod_full

    for i in range(6): #arma digitos de 7 cifras
        cod=cod+random.choice(num)
    cod_full=cod
    cod=''
    print(cod_full)

while cod_full != '477094': #codigo q debe encontrar
    share()
    
print('Encontrado!!!:',cod_full)

    


#opt2
'''
numeros=[]

def obtener():
    global num
    global cod
    global numeros

    for i in range(6):
        cod=cod+random.choice(num) 
    numeros.append(cod)

for i in range(10):
    obtener()
    cod=''



print(numeros)
'''
        

'''
def digitos():
    global num
    global cod

    for i in range(6):
        cod=cod+random.choice(num)
    cod_completos=cod
    cod=''
    print(cod_completos)

for i in range(50):
    digitos()
    

'''






