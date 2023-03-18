import random

palpite = set()

while (len(palpite) < 6):
  numero = random.randint(1, 60)
  print("Número sorteado: ", numero)
  palpite.add(numero)
print(palpite)
