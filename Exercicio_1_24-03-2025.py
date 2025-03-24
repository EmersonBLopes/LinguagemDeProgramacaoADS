class Carro:

  def __init__(self,fabricante,modelo,ano,cor,placa):
    self.fabricante = fabricante
    self.modelo = modelo
    self.ano = ano
    self.cor = cor
    self.placa = placa
  
  def __str__(self):
    return f"Fabricante:{self.fabricante}\nModelo:{self.modelo}\nAno:{self.ano}\nCor:{self.cor}\nPlaca:{self.placa}\n"

fabricante = input("Digite o nome da fabricante do carro:")
modelo = input("Digite o modelo do carro:")
ano = input("Digite o ano do carro:")
cor = input("Digite a cor do carro:")
placa = input("Digite placa do carro:")

carro = Carro(fabricante, modelo, ano, cor, placa)

print(f"\n{carro}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             