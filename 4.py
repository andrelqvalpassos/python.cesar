#Solicita os valores

valor_inicial = float(input("Digite um valor: "))
taxa_de_juros = float(input("Digite o valor do juros: "))
tempo = int(input("Qual o tempo em (anos): "))

#Executa a conta

valor_futuro = valor_inicial * (1 + (taxa_de_juros / 100))

print(f"O valor futuro apos {tempo} anos será: R${valor_futuro} ")