salario = float(input("digite seu salario:"))
salario_minimo = 1509

if salario < salario_minimo:
    print("seu salario eh menor que o salario minimo")
elif salario == salario_minimo:
    print("seu salario eh igual o salario minimo")
else:
    print("seu salario eh maior que o salario minimo")
