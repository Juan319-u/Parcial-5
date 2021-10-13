'''Este codigo verifica que numeros son perfectos
verifica los numeros perfectos del rango desde 1 hasta x
verifica si x es un numero ore
Autor : Juan  Felipe  Corrales  Toro
Parametros: N el numero mayor del rango para numeros a escoger 
ULTIMA  ACTUALIZACION : 13  de  Octubre  /  2021'''
import random #importo libreria random para usar sus funciones de numeros aleatorios
divisores={}
perfecto={}
noperfecto={}

def esperfecto(x):#creamos la funcion que comprueba si x es un numero perfecto
    suma=0
    for i in range(1,x):#este for sirve para pasar por todos los numeros desde 1 hasta x
        if x % i == 0:
            suma+=i #si la division da modulo 0 a la variable suma se le suma i 
            divisores[i]=i
    return suma == x #si la suma es igual a x el retorno dara True sino dara False


decision=input("desea agregar el numero si/no? ")
if decision == "si":
    x=int(input("ingresa el numero que deseas verificar si es perfecto "))
else:
    n=int(input("ingrese el rango max de la muestra ")) #aqui solicitamos el numero de mayor del rango a numeros a escoger
    x=random.randint(1,n) #se escoge el numero al azar entre 1 y n 
    print("el numero al azar escogido fue",x)
    
    
if esperfecto(x)==True: #condicional para imprimir 
    print(x," es un numero perfecto")
    print("sus divisores son :")
    listaDeDivisores = divisores.values() #en una variable sacamos los valores del diccionario divisores
    listaDeDivisores = list(listaDeDivisores) #convertimos la variable en una lista
    print(listaDeDivisores)
else: 
    print(x, "no es un numero perfecto")
    print("sus divisores son :")
    listaDeDivisores = divisores.values()
    listaDeDivisores = list(listaDeDivisores)
    print(listaDeDivisores)

    
for i in range(1,x+1): #con este for contamos la cantidad de numeros perfectos desde 1 hasta x+1
    if esperfecto(i)==True:
        perfecto[i]=i
    else:
        noperfecto[i]=i
            
            
cont=len(perfecto) #con la funcion len contamos cuantos numeros hay en el diccionario perfecto
print("hay entre el 1 y ",x," esta cantidad de perfectos :",cont)
print("hay entre el 1 y ",x," esta cantidad de no perfectos :",len(noperfecto))
listap=perfecto.values()
listap=list(listap)
print("esta es la lista de perfectos :")
print(listap)
print("el porcentaje de numeros perfectos desde 1 hasta ",x," es ",cont/x,"%")


print("se realiza el calculo para saber si ",x," es un numero ore")
suma=sum(listaDeDivisores)+x
h=len(listaDeDivisores)+1
calculo=(x*h)/suma #realizamos el calculo para saber si es un numero ore
print("el resultado es ",calculo)
if (x*h)%suma==0: #con este condicional si la variable calculo da residuo 0 significa que el numero x es de ore
    print(x," es un numero de ore")
else:
    print(x," no es un numero de ore")