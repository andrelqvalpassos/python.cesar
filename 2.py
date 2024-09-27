# Solicita os valores ao usuário
valor_produto = float(input("Insira o valor do produto: "))
valor_desconto = float(input("Insira a taxa de desconto (%): "))

 # Calcula o valor final com desconto
valor_final = valor_produto * (1 - (valor_desconto / 100))


# Exibe o resultado
print(f"O valor final do produto com imposto será: R${valor_final:.2f}")
