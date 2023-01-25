# P06: Iteração
import pandas as pd

# Cria a Series "alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'})

# Itera sobre os dados ( nome dos alunos )
print('### Iterando sobre os dados ###')
for aluno in alunos: print(aluno)

print('--------------------------------------------')

# Itera sobre os índices ( matrículas )
print('### Iterando sobre os índices ###')
for indice in alunos.index: print(indice)