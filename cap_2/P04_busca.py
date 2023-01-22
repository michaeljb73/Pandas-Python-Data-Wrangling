#P04: Busca em Series
import pandas as pd

# Cria a Series "alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'})

# Testa se rótulos fazem parte de uma Series
tem_M13 = 'M13' in alunos
tem_M99 = 'M99' in alunos
print("Existe o rótulo 13 em alunos ? -> ", tem_M13)
print("Existe o rótulo 99 em alunos ? -> ", tem_M99)

print("----------------------------------")

# Testar se valor faz parte de uma Series
tem_Bob = alunos.isin(['Bob'])
print("Existe o valor 'Bob' ? ")
print(tem_Bob)

print("----------------------------------")

# Combinando indexação boolean e teste de um valor em uma Series
tem_Cris = alunos[alunos.isin(['Cris'])]
print("Tem Cris ? -> ")
print(tem_Cris)

# Continuar na  página 35 'Modificação'
