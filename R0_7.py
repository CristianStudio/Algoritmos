# Ejercicio 0_7

# Gracias Dios :)

# leemos la cantidad de casos de prueba
C=int(input())

# iniciamos la salida
salida=''

# leemos cada caso de prueba
for i in range(1,C+1):
  N=int(input())          # n articulos de la lista
  valores=input().split() # valores de los articulos en string separado por espacios

  lista=[int(x) for x in valores] # metemos los valores en una lista

  if(len(lista) != N):
    break
  else:
    # ordenamos la lista
    lista=sorted(lista, reverse=True)
    #print("la lista ordenada es", lista)

    # iniciamos p para guardar los precios
    p=[]
    for j in range(1,len(lista)+1):
      # print('j es:',j)
      if( j%3==0):
        p.append(lista[j-1])
        #print('los precios a guardar son:',p)

        # guardamos la suma de los valores en las terceras componentes
        suma=sum(p)
        # print("la suma es:",suma)

    salida+= str(suma)+ '\n'
    # print('la salida parcial es:',salida)

#print(suma)
print(salida)