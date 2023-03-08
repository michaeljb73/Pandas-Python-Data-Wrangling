#P11: Hello DataFrame!
import pandas as pd

# Cria o DataFrame
dados = {
    'nome':         ['Argentina','Brasil','Fransa','Itália','Reino Unido'],
    'continente':   ['Amériaca','América','Europa','Europa','Europa'],
    'extensao':     [2780,8511,644,301,244],
    'corVerde':     [0,1,0,1,0]
}

siglas = ['AR','BR','FR','IT','UK']

paises = pd.DataFrame(dados,index=siglas)

# Imprime o DataFrame
print(paises)