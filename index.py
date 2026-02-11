# amadeo = 0

# while amadeo < 10 :
#     print(amadeo , end=" * ")
#     amadeo += 1

# print("\n\n")

# for amadeo in range (40,14,-5) :
#     print(amadeo , end=" - ")


# for i in range (2, 8, 3) :
#     print(i)


# import time

# for segundo in range(15):
#     print(f'{segundo} ')
#     time.sleep(segundo/5)
# print("\n\ngame over")


# print("la instruccion break: ")

# for b in range (1,6) :
#     if b == 3 :
#         break
#     print(f'Dentro del bucle break: {b}')


# print('\n ejemplo con continue : ')
# yoma = 3, 5

# for c in range(1,15):
#     if  (5 <= c < 8) or c==11 :
#         continue
#     print(f"dentro del continue : {c}")

# print('\n\nfuera del bucle')

# numero_mayor = -99999999

# contador = 0

# while True :
#     numero = int(input('Introduce un numero o escribe -1 para salir : '))
#     if numero == -1 :
#         break
#     contador += 1
#     if numero > numero_mayor :
#         numero_mayor = numero

# if contador != 0:
#     print(f'el numero mas grande es : {numero_mayor}')
# else:
#     print('no has ingresado ningun numero')


# while True :
#     palabra = input('estas en un bucle infinito !! \n Ingresa la palabra secreta :')
#     if palabra == 'chupacabra' :
#         break

# print(f'\n\nhas salido del bucle : {palabra}')


# palabra = input("Introduzca la palabra : ")
# palabra = palabra.upper()
# nuevo = ''


# for letra in palabra : 
#     if letra == 'A':
#         continue
#     elif letra == 'E':
#         continue
#     elif letra == 'I' :
#         continue
#     elif letra == 'O' :
#         continue
#     elif letra == 'U' :
#         continue
    
#     else:
#         nuevo += letra
#         print(letra)

# print(f'\n\n {nuevo}')    

# bloques = int(input("ingrese la cantidad de bloques : "))

# altura = 0
# en_capa = 1

# while en_capa <= bloques :
#     altura += 1
#     bloques -= en_capa
#     en_capa += 1

# print(f'la altura de la piramide es : {altura}')

# texto = "pyxpyxpyxpyxpyxpy"

# for letra in texto :
#     if letra == "x":
#         continue
#     print(letra, end="")
    
numeros = [10, 5 , 7, 2 , 1]

# print(f'el valor original de la lista es : {numeros}')

# numeros[0] = 111 
# print(f'\nel valor actual de la lista es : {numeros}')

# numeros[1] = numeros[4]
# print(f'\nel valor actualizado del numero 2 es : {numeros} ')

print(numeros[0])
print(f'\n{numeros}')

print(f'\n{len(numeros)}')

del numeros[1]

print(f'\n nueva longitud , despues de borrar : {len(numeros)}')

# print(numeros[4])
# numeros[4] = 10
# print(f'\n{numeros[4]}')



























# for i in range(100) :
#     if i % 2 == 1 or i% 5== 0:
#         print(f'el de valor de i es : {i} ', end=" * ")


# numero_secreto = 777 

# numero = int(input("ingrese el numero : ")) 


# while numero != numero_secreto :
#     print(f'el numero secreto esta incorrecto -- loop ')
#     numero = int(input("ingrese el numero otra vez : "))
#     if numero == -999 :
#         print(f'definitivo : te diste por vencido')
#         break
#     else :
#         continue

# print(f'\n \nel numero secreto es : {numero_secreto} ')

i = 0

# while i < 100 :
#     print(f'i : {i}' , end=" ; ")
#     i += 5

# for i in range(0,100,5) :
#     print(f' \n\n i : {i}' , end=" ; ")

# for i in range (10, 15) :
#     print(f'i : {i} ')

# for i in range (3,-2 , -2) :
#     print(f'i : {i}')
    
# potencia = 1

# for expo in range (17):
#     print(f' 2 a la potencia de {expo} es igual a : {potencia}')
#     potencia *= 2


# for i in range(2, 8, 3) :
#     print(f'el valor de i es : {i}')

# import time

# for s in range (1, 6) :
#     print(s , 'missisipi')
#     time.sleep(1)

# print('\nlistos o no , ahi voy')

# print('la instruccion break')

# for i in range (1,6) :
#     if i == 3 :
#         break
#     print(f'dentro del bucle : {i}')

# print(f'\nfuera del loop , i es : {i}')

# print('\n\n ahora ... ejemplo con continue')

# for i in range (6) :
#     if i % 2 == 1 :
#         continue 
#     print(f'dentro del bucle : {i}')
# print(f'\n\nfuera del bucle {i}')

# numero_mayor = -99999999
# contador = 0

# while True :
#     numero = int(input("introduzca -1 para finalizar : "))
#     if numero == -1 :
#         break
#     contador += 1
#     if numero > numero_mayor :
#         numero_mayor = numero 

# if contador != 0 :
#     print(f'el numero mayor es : {numero_mayor}')

# else:
#     print(f"no has introducido ningun numero")

#####################################################################

# numero_mayor = -99999999

# contador = 0

# numero = int(input("Ingrese un numero o digite -1 para finalizar el programa : "))

# while numero != -1 :
#     contador += 1
#     if numero > numero_mayor :
#         numero_mayor = numero
#     numero = int(input("Ingrese un numero o digite -1 para finalizar "))

# if contador :
#     print(f'el numero mayor es : {numero_mayor}')

# else:
#     print(' no has ingresado un numero ')


#############################################################


# while True :
#     palabra = input(" esta en un loop infinito \n ingrese una palabra para salir de el: ")
#     if palabra == "chupacabra":
#         break

# print(f'\n\nconseguiste la palabra correcta : {palabra}')



##############################################################

# palabra = input("introduce una palabra : ")
# resultado = ""
# palabra = palabra.strip().upper()

# # print(f'la palabra es {palabra}')

# for p in palabra :
#     if  p == "A" :
#         continue
#     elif p == "E" :
#         continue
#     elif p == "I" :
#         continue
#     elif p == "O" :
#         continue
#     elif p == "U" :
#         continue
#     elif p == " ":
#         p = "*"
    
    
#     resultado += p
    
   

# print(f'\n\nla palabra sin vocales es : {resultado}', end="")


##############################################################################

# i = 6
# #ahora aplicaremos la sentencia while
# while i < 5 :
#     print(f'el valor de i es : {i}')
#     i += 1
# #ahora imprimiremos
# print(f' i por fuera es : {i}')

# for r in range(5) :
#     print(f'dentro del loop : {r}')

# else :
#     print(f'else  : {r}')

# bloques = int(input("introduce la cantidad de bloques : "))

# altura = 0
# en_capa = 1

# while en_capa <= bloques :
#     altura += 1
#     bloques -= en_capa
#     en_capa +=1

# print(f'la altura de la piramides es : {altura}')

#######################################################

# while True :
#     print("agarrados en un blucle")

# contador = 5
# while contador > 2 :
#     print(contador)
#     contador -= 1

#######################################################
# palabra = "Python"

# for letra in palabra :
#     print(letra, end="*")


#################################################

# for i in range (1,10) :
#     if i % 2 == 0:
#         print(i)


########################################################

# texto = "Estamos trabaJando en el sistema global de IA"

# for letra in texto :
#     if letra == "J" :
#         break
#     print(letra, end="")

#######################################################

# texto = "pyxpyxpyx"
# for letra in texto :
#     if letra == "x" :
#         continue
#     print(letra, end="")


#########################################################

# for i in range (3) :
#     print(i, end =" ")

# for r in range(6, 1, -3) :
#     print(r, end=" ")

#########################################################

# for i in range (1, 11) :
#     if i % 2 == 0 :
#         print(i)

# x = 1 

# while x < 11:
        
#     if x % 2 == 0 :
#         print(x)
#     x += 1
    










# impar = 0
# par = 0

# numero = int(input("Introduzca un numero , o tipee 0(cero) para detener :"))

# while numero != 0 :
#     if numero % 2 == 1 :
#         impar += 1

#     else :
#         par +=1

#     numero = int(input("Introduzca un numero , o tipee 0(cero) para detener :"))

# print(f"La cantidad de numeros impares es : {impar}")
# print(f"La cantidad de numeros pares es : {par}")

# ////////////////////////////////////////////////////

# contador = 5

# while contador != 0 :
#     print(f"Dentro del loop , contador en : {contador}")
#     contador -= 1

# print(f"Fuera del loop , contador en : {contador}")



# ////////////////////////////////////


# contador = 5

# while contador :
#     print(f"Dentro del loop : {contador}")
#     contador -= 1 

# print(f"Fuera del loop : {contador}")

# /////////////////////////////////////////////////////////

# secreto = 777
# num = int(input("Introduca el numero de la suerte : "))
# while num != secreto :
#     num = int(input("Introduzca el numero de la suerte : "))
#     print (f"Estas en un loop , el numero secreto no es : {num} ")

# print(f"Lo lograste , el numero secreto es : {num}")


# ////////////////////////////////////////////////////////////
# i=10

# for i in range(5,10,2) :
    
#     print(f"El valor del contador es : {i}")

# ///////////////////////////////////////////////

# potencia = 1

# for expo in range (16):
#     print(f"2 a la potencia de {expo} es igual a   {potencia}")
#     potencia *= 2


#///////////////////////////////////////////////////////////////////

# import time

# for segundo in range (1,6) :
#     print(f"{segundo} Mississisipi")
#     time.sleep(3)

# print(f"Listos o no , hemos terminado !")

    
# ///////////////////////////////////////////////

# for i in range (1,6):
#     if i == 3 :
#         break
#     print(f"contador en {i} : dentro del loop")

# print(f"contador en {i} : FUERA DEL LOOP")
# print()

# #EJEMPLO DE CONTINUE

# for i in range(1,6):
#     if i == 3 :
#         continue
#     print(f"el contador {i} : define el continue")

# print(f"el contador en {i} , termina el conteo")

# ////////////////////////////////////////////////////////////////////

# while True :
#     palabra = input("Introduzca la palabra : ")
#     if palabra == "python" :
#         break
#     else:
#         print(f"{palabra} no es lo que busco , estas en un bucle infinito ..... \n")

# print(f"felicidades : {palabra} es lo que buscaba , has salido del bucle")


# //////////////////////////////////////////////////////////////////////

# palabra = input("introduzca una palabra : ")
# palabra = palabra.upper()
# yo = ""

# for letra in palabra :
#     if letra == "A" :
#         continue
#     if letra == "E" :
#         continue
#     if letra == "I" :
#         continue
#     if letra == "O" :
#         continue
#     if letra == "U" :
#         continue
#     else : 

#         yo += letra
#         print(f"La letra es : {letra} \n")

# print(f"La palabra sin vocales es : {yo}")

# ///////////////////////////////////////////////////////////////


# palabra = "Python"
# for letra in palabra :
#     print(letra, end="*")

# ///////////////////////////

# for i in range(1,10) :
#     if i % 2 == 0 :
#         print(i)

# //////////////////////////////


# texto = " Estamos aprendiendo python "

# for letra in texto :
#     if letra == "o" :
#         break
#     print(letra , end="")

#//////////////////////////////////


# texto = "pyxpyxpyx"
# for letra in texto:
#     if letra == "x" :
#         continue
#     print(letra , end="")


#///////////////////////////////////

# for i in range(3) :
#     print(i, end=" ")

# for i in range(6,1 , -1) :
#     print(i, end=" ")


# //////////////////////////////////////
# for ch in "franciscoh@gmail.com" :
#     if ch == "@" :
#         break
#     print(ch,end="")

# //////////////////////////////////////

# for digit in "0165031806510" :
#     if digit == "0" :
#         print("x", end="")
#         continue
#     print(digit , end="")

# ///////////////////////////////////

# n = range(4)

# for num in n :
#     print(num - 1)
# else :
#     print(num)

# ////////////////////////////////////////////

# for i in range(0,6,3):
#     print(i)

#  ////////////////////////////////////////////

# numeros = [10, 5, 7, 2 , 1]

# print(f" Lista original de contenidos :  {numeros}")

# numeros[0] = 111
# print(f"\n Lista actualizada : {numeros}")

# numeros[1] = numeros[4]
# print(f"Nueva lista de contenido : {numeros}")

# print(f"\n Longitud de la lista : {len(numeros)}")

# del numeros[1]
# print(f"nueva longitud de la lista : {len(numeros)}")

# print(numeros)

# print(numeros[-1])

# print(numeros[-2])

# print(numeros[-4])

# print(numeros[0])


# ///////////////////////////////////////////////////////////////////////

# lista_sombrero = [1, 2, 3 , 4 ,5]

# lista_sombrero[2] = 9

# del lista_sombrero[-1]

# print(len(lista_sombrero))

# print(lista_sombrero)

# ////////////////////////////////////////////////////////////////////////////////////////////

# numeros = [111, 7, 2 ,1 ]

# print(f"longitud {len(numeros)}")

# print (numeros)

# numeros.append(4)
# print(f"\n {numeros}")

# numeros.insert(1, 222)
# print(f"\n \n nueva longitud {len(numeros)}")

# print(numeros)

# /////////////////////////////////////////////////////////////////////////////////////////

# primera=[]

# for i in range(5) :
#     primera.append( i + 1)

# print(primera)


# lista = []

# for i in range(5) :
#     lista.insert(0, i + 1)

# print(lista)

# lista = []

# ////////////////////////////////////////////////////////////////////////////////////////////

# milista = [10, 1, 8 , 3 , 5]
# total = 0

# for i in milista :
#     total += i

# print(total)

# ///////////////////////////////////////


