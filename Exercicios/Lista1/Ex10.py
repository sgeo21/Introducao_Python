produto = input("Digite o nome do produto:\n")
quantidade = int(input("Digite a quantidade de produtos vendidos:\n"))
precoUnitario= float(input("Digite o valor unitário do produto:\n"))
valorFinal= (quantidade * precoUnitario)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("    Relatório de Vendas     ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Produto: ", produto)
print("Quantidade vendida: ", quantidade)
print("Preço unitário: R$", precoUnitario)
print("Total das vendas é: R$", valorFinal)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

