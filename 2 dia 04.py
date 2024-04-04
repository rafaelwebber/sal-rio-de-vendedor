'''2) Uma imobiliária paga aos seus corretores um salário base de R$
1.500,00. Além disso, uma comissão de R$ 200,00 por cada imóvel
vendido e 5% do valor de cada venda. Construa um programa que
solicite o nome do corretor, a quantidade de imóveis vendidos e o valor
total de suas vendas. Ao fim, o programa deve calcular e escrever o
salário final do corretor de imóveis'''

nome = input("Digite o nome do vendedor: ")
imovel = int(input("Digite o número total de imóveis vendidos pelo vendedor: "))
vendas = float(input("Digite o valor total das vendas: "))

salario = 1500 + (200*imovel) + (5/100 * vendas/100)

print(f"O valor do salário do vendedor {nome} foi de {salario:,.2f}")