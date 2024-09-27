#Solicita os valores

valor_total_compra = float(input("Qual o valor total da compra: "))
parcelas = float(input("Qual o numero de parcelas: "))

#Executa a conta
valor_parcelas = valor_total_compra / parcelas

print(f"De acordo com o numero de parcelas o será: R${valor_parcelas:.2f}")