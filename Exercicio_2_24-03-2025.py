class Animal:
	
	__init__(self, especie, nome, cor, alimentacao, habitate, sexo, idade, tamanho, velocidade, possuiRabo,):
		self.especie = especie
		self.nome = nome
		self.cor = cor
		self.alimentacao = alimentacao
		self.habitate = habitate
		self.sexo = sexo
		self.idade = idade
		self.tamanho = tamanho
		self.velocidade = velocidade
		self.possuiRabo = possuiRabo
	

	__str__(self):
		return f"Especie: {self.especie}\nNome:{self.nome}\nCor:{self.cor}\nAlimentacao:{self.alimentacao}\nHabitate:{self.habitate}\nSexo:{self.sexo}\nIdade:{self.idade}\nTamanho:{self.tamanho}\nVelocidade:{self.velocidade}\nPossui rabo?{self.possuiRabo}"
	

cachorro = animal("Cachorro","BOB","Azul","Carne","Rua","Macho",int(2),float(80.5),"Rapido",True)
gato = animal("Gato","BOB Marley","Preto","Carne","Rua","Macho",int(2),float(80.5),"Rapido",True)
cavalo = animal("Cavalo","Marcos","Marrom","Grama","Fazenda","Macho",int(2),float(80.5),"Rapido",True)
calopsita = animal("Passaro","Maria","Branco","Alpiste","Arvore","Femea",int(2),float(80.5),"Rapido",False)
dinossauro = animal("Reptil","BOB","Verde","Carne","Floresta","Macho",int(90),float(80.5),"Lento",True)
peixe = animal("Peixe","Peixoto","Azul","Carne","Esgoto","Macho",int(24),float(80.5),"Rapido",True)
cachorro = animal("Cachorro","BOB","Azul","Carne","Rua","Macho",int(1),float(80.5),"Rapido",True)
macaco = animal("Ximpanze","Twelves","Marrom","Banana","Floresta","Macho",int(6),float(80.5),"Rapido",True)