import math
import random 
import copy

class Genetico:
	def __init__(self,maxIteracoes,tamanhoPopulacao,tamGenoma,taxaReproducao,deslocamentoGene):
		self.populacao = []
		self.tamGenoma = tamGenoma
		self.taxaReproducao = taxaReproducao
		self.deslocamentoGene = deslocamentoGene
		self.maxIteracoes = maxIteracoes 
		self.deslocamentoGene = deslocamentoGene
		self.tamanhoPopulacao =tamanhoPopulacao
		self.popInicial(tamanhoPopulacao,tamGenoma)

	def posicionaQueens(self,tamanho):
		if tamanho < 2: return [-1]
		queensPosition = []
		
		for i in range(tamanho):
			j = random.randint(i,tamanho-1)
			queensPosition.append((i,j))
		return queensPosition		

	def popInicial(self,n, tam): 
		for i in range(n):
			self.populacao.append(self.posicionaQueens(tam))
	
	def diagonalCollision(self,queen1,queen2):
		if abs(queen1[0]-queen2[0]) == abs(queen1[1]-queen2[1]):
			return True
		else:
			return False

	def calAtaque(self,estado):
		linhas = dict()
		colunas = dict()
		total = 0
		counter = 1
		estado.sort()
		for queen1 in estado:
			
			if queen1[0] in linhas:
				linhas[queen1[0]] += 1
			else:
				linhas[queen1[0]] = 0
			
			if queen1[1] in colunas:
				colunas[queen1[1]] += 1
			else:
				colunas[queen1[1]] = 0
			


			for queen2 in estado[counter:]:
				if self.diagonalCollision(queen1,queen2):
					total += 1
			counter += 1
		
		for collumKey in colunas:
			total += colunas[collumKey]

		for lineKey in linhas:
			total += linhas[lineKey]
		return total

	def mutacao(self,estado,passo):
		tam = len(estado)
		while True:
		    i,j = random.choice(estado)
		    k = (j + passo)%tam

		    if (i,k) not in estado:
		        estado.remove((i,j))
		        estado.append((i,k))
		        break

	       


if __name__ == "__main__":
	maxIteracoes = 10000
	tamanhoPopulacao = 10 
	tamGenoma = 5
	taxaReproducao = 3
	deslocamentoGene = 10

	a = Genetico(maxIteracoes,tamanhoPopulacao,tamGenoma,taxaReproducao,deslocamentoGene)
	l =[[1,0,0,0,0],
		[0,0,1,0,0],
		[0,0,0,1,0],
		[0,0,0,0,1],
		[0,0,0,0,1]]
	p = [(0, 0), (1, 2), (2, 3), (3, 4), (4, 4)]
	
	print("Original: ",p)
	a.mutacao(p,1)
	print("Mutacao: ",p)