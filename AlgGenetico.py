#!/usr/bin/env python
# coding: utf-8

# In[197]:



import math
import random 
import copy
import itertools as it 
TAMANHOTABULEIRODEFAULT = 4


# In[268]:


def geratab(tamanho):
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


# In[269]:


geratab(4)


# In[270]:


def acharrainha(estado):
    q=[]
    for i in range(len(estado)):
        for j in range(len(estado)):
                if estado[i][j]==1:q.append((i,j))
    return q


# In[271]:


def calAtaque(estado):
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
    pr = acharrainha(estado)
    d = 0
    for p,coords in enumerate(pr):
        i,j = coords
        #diagonal esquerda
        k,w = i+1,j-1
        while(w>=0 and k<len(estado)):
            if estado[k][w]==1:
                d+=1
                break
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


# In[272]:


def mutacao(estado,passo):
    tam = len(estado)
    while True:
        i,j = random.choice(acharrainha(estado))
        k = (j + passo)%tam
        if estado[i][k] == 0:
            estado[i][k],estado[i][j] = estado[i][j], estado[i][k]
            break
    return estado


# In[273]:


def popInicial(n, tam): 
#quantidade de tabuleiros de tamanho n
    populacao = []
    for i in range(n):
        populacao.append(geratab(tam))
    return populacao


# In[274]:


popInicial(1,4)


# In[275]:


def cruzar(genoma1,genoma2):
    g1 = copy.deepcopy(genoma1)
    g2 = copy.deepcopy(genoma2)
    corte = random.randint(0,len(g1)-1)
    return g1[:corte]+g2[corte:],g2[:corte]+g1[corte:] #gera 2 filhos


# In[276]:


cruzar([[1, 0, 0, 0], [0, 1, 0, 0]], [[0, 1, 0, 0], [0, 1, 0, 0]])


# In[277]:


def fitness(populacao):
    fits = []
    tam = len(populacao[0])
    maxAtaques = math.factorial(tam)/((math.factorial(tam-2)*2))
    for i in populacao:
        fits.append(1 - calAtaque(i)/maxAtaques)
    return fits


# In[278]:


def roletaViciada(populacao,fitness):
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


# In[279]:


def selecaoNatural(populacao,numCasais):
    selecao = []
    fts = fitness(populacao)
    for i in range(2*numCasais):
        selecao.append(roletaViciada(populacao,fts))
    return selecao


# In[280]:



def testeMeta(pops):
    fts = fitness(pops)
    try:
        posMeta = fts.index(1)
        return "solucao",pops[posMeta]
    except(ValueError):
        return -1


# In[324]:


def genetico(maxIteracoes,tamanhoPopulacao,tamGenoma,taxaReproducao,deslocamentoGene):
    #gera populacao inicial
    populacao = popInicial(tamanhoPopulacao,tamGenoma)
    #iterações
    print("população ",populacao)
    print("------------------------------------------------------------")
    #print("população inicial",popInicial)
    
    for i in range(maxIteracoes):
        #primeiro teste de meta
        #print("a",)
        res = testeMeta(populacao)
        if res != -1: return res,i
        #etapa de evolucao por reproducao
        novaPopulacao = []
        reprodutores = selecaoNatural(populacao,taxaReproducao)
        machos = reprodutores[:taxaReproducao]
        femeas = reprodutores[taxaReproducao:]
        for k,w in zip(machos,femeas):
            f1,f2 = cruzar(k,w)
            novaPopulacao.append(f1)
            novaPopulacao.append(f2)
        #teste de meta na nova populacao
        res = testeMeta(novaPopulacao)
        #print("-------------------------")
        if res != -1:return res,i
        #aceita algumas mutacoes na nova populacao
        for z in novaPopulacao:
            if random.randint(0,5)<10:
                z = mutacao(z,deslocamentoGene)
        populacao = novaPopulacao
        #print("aquiiiiii" ,novaPopulacao)
    return "falha",z


# In[328]:


maxIteracoes = 1000
tamanhoPopulacao = 1 
tamGenoma = 4
taxaReproducao = 1
deslocamentoGene = 10

genetico(maxIteracoes,tamanhoPopulacao,tamGenoma,taxaReproducao,deslocamentoGene)


# In[ ]:





# In[ ]:




