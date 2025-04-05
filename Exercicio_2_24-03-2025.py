class Animal:
	
	def __init__(self, especie, nome, cor, alimentacao, habitate, sexo, idade, tamanho, velocidade, possuiRabo):
		self.especie = especie
		self.nome = nome
		self.cor = cor
		self.alimentacao = alimentacao
		self.habitate = habitate
		self.sexo = sexo
		self.idade = idade
		self.tamanho = tamanho #em cm
		self.velocidade = velocidade
		self.possuiRabo = possuiRabo
	

	def __str__(self):
		return f"Especie: {self.especie}\nNome:{self.nome}\nCor:{self.cor}\nAlimentacao:{self.alimentacao}\nHabitate:{self.habitate}\nSexo:{self.sexo}\nIdade:{self.idade}\nTamanho:{self.tamanho}\nVelocidade:{self.velocidade}\nPossui rabo?{self.possuiRabo}\n"
	

cachorro = Animal("Cachorro","BOB","Azul","Carne","Rua","Macho",int(2),float(80.5),"Rapido",True)
gato = Animal("Gato","Tom","Preto","Peixe","Casa","Macho",int(5),float(60.5),"Rapido",True)
cavalo = Animal("Cavalo","Marcos","Marrom","Grama","Fazenda","Macho",int(1),float(240.0),"Rapido",True)
calopsita = Animal("Passaro","Maria","Branco","Alpiste","Arvore","Femea",int(2),float(10.5),"Rapido",False)
dinossauro = Animal("Reptil","Geovaldo","Verde","Folhas","Pangeia","Macho",int(90),float(10000),"Lento",True)
peixe = Animal("Peixe","Peixoto","Dourado","Algas","Mar","Macho",int(6),float(40.5),"Rapido",True)
boi = Animal("Boi","Roberto","Preto","Grama","Fazenda","Macho",int(10),float(195),"Lento",True)
macaco = Animal("Chimpanze","Twelves","Marrom","Banana","Floresta","Macho",int(6),float(100.5),"Rapido",True)

print(cachorro)
print(gato)
print(cavalo)
print(calopsita)
print(dinossauro)
print(peixe)
print(boi)
print(macaco)