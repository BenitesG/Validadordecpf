import os

while True:
    cpf_digitado = input('Digite o seu CPF sem caracteres especiais:')
    cpf_lista = []
    cpf_lista2 = []
    contador_regressivo1 = 10
    contador_regressivo2 = 11
    for digito1_multi in cpf_digitado:

        if digito1_multi.isdigit():
            digito1_int = int(digito1_multi)
            cpf_lista.append(digito1_int * contador_regressivo1)
            contador_regressivo1 -= 1

        if contador_regressivo1 == 1:
            soma_digito1 = (cpf_lista[0] + cpf_lista[1] + cpf_lista[2] + cpf_lista[3] +
                            cpf_lista[4] + cpf_lista[5] + cpf_lista[6] +
                            cpf_lista[7] + cpf_lista[8]) * 10 % 11

    for digito2_multi in cpf_digitado:

        if digito2_multi.isdigit():
            digito2_int = int(digito2_multi)
            cpf_lista2.append(digito2_int * contador_regressivo2)
            contador_regressivo2 -= 1

        if contador_regressivo2 == 0:
            soma_digito2 = (cpf_lista2[0] + cpf_lista2[1] + cpf_lista2[2] + cpf_lista2[3] +
                            cpf_lista2[4] + cpf_lista2[5] + cpf_lista2[6] +
                            cpf_lista2[7] + cpf_lista2[8] + cpf_lista2[9]) * 10 % 11

    try:
        if soma_digito1 <= 9 and soma_digito2 <= 9:
            if soma_digito1 == cpf_lista[9] and soma_digito2 == cpf_lista2[10]:
                print('Cpf válido')
                break
            else:
                os.system('cls')
                print('Cpf inválido ou inexistente')
        else:
            soma_digito1 == 0 and soma_digito2 == 0
            print('Cpf válido')
            break
    except:
        os.system('cls')
        print('Cpf inválido ou inexistente')
