# Exercício - sistema de perguntas e respostas
from time import sleep

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


cont = 0
for pergunta in perguntas:
    
    print(f"\nPergunta: {pergunta['Pergunta']}")
    print('\nOpções:')
    for i, opcao in enumerate(pergunta['Opções'], start=1):
        print(f'{i}) {opcao}')
    
    for i in range(len(pergunta['Opções'])):
        if pergunta['Opções'][i] == pergunta['Resposta']:
            certo = i 

    while True:        
        try:
            escolhido = int(input('Escolha uma opção: '))
            if 1 <= escolhido <= len(pergunta['Opções']):
                break
        except ValueError:
            print()
            print('Entrada incompátivel... Tente novamente')
            print()
    if escolhido -1  == certo:
        sleep(0.5)
        print('\n\033[32mAcertou\033[0m!')
        cont += 1
    else:
        sleep(0.5)
        print('\n\033[31mErrou\033[0m!')

sleep(0.5)
print(f'\nVocê acertou {cont} de {len(perguntas)} perguntas!!!')

