
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

	def calAtaque(estado):
	    at=0
	    atlinhas = 0
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
	    for p,coords in enumerate(pr):
	        i,j = coords
	        #diagonal inferior esquerda
	        k,w = i+1,j-1
	        while(w>=0 and k<len(estado)):
	            if estado[k][w]==1:
	                d+=1
	            w-=1
	            k+=1

	        #diagonal superior esquerda
	        k,w = i-1,j+1
	        while(k>=0 and w<len(estado)):
	            if estado[k][w]==1:
	                d+=1
	            w-=1
	            k+=1
	        #diagonal direita
	        l,c = i+1,j+1
	        while(1 <len(estado) and c<len(estado)):
	            if estado[1][c]==1:
	                d+=1
	                break
	            l+=1
	            c+=1
	    at+=d
	    return at

if __name__ =="__main__":
	a = Genetico(4)
	print(a.tab)