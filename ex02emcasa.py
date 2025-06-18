meses = 3
matriz = []
nomes = []
for i in range(3):
    nomes.append(input(f'Informe o nome do {i + 1} funcionário: ').capitalize())

for i in range(len(nomes)):
    linha = []
    for j in range(meses):
        linha.append(float(input(f'Informe o salário do {nomes[i]} no {j + 1}° mês:  ')))
    matriz.append(linha)

posicao_maior = []
media_geral = 0
for i in range(len(nomes)):
    soma = 0
    for j in range(meses):
        soma += matriz[i][j]
    media_salario = soma / meses
    media_geral += media_salario
    print(f'{nomes[i]} tem uma média salarial de R${media_salario:.2f} ')
    if media_salario > 3000:
        posicao_maior.append(nomes[i])
print()
for i in range(len(posicao_maior)):
    print(f'{posicao_maior[i]} tem uma média salarial maior que R$3000.00')

media_geral = media_geral / len(nomes)
print(f'\nA média geral é de R${media_geral:.2f}')

