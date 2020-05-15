#!/usr/bin/python3

# Implementation of Stewart's optimal algorithm for multi-peg Tower of Hanoi

from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import colorsys
import os


DEBUG=False

S_mem = dict() # hash memory of the values

# score optimal et coupe optimale 

def argmin_set(l): # tous les minima
    m=min(l)
    mins=[]
    for i in range(len(l)):
        if l[i]==m:
            mins.append(i)
    return(mins)

def S_optcut(n,p):
    if n<p:
        S_mem[(n,p)] = 2*n-1, None
        return S_mem[(n,p)]
    if p==3:
        S_mem[(n,p)] = 2*S_optcut(n-1,p)[0]+1, n-1
        return S_mem[(n,p)]
    if (n,p) in S_mem:
        return S_mem[(n,p)]
    S = ([ 2*S_optcut(m,p)[0] + S_optcut(n-m,p-1)[0] for m in range(1,n) ])
    if DEBUG: print(S, list(range(1,n)))
    m = argmin_set(S)
    S_mem[(n,p)] = S[m[-1]], [i+1 for i in m]
    return S_mem[(n,p)]

def move( etat, src, dest ):
    etat[dest].append( etat[src].pop() ) # on enlève le disque de src et on le met sur dest
    deplacements.append( deepcopy(etat) )

def hanoi( etat, n, src, dest, libres, strategie, niv=0 ):

    # etat du jeu, nombre de disques à déplacer, source, destination, liste des pics libres pour bosser
    # seule la variable etat est changée par cette fonction
    
    p = len(libres)+2

    if DEBUG: print(" |"*niv,"HANOI()", n, " de ",src, "à", dest, "/", libres, '/ n:',n,'p:',p)
    
    if n<p:
        for i in range(n-1):
            move(etat, src, libres[i])
        move(etat, src, dest)
        for i in range(n-2,-1,-1):
            move(etat, libres[i], dest)
    else:
        m = strategie(n,p)
        hanoi( etat, m, src, libres[0], [dest] + libres[1:], strategie, niv+1 )
        hanoi( etat, n-m,  src, dest,  libres[1:], strategie, niv+1 )
        hanoi( etat, m, libres[0], dest, [src] + libres[1:], strategie, niv+1 )
    
    if DEBUG: print(" |"*niv,etat)
                
def go(n=3,p=3, strat=None):

    global deplacements
    
    etat = [ list(range(n,0,-1)) ] + [ [] for i in range(p-1) ]
    deplacements = [ deepcopy(etat) ]
    
    if strat==None: # optimal
        S,_ = S_optcut(n,p)
        #print("Nb de coups:",S)
        #print("Stratégie:",S_mem)
        strat = lambda a,b: S_mem[(a,b)][1]
    
    hanoi( etat, n,   0,  p-1,   list(range(1,p-1) ), strat )


##############################
# représentation graphique

def plot_etat(fig, n, p, etat):

    plt.clf()

    colors = [ colorsys.hsv_to_rgb( x, 1.0, 0.8 ) for x in np.arange(0.0,1.0, 1.0/n ) ]

    cc = 2
    coef = 0.49*n/(n+cc)
    
    ax = fig.add_subplot(211)
    plt.xlim(0, p*n )
    plt.ylim(-1, n+2 )
    ax.axis('off')
    i=.5
    ax.add_patch(Rectangle( (0,-1),p*n,1,color='brown',alpha=1))
    for x in etat:
        ax.add_patch(Rectangle( (n*i-coef*cc/2,0), coef*cc, n+2, color='brown', alpha=1))
        j=0
        for d in x:
            r = coef*(d+2)
            ax.add_patch(Rectangle( (n*i-r,j), 2*r,1, alpha=1, facecolor=colors[d-1], edgecolor='black' ) )
            j+=1
        i+=1
    plt.tight_layout()
    
    ax = fig.add_subplot(212)
    plt.xlim(0, n*p )
    plt.ylim(0, n )
    ax.axis('off')
    ax = plt.gca()
    ax.add_patch(Rectangle( (0,0),p*n, n, color='brown',alpha=1))
    i=.5
    for x in etat:
        ax.add_patch(Circle( ( n*i, n/2), coef*(n+cc), alpha=1, facecolor='grey', edgecolor='white' ))
        for d in x:
            r = coef*(d+cc)
            ax.add_patch(Circle( ( n*i, n/2), r, alpha=1, facecolor=colors[d-1], edgecolor='black' ))
        ax.add_patch(Circle( ( n*i, n/2), coef*cc, alpha=1, facecolor='brown', edgecolor='white' ))
        i+=1
    plt.tight_layout()


####################################################
### Main


# Génération des courbes

nrange = range(3,30)
rln = range(len(nrange))
for p in range(3,7):
    S = [ S_optcut(n,p) for n in nrange ]
    print(len(S),len(nrange))
    y = [ S[i][0] for i in rln ]
    print(y)
    m = [ S[i][1] for i in rln ]
    plt.figure(figsize=(12,8))
    plt.title("$S(n,%d)$ and $h(n,%d)$ as a function of $n$"%(p,p))
    plt.xlabel("$S(n,%d)$"%p)
    plt.ylabel("$n$")
    plt.plot( nrange, y,'o' )
    plt.yscale('log')
    i=0
    for n in nrange:
        if S[i][1]!=None:
            plt.text(n, S[i][0], S[i][1],ha='right' )
        i+=1
    plt.savefig("S_h_%d.png"%p)
    plt.close()


def genere_anim(n,p):

    go(n,p)
    print(len(deplacements)-1)
    #go(n,p, strat = lambda a,b: (a-1 if b==3 else max(1,int(a-pow(a,(b-3)/(b-2))))) ) # approximation raisonnable de la coupe optimale
    #print(len(deplacements)-1)

    haut = 3
    fig = plt.figure(figsize = (p*haut/2.4, haut))
    os.system("rm tmp/*")
    t=0
    for x in deplacements:
        print(t, x)
        plot_etat(fig, n,p, x)
        plt.savefig('tmp/%04d.png'%t)
        t+=1
    plt.close('all')
    os.system("convert -verbose -loop 0 -delay 100 tmp/0000.png -delay 20 tmp/*.png -delay 300 tmp/%04d.png %d_%d.gif"%(t-1,n,p))
    os.system("rm tmp/*")

for p in range(3,7):
    genere_anim(10,p)



