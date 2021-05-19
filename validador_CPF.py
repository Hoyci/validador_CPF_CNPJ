cpf_original = input('Insira o CPF: ')
cpf = cpf_original[:9]
soma1 = 0
it1 = 10

for i in cpf:
    mult1 = int(i) * it1
    print(f'{i} * {it1} = {mult1}')
    soma1 += mult1
    it1 -= 1
print(soma1)

digito1 = 11 - (soma1 % 11)
if digito1 > 9:
    novo_cpf = cpf + '0'
    print(novo_cpf)
else:
    novo_cpf = cpf + str(digito1)


soma2 = 0
it2 = 11
for i in novo_cpf:
    mult2 = int(i) * it2
    print(f'{i} * {it2} = {mult2}')
    soma2 += mult2
    it2 -= 1
print(soma2)

digito2 = 11 - (soma2 % 11)
print(digito2)
if digito2 > 9:
    novo_cpf += '0'
else:
    novo_cpf += str(digito2)
print(novo_cpf)
