import pandas as pd

tabela= pd.DataFrame({
    'id': pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    'nome': pd.Series(['hb20','astra','celta', 'corsa', 'civic', 'fusca', 'santana', 'pegeout', 'camaro', 'kombi']),
    'marca': pd.Series(['hyundai', 'chevrolet', 'chevrolet', 'hyundai', 'volkswagem', 'volkswagem', 'pegeout', 'volkswagem', 'volkswagem'])
})

print(tabela)