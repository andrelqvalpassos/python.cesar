#Solicita os valores

custo_producao = float(input("Qual o valor do custo: "))
preco_venda = float(input("Qual o da venda: "))

#Executa a conta

lucro_liquido = preco_venda - custo_producao

#Imprime resultado
print(f"O seu lucro será: R${lucro_liquido:.2f}")