
f = open('p022_names.txt', 'r')


##Probleme 16

def solve(n):
    S=0
    Chiffres=str(2**n)
    for k in range(0,len(Chiffres)):
        S=S+int(Chiffres[k])  
    return S

assert solve(1000)

##Problem 22
def liste():
    T=[]
    for ligne in f:
        I=ligne.split(',')
        T=T+I
    return T

def liste_sans_guillemets():
    L=liste()
    for k in range(0,len(L)):
        n=len(L[k])
        I=L[k][1:n-1]
        L[k]=I
    return L

def liste_triée():
    L=liste_sans_guillemets()
    T=sorted(L)
    return T

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def score_prenom(prenom):
    n=len(prenom)
    s=0
    for i in range(n):
        for k in range(26):
            if prenom[i]==alphabet[k]:
                s+=k+1
    return s

def score_total():
    L=liste_triée()
    n=len(L)
    s=0
    for k in range(n):
        s=s+(k+1)*score_prenom(L[k])
    return s


        
    
    
        

          
    
    


