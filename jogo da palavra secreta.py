import random
import time

lista_palavra_secreta = ['abacate', 'manga', 'ovo', 'melancia', 'cuscuz']
palavra_secreta = random.choice(lista_palavra_secreta)

letras_descobertas = []
for letra in palavra_secreta:
    letras_descobertas.append('*')

tentativas = 0
letras_usadas = []
chutes = 0
while True:

    print("\nPalavra: ", end='')
    for letra in letras_descobertas:
        print(letra, end=' ')
    print()

    letra_inserida = input('Informe uma letra para tentar adivinhar a palavra secreta: ').lower().strip()
    tentativas += 1
    if len(letra_inserida) != 1 or not letra_inserida.isalpha():
        time.sleep(0.5)
        print('\nDigite apenas uma LETRA! Tente novamente...')
        continue
    
    if letra_inserida in letras_usadas:
        time.sleep(0.5)
        print('\nVocê ja usou esta letra! Tente novamente...')
        continue

    letras_usadas.append(letra_inserida)

    letra_certa = False
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra_inserida:
            letras_descobertas[i] = letra_inserida
            letra_certa = True

    if letra_certa:
        time.sleep(0.5)
        print('\n\033[32mLetra certa!\033[0m')
        
    else:
        chutes += 1
        time.sleep(0.5)
        print('\n\033[31mLetra errada!\033[0m')
        print(f'Você ainda tem {8 - chutes} tentativas, boa sorte!!')
        if chutes == 8:
            print(f'Você gastou todas sua chances... A palavra secreta era "{palavra_secreta}".')
            break
        
    
    palavra_pronta = True
    for letra in letras_descobertas:
        if letra == '*':
            palavra_pronta = False
            break
    if palavra_pronta:
        print(f'\nPrabénss! Você completou a palavra secreta: "{palavra_secreta}" com {tentativas} tentativas!')
        break
