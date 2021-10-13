'''Este codigo verifica que la expresion 6 dividido pi al cuadrado
es igual a casos favorables sobre casos posibles de los numeros enteros libres de cuadrados
Autor : Juan  Felipe  Corrales  Toro
Parametros: N el numero mayor del rango para numeros a escoger 
ULTIMA  ACTUALIZACION : 13  de  Octubre  /  2021'''
import math
numeroslibres=[1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 51, 53, 55, 57, 58, 59, 61, 62, 65, 66, 67, 69, 70, 71, 73, 74, 77, 78, 79, 82, 83, 85, 86, 87, 89, 91, 93, 94, 95, 97, 101, 102, 103, 105, 106, 107, 109, 110, 111, 113]
x=len(numeroslibres)
casosposibles=113
cal=x/casosposibles

calculo=6/(math.pi**2)
dife=cal-calculo
print("este es la diferencia con respecto al calculo correcto ",calculo-cal)
print("este es el resultado correcto ",calculo)
print("este es nuestro calculo ",cal)