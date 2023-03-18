valor = float(input("Digite o valor do seu salário:"))
if (valor >= 800.0):
  valor = valor - 10 / 100 * valor
elif valor >= 500.0:
  valor = valor - 5 / 100 * valor
print("Valor líquido:", valor)