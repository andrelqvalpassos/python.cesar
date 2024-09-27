#Solicita os valores

valor_total_vendas = float(input("Digite o valor da venda: "))
porcentagem = float(input("Qual o valor da porcentagem: "))

#Executa a conta

comissao = valor_total_vendas * (porcentagem / 100)

#Imprime resultado
print(f"O valor que voce ira receber e: R${comissao} ")