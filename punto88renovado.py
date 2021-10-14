'''Este codigo verifica que la expresion 6 dividido pi al cuadrado
es igual a casos favorables sobre casos posibles de los numeros enteros libres de cuadrados
Autor : Juan  Felipe  Corrales  Toro 
ULTIMA  ACTUALIZACION : 13  de  Octubre  /  2021'''
#está función toma de entrada un entero positivo mayor que 1 y muestra los factores primos de él, su salida es un vector.
def descomponer_factores(n):   
    factor_primo = 2
    factores = []
    
    while n>1:
        if n % factor_primo == 0:
            n //= factor_primo  #función actualiza el n, con la parte entera (menor entero) de n al dividir por el factor primo
            factores.append(factor_primo)
            
        else:
            factor_primo += 1
            
            
    return factores #devuelve el vector de factores primos con repeticiones   


def frecuencia(lista):
    f = []
    unique_list = list(set(lista)) #se queda sólo con los valores son repetición
    for i in unique_list:
        f.append(lista.count(i))
    return len(f)


# calcula la cantidad de enteros libres de cuadrados hasta un n y su probabilidad

def libre_cuadrados(n):
    c = 0
    for z in range(2,n+1,1):
        lista_factores = descomponer_factores(z)
        
        if  len(lista_factores) == frecuencia(lista_factores):
            c=c+1
            
        else:
            continue
            
    print('Cantidad de enteros libres:', c)
    print('P(z libre)=', c/n)


for n in range(2,1000,1):
    print(libre_cuadrados(n))