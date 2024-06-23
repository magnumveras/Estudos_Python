nome = 'Magno'
sobrenome = 'Veras'
idade = 36
ano_nascimento = 2024 - idade
maior_de_idade = idade >= 18
altura_metros = 1.84

#Verifica se é maior de idade ou não 
if maior_de_idade:
    maior_de_idade = 'Sim'
else:
    maior_de_idade = 'Não'

print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de Nascimento: ', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros: ', altura_metros)