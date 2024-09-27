# Solicita os valores ao usuário
valor_produto = float(input("Insira o valor do produto: "))
taxa_imposto = float(input("Insira a taxa de imposto (%): "))

 # Calcula o valor final com o imposto
valor_final = valor_produto * (1 + (taxa_imposto / 100))


# Exibe o resultado
print(f"O valor final do produto com imposto será: R${valor_final:.2f}")
