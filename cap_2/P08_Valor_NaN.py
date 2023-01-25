# P08: Valor NaN
import pandas as pd

verde = pd.Series({'BR': 1,'FR': 0,'IT': 1,'UK': 0})
azul = pd.Series({'AR': 1,'BR': 1,'FR': 1,'IT': 0,'UK': 1})

print('# Soma verde e azul ---------------------')
soma = verde + azul
print('soma:')
print(soma)

print('-----------------------------------------')
print('isnull(soma): ')
print(pd.isnull(soma))