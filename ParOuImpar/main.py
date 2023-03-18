pares = 0
impares = 0

valor = int(input('Digite um valor inteiro:'))

while valor > 0:
  if valor % 2 == 0:
    print(valor, "é PAR!")
    pares +=1
  else:
    print(valor, "é IMPAR!")
    impares +=1

  valor = int(input('Digite um valor inteiro:'))

print('Total de valores pares: ', pares)
print('Total de valores impares:', impares)