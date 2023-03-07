while True:
    cpf_digitado = input('Digite o seu CPF sem caracteres especiais:')
    cpf_lista = []
    i = 10
    for numero_multi in cpf_digitado:

        if numero_multi.isdigit():
            numero_int = int(numero_multi)
            cpf_lista.append(numero_int * i)
            i -= 1

        if i == 1:
            cpf_soma = (cpf_lista[0] + cpf_lista[1] + cpf_lista[2] + cpf_lista[3] +
                        cpf_lista[4] + cpf_lista[5] + cpf_lista[6] +
                        cpf_lista[7] + cpf_lista[8]) * 10 % 11

    try:
        if cpf_soma == cpf_lista[9]:
            print('Cpf válido')
            break

    except:
        print('Cpf invalido, tente novamente')
