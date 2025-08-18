def validar_primeiro_digito_cpf(cpf): 
    soma = 0
    peso = 10
    for i in range(9):
        mult = int(cpf[i]) * peso 
        soma += mult
        peso -= 1

    resto = (soma * 10) % 11
    if resto > 9:
        resto = 0    

    return resto

def validar_segundo_digito_cpf(cpf):
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = (soma * 10) % 11
    if resto > 9:
        resto = 0
    
    return resto

def gerador_cpf_valido():
    from random import randint
    cpf = ''
    for i in range(9):
        cpf += str(randint(0, 9))

    resultado_1_digito = validar_primeiro_digito_cpf(cpf)
    resultado_2_digito = validar_segundo_digito_cpf(cpf + str(resultado_1_digito))

    #CPF completo
    return cpf + str(resultado_1_digito) + str(resultado_2_digito)

def valida_cpf_usuario():
    while True:    
        cpf = input('Digite o cpf (xxx.xxx.xxx-xx): ')
        cpf_novo = cpf.replace('.', '').replace('-', '')
        try:
            int(cpf_novo)
            if len(cpf_novo) != 11:
                raise ValueError

            if cpf_novo == cpf_novo[0] * len(cpf_novo):
                print('CPF sequencial! Tente novamente...\n')
                continue

            break
        except ValueError:
            print('CPF inválido, digite novamente...\n')

    resultado_1_digito = validar_primeiro_digito_cpf(cpf_novo)
    resultado_2_digito = validar_segundo_digito_cpf(cpf_novo)

    if resultado_1_digito == int(cpf_novo[9]) and resultado_2_digito == int(cpf_novo[10]):
        print(f'{cpf} é válido')

    else: 
        print('CPF inválido')    


for __ in range(2):
    cpf_valido = gerador_cpf_valido()

    print(cpf_valido)

cpf_usuario = valida_cpf_usuario()
