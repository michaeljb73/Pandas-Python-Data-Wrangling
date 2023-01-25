# P07: Oerações Aritméticas com computação vetorizada.
import pandas as pd
import numpy as np

# Criar Series s1 e s2
s1 = pd.Series([2,4,6])
s2 = pd.Series([1,3,5])
print("### Serie s1 ###"); print(s1)
print("### Serie s2 ###"); print(s2)

print('--------------------------------------------')
# Efetua operações aritméticas
print('### Multiplicando elementos de s1 por 2 ###')
print('s1 * 2')
print( s1 * 2 )

print('--------------------------------------------')
print('### Soma s1 a s2 ###')
print('s1 + 2')
print( s1 + s2 )

print('--------------------------------------------')
print('### Raiz quadrada dos elementos de s1 ###')
print( np.sqrt(s1) )
