#P05: Inserindo, alterando e removendo elementos de Series
import pandas as pd

# Cria a Series "alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'})

print('Series original:')
print(alunos)

# Inserir o aluno de matrícula M55, Rakesh
alunos['m55'] = 'Rakesh'

# Altera os nomes de Bill, Cris e Jimi
alunos['M13'] = 'Billy'
alunos[['M14','M19']] = ['Cristy','Jimmy']

# Remove o aluno de matrícula M02 Bob
alunos = alunos.drop('M02')

print('------------------------------------')
print('Series após as alterações: ')
print(alunos)

print('------------------------------------')
print('Alterando o índice da Series: ')
alunos.index = ['M91','M92','M93','M94','M95',]
print(alunos)

# Continuar página 36 - Computação Vetorizada