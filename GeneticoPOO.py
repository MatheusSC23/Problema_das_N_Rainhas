
import math
import random 
import copy
import itertools as it 
TAMANHOTABULEIRODEFAULT = 4

class Genetico:
	def __init__(self,tamanhoTabuleiro):

		self.tab,self.queensPosition = self.geratab(tamanhoTabuleiro)

	def geratab(self,tamanho):
		queensPosition = []
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
		            queensPosition.append((i,j))
		            break
		return tab,queensPosition

	def calAtaque(self):
	    at=0
	    atlinhas = 0
	    estado = copy.deepcopy(self.tab)
	    for i in estado: 
	        #ataque em linhas
	        if sum(i)>1:
	            atlinhas+=math.ceil(sum(i)/2)
	    at+=atlinhas
	    atcolunas = 0
	    for c in range(len(estado)):
	        n1 = 0
	        
	        for l in range(len(estado)): n1+= estado[l][c]
	        if n1>1:
	            atcolunas += math.ceil(n1/2)
	    at+=atcolunas
	    pr = self.queensPosition
	    d = 0
	    print(pr)
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

	        #diagonal superior esquerda
	        k,w = i-1,j+1
	        conflict = False
	        while(k>=0 and w<len(estado) and not conflict):
	            if estado[k][w]==1:
	                d+=1
	                conflict = True
	            w+=1
	            k-=1
	        #diagonal inferior direita
	        l,c = i+1,j+1
	        conflict = False
	        while(l <len(estado) and c<len(estado) and not conflict):
	            if estado[l][c]==1:
	                d+=1
	                conflict = True
	            l+=1
	            c+=1
	        #diagonal inferior direita
	        l,c = i-1,j-1
	        conflict = False
	        while(l >= 0 and c >= 0 and not conflict):
	            if estado[l][c]==1:
	                d+=1
	                conflict = True
	            l-=1
	            c-=1
	    at+=d/2
	    return at

if __name__ =="__main__":
	a = Genetico(4)
	for i in a.tab:
	    print(i)
	print(a.calAtaque())