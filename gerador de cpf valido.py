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

for __ in range(5):
    cpf_valido = gerador_cpf_valido()

    print(cpf_valido)    
