#P02: Propriedades básicas das séries
import pandas as pd

#cria a Series alunos
alunos = pd.Series({'M02': 'Bob', 'M05': 'Dayse', 'M13': 'Bill', 'M17': 'Cris', 'M19': 'Jimi'})

#atribui nomes para os vetores de dados e rótulos
alunos.name = "alunos"
alunos.index.name = "matrículas"

#recupera e imprime as propriedades
print(alunos)
print("------------------")
tamanho = alunos.size
dados = alunos.values
rotulos = alunos.index
alunos_tipo = type(alunos)
alunos_dtype = alunos.dtype
alunos_idx_dtype = alunos.index.dtype

print('Número de elementos: ', tamanho)
print('Vetor de dados: ', dados)
print('Vetor de rótulos: ', rotulos)
print('tipo (type): ', alunos_tipo)
print('dtype da Series: ', alunos_dtype)
print('dtype do vetor rótulos: ', alunos_idx_dtype)

# Consultando através de indices
# Consultando o aluno Bob
print('Concultando matrícula M02: ', alunos['M02'])

# Consulta por fatiamento slicing
print('Consulta por fatiamento slicing #######################')

print('### Do primeiro ao quarto elemento ###')
print(alunos[0:4]) # do primeiro ao quarto elemento

print('### Do segundo ao último ###')
print(alunos[1:]) #do segundo ao último

print('### Do quarto ao primeiro ###')
print(alunos[:3]) # do quarto ao primeiro

print('### Três últimos elementos ###')
print(alunos[-3:]) # três últimos elementos

print('### Do primeiro ao 5 de dois em dois ###')
print(alunos[0:5:2]) # do primeiro ao 5 de dois em dois

print('### Elementos 0, 5 e 2 ###')
print(alunos[[0,4,2]]) # elementos 0, 5 e 2

# Continuar na página 29
