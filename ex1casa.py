linhas = 3
colunas = 7
matriz = []
cidades = []


for i in range(linhas):
    cidades.append(input(f'Digite a {i + 1}° cidade: '))
    linha = []
    for j in range(colunas):
        linha.append(float(input(f'Informe a temperatura do {j + 1}° dia da semana: ')))    
    matriz.append(linha)

print()

for i in range(linhas):
    print(f'{cidades[i]:15}', end = '')
    for j in range(colunas):
        print(f'{matriz[i][j]:10}', end = '')
    print()


print()
#A temperatura média da semana para cada cidade.
for i in range(linhas):
    soma_temp = 0
    for j in range(colunas):
        soma_temp += matriz[i][j]
    temp_media = soma_temp / colunas
    print(f'Em {cidades[i]}, a temperatura média é de {temp_media:.2f}°C')


print()
#A maior temperatura registrada e a cidade e o dia em que ocorreu.
maior_temp = 0
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior_temp:
            maior_temp = matriz[i][j]
            cidade_maior_temp = cidades[i]
print(f'A maior temperatura é de: {maior_temp:.2f}°C em {cidade_maior_temp}')


print()
#A média geral de todas as temperaturas.
soma_total = 0
cont = 0
for i in range(linhas):
    for j in range(colunas):
        soma_total += matriz[i][j]
        cont += 1
media_geral = soma_total / cont
print(f'A média geral de todas as temperaturas é de: {media_geral:.2f}°C')
