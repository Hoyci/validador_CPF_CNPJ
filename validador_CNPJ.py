def calcular_primeiro(cnpj):
    it = 5
    soma = 0
    for i in cnpj:
        mult = int(i) * it
        if it == 2:
            it = 10
        it -= 1
        soma += mult
    resultado = 11 - (soma % 11)
    if resultado > 9:
        resultado = 0
    print(resultado)
    return cnpj + str(resultado)


def calcular_segundo():
    cnpj = input('Insira o CNPJ: ')
    variavel = calcular_primeiro(cnpj)
    it = 6
    soma = 0
    for i in variavel:
        mult = int(i) * it
        if it == 2:
            it = 10
        it -= 1
        soma += mult
    resultado = 11 - (soma % 11)
    if resultado > 9:
        resultado = 0
    print(resultado)
    final = variavel + str(resultado)
    return final


def formatar():
    valor = calcular_segundo()
    valor = valor[0:2] + '.' + valor[2:5] + '.' + valor[5:8] + '/' + valor[8:12] + '-' + valor[12:14]
    print(f'O número validado é {valor}')

formatar()