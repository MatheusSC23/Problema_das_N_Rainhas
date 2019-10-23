
import math
import random 
import copy
import itertools as it 
TAMANHOTABULEIRODEFAULT = 4

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

	def geratab(self,tamanho):
		if tamanho < 2: return [-1]
		tab = []
		for i in range(tamanho):
		    l=[]
		    for j in range(tamanho):
		        l.append(0)
		    tab.append(l)
		for i in range(tamanho):
		    while True:
		        j = random.randint(0,tamanho-1)
		        if tab[i][j] == 0:
		            tab[i][j] = 1
		            break
		return tab


	def acharrainha(self,estado):
		q=[]
		for i in range(len(estado)):
		    for j in range(len(estado)):
		            if estado[i][j]==1:q.append((i,j))
		return q

	def calAtaque(self,estado):
	    at=0
	    atlinhas = 0
	    for i in estado: 
	        #ataque em linhas
	        if sum(i)>1:
	            atlinhas+=sum(i)-1
	    at+=atlinhas
	    atcolunas = 0
	    for c in range(len(estado)):
	        n1 = 0
	        
	        for l in range(len(estado)): n1+= estado[l][c]
	        if n1>1:
	            atcolunas += n1 - 1
	    at+=atcolunas
	    pr = self.acharrainha(estado)
	    d = 0
	    for coords in pr:
	        i,j = coords
	        #diagonal inferior esquerda
	        k,w = i+1,j-1
	        conflict = False
	        while(w>=0 and k<len(estado) and not conflict):
	            if estado[k][w]==1:
	                d+=1
	                conflict = True
	            w-=1
	            k+=1

	        #diagonal inferior direita
	        l,c = i+1,j+1
	        conflict = False
	        while(l < len(estado) and c < len(estado) and not conflict):
	            if estado[l][c]==1:
	                d+=1
	                conflict = True
	            l+=1
	            c+=1
	        
	    at+=d
	    return at

	def mutacao(self,estado,passo):
		tam = len(estado)
		while True:
		    i,j = random.choice(self.acharrainha(estado))
		    k = (j + passo)%tam
		    if estado[i][k] == 0:
		        estado[i][k],estado[i][j] = estado[i][j], estado[i][k]
		        break

	def popInicial(self,n, tam): 
	    for i in range(n):
	        self.populacao.append(self.geratab(tam))

	def cruzar(self,genoma1,genoma2):
		g1 = copy.deepcopy(genoma1)
		g2 = copy.deepcopy(genoma2)
		corte = random.randint(0,len(g1)-1)
		return g1[:corte]+g2[corte:]

	def fitness(self,populacao):
		fits = []
		for i in populacao:
		    fits.append(self.calAtaque(i))
		return fits
	    		    
	def roletaViciada(self,populacao,fitness):
	    #levantamento de qualidade dos individuos
	    totalFitness = sum(fitness)
	    #calcular fações de cada individuo
	    fracoes = [f/totalFitness for f in fitness]
	    #cira intervalos
	    intervalos = []
	    acum = 0
	    for i in fracoes:
	        acum+=i
	        intervalos.append(round(acum,2))
	    #gira roleta
	    resultadoRoleta = random.randint(0,len(populacao))/len(populacao)
	    #selecionar individuo
	    ind = 0
	    while resultadoRoleta > intervalos[ind]: ind+=1
	    #retorna individuo selecionado
	    return populacao[ind]

	def selecaoNatural(self,populacao,numCasais):
		selecao = []
		fts = self.fitness(populacao)
		for i in range(numCasais):
			selecao.append(self.roletaViciada(populacao,fts))
		return selecao

	def testeMeta(self,populacao):
	    fts = self.fitness(populacao)
	    try:
	        posMeta = fts.index(0)
	        return populacao[posMeta]
	    except(ValueError):
	        return -1

	def genetico(self):
		populacao = self.populacao
		#print("população inicial",popInicial)
		print("População inicial:")
		for estado in populacao:
			for linha in estado:
				print(linha)
			print("\n\n")

		for i in range(self.maxIteracoes):
			print(i)

		    #primeiro teste de meta
		    #print("a",)
		    res = self.testeMeta(populacao)
		    if res != -1: return res
		    #etapa de evolucao por reproducao
		    novaPopulacao = []
		    reprodutores = self.selecaoNatural(populacao,self.tamanhoPopulacao)

		    machos = copy.deepcopy(reprodutores)
		    reprodutores.reverse()
		    femeas = copy.deepcopy(reprodutores)
		    
		    for k,w in zip(machos,femeas):
		        f1 = self.cruzar(k,w)
		        novaPopulacao.append(f1)
	
		    #teste de meta na nova populacao
		    res = self.testeMeta(novaPopulacao)
		    #print("-------------------------")
		    if res != -1:return res
		    #aceita algumas mutacoes na nova populacao
		    for z in novaPopulacao:
		        if random.randint(5,11)<10:
		            z = self.mutacao(z,self.deslocamentoGene)
		    populacao = novaPopulacao
		    #print("aquiiiiii" ,novaPopulacao)
		return "Falha, tabuleiro não encontrado"

if __name__ =="__main__":
	maxIteracoes = 10000
	tamanhoPopulacao = 10 
	tamGenoma = 5
	taxaReproducao = 3
	deslocamentoGene = 10

	a = Genetico(maxIteracoes,tamanhoPopulacao,tamGenoma,taxaReproducao,deslocamentoGene)
	res = a.genetico()
	print("Tabuleiro resultante:")
	
	for i in res:
		print(i)
	#print(a.selecaoNatural(a.populacao,tamanhoPopulacao))

	
		