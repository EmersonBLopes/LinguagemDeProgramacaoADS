#Exercicio 1 - Ler uma idade e dizer se o usuário é maior de idade ou menor de idade

idade = int(input("digite sua idade:"))

if idade >= 18:
    print(f"Sua idade eh: {idade}\nvoce eh maior de idade")
else:
    print(f"Sua idade eh: {idade}\nvoce eh menor de idade ")