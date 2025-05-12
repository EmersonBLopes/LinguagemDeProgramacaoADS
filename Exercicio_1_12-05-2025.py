import pandas as pd

pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
pd.Series(data=6)
nomes = 'Alek Everson Caique Fabiano Alessio Eduardo'.split()
cpf = '1111-1111-11111 2222-2222-2222 333-333-333 444-444-444 555-555-555 666-666-666'.split()
idade = '2 25 16 40 54 55'.split()
estado = 'BH MG MG SP RJ AC'.split()

dados = list(zip(nomes,cpf,idade,estado))

tabela = pd.DataFrame(dados,columns=['nomes','cpf','idade','estado'])

print(tabela)



