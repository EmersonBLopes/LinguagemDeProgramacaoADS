import pandas as pd

registros = []

for i in range(10):
    print(f"\nInsira os dados do registro {i+1}")
    id = i
    titulo = input("Digite o nome do livro:")
    genero = input("Digite o genero do livro")
    autor = input("Digite o autor do livro:")
    ano = int(input("Digite o ano do livro"))
    
    registros.append({
        'ID': id,
        'titulo': titulo,
        'genero': genero,
        'autor': autor,
        'ano': ano
    })

tabela = pd.DataFrame(registros)

print(f"\nLista de livros disponíveis:\n{tabela}")
