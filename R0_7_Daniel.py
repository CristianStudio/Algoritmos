C = int(input())
if C > 20:
 print("Solo se permite hasta 20 Caso de Prueba")

else:
  salidas = ''
  for prueba in range(C):

    num_prod = int(input())
    products = input().split()

    products_num = [int(x) for x in products ]

    if len(products) != num_prod:
      break
    else:
      products_num.sort()
      if len(products_num)%3 == 0:
        max_precio = products_num[0]
      else:
        max_precio = 0
      for i in range(1,len(products_num)):
        if i%3 == 0:
          max_precio += products_num[-i]
    salidas += str(max_precio)+ '\n'

  print(salidas)