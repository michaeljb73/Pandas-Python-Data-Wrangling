# P12 : Propriedades básicas dos DataFrames
import pandas as pd

dados = {
    'nome':         ['Argentina','Brasil','Fransa','Itália','Reino Unido'],
    'continente':   ['Amériaca','América','Europa','Europa','Europa'],
    'extensao':     [2780,8511,644,301,244],
    'corVerde':     [0,1,0,1,0]
}

siglas = ['AR','BR','FR','IT','UK']

paises = pd.DataFrame(dados,index=siglas)

# Recupera e imprime as propriedades
print("--------------")
num_linhas = paises.shape[0]
num_colunas = paises.shape[1]
indices = paises.index
colunas = paises.columns
paises_tipo = type(paises)
paises_dtypes = paises.dtypes
paises_idx_dtype = paises.index.dtype

print(f"Numero de linhas:.............{num_linhas}")
print(f"Numero de colunas:............{num_colunas}")
print(f"Rótulos das linhas:...........{indices}")
print(f"Rótulo das colunas:...........{colunas}")
print(f"Tipo (type):..................{paises_tipo}")
print(f"dtypes das colunas:           \n{paises_dtypes}")
print(f"dtype dos rótulos das linhas:.{paises_idx_dtype}")

# Cotinuar na pág. 52
# 3.2 Técnicas para consulta e modificação de dados