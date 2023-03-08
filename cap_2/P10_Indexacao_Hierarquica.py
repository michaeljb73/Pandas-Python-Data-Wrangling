# P10: Indexação hierarquica.
import pandas as pd

moedas = ['Peso','Real','Euro','Euro','Libra']
paises = [['América','América','Europa','Europa','Europa'],['AR','BR','FR','IT','UK']]
paises = pd.Series(moedas, index=paises)

print(paises)                 # Imprime toda a Series
print('---------------------------------')
print(paises['América'])      # { AR: Peso, BR: Real }
print('---------------------------------')
# . Obs.: Não se pode fazer referência direta ao índice mais interno,
#         no caso uma referência direta a IT( paises[IT] ). A forma
#         correta é descrita abaixo.
print(paises[:,'IT'])         # { Europa: Euro }
print('---------------------------------')
print(paises['Europa','IT'])  # Euro

# Continuar na pág. 48 - Cap. 3 : A Estrutura de Dados DataFrame