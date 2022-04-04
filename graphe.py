from copy import copy, deepcopy
# 1.1 Mots:

def pref(mot):
    tab=[]
    for index in range(len(mot)+1):
        tab.append(mot[0:index])
    return tab

def suf(mot):
    tab=[]
    for index in range(len(mot)+1):
        tab.append(mot[index:])
    return tab

def fact(mot):
    fact=[]
    for i in range(len(mot)+1):
        for j in range(len(mot)+1):
            if mot[i:j] not in fact:
                fact.append(mot[i:j])
    return fact

def miroir(mot):
    tab=''
    for i in range(len(mot)):
        tab+=mot[-i-1]
    return tab

# 1.2:

def concatene(lang1,lang2):
    lang3 = []
    for mot in lang1:
        for mot2 in lang2:
            newMot = mot+mot2
            if newMot not in lang3:
                lang3.append(newMot)
    return lang3

def puis(lang,nombre):
    save=copy(lang)
    for puiss in range(nombre-1):
        concat=concatene(save,lang)
        save=copy(concat)
    return concat

            
    return retour

    # 1.2.3 On ne peut faire la fonction calculant l'étoile d'un langage car elle 
    # tourenerai à l'infini et ne renverrai donc rien

def tousmots(lang,taille):
    langTousMots = copy(lang)
    for i in range(2,taille+1):
        langTousMots+=puis(lang,i)
    langTousMots+=['']
    return langTousMots
    
#1.3:

#1.3.1:
def defauto() : 
    autoVide={"alphabet":[],"etats": [],"transitions":[], "I":[],"F":[]}
    saisie = ""
    while saisie != "stop":
        saisie=input("entrez une lettre de votre alphabet (stop pour tout arreter)\n")
        if saisie in autoVide["alphabet"]:
            print("Cette lettre est déja dans l'alphabet")
        elif len(saisie)==1:
            autoVide['alphabet'].append(saisie)
        elif saisie!="stop":
            print("Une seul lettre!\n")
        

    saisie = ""     
    while saisie != "stop":
        saisie=input("entrez un de vos etats sous forme de nombre (stop pour tout arreter)\n")
        if saisie.isnumeric():
            if int(saisie) in autoVide["etats"]:
                print("Deja dans la liste")
            else:
                autoVide['etats'].append(int(saisie))
        elif saisie!="stop":
            print("Un etat doit être un nombre")

        
    saisie = ""
    while saisie != "stop":
        saisie=input("entrez une de vos transition sous la forme etat-lettre-etat, ex : 1-a-2 (stop pour tout arreter)\n")
        
        i=0
        etat1=''
        alpha=''
        etat2=''
        while saisie[i]!='-' and saisie!='stop':
            etat1+=saisie[i]
            i+=1
        i+=1

        while saisie[i]!='-' and saisie!='stop':
            alpha+=saisie[i]
            i+=1  
        i+=1

        if saisie!='stop' :
            for lettre in saisie[i:] :
                etat2+=lettre
        
            if (not etat1.isnumeric()) or (not etat2.isnumeric()):
                print(etat1)
                print(etat2)
                print("Les etats douvent être des nombres")
            else:
                etat1=int(etat1)
                etat2=int(etat2)
                if [int(etat1),alpha,int(etat2)] in autoVide["transitions"]:
                    print("Deja dans la liste")
                elif (etat1 in autoVide["etats"]) and (etat2 in autoVide["etats"]) and (alpha in autoVide["alphabet"]):
                    autoVide['transitions'].append([int(etat1),alpha,int(etat2)])
                else:
                    print("Cette transition n'est pas valable")
            
    saisie = ""
    while saisie != "stop":
        saisie=input("entrez un de vos etats initiaux (stop pour tout arreter)\n")
        if not saisie.isnumeric():
            print("Un etat doit être un nombre")
        elif int(saisie) in autoVide["I"]:
            print("Deja dans la liste")
        elif int(saisie) in autoVide["etats"]:
            autoVide['I'].append(int(saisie))
        else:
            print(saisie +" ne fait pas partie des etats de l'automate\n")
   
    saisie = ""
    while saisie != "stop":
        saisie=input("entrez un de vos etats finaux (stop pour tout arreter)\n")
        if not saisie.isnumeric():
            print("Un etat doit être un nombre")
        elif int(saisie) in autoVide["F"]:
            print("Deja dans la liste")
        elif int(saisie) in autoVide["etats"]:
            autoVide['F'].append(int(saisie))
        else:
            print(saisie +"ne fait pas partie des etats de l'automate\n")
    
    return autoVide

#1.3.2:
def lirelettre(transitions, etats, lettre):
    retour = []   
    for etatDepart in etats:
        for transition in transitions:
            if transition[0] == etatDepart and transition[1]==lettre and transition[2] not in retour:
                retour.append(transition[2])
     
    return retour

#1.3.3:
def liremot(transitions, etats, mot):  
    for lettre in mot:
        etats = lirelettre(transitions, etats, lettre) 
    return etats

#1.3.4:
def accepte(auto,m):
    resultat = False
    EtatFinDeMot = liremot(auto['transitions'],auto["I"],m)
    if len(EtatFinDeMot)>0:
        for etat in EtatFinDeMot:
            if etat in auto["F"]:
                resultat = True
                break
    return resultat

#1.3.5
def langage_accept(automate, longueur):
    ToutMot = tousmots(automate["alphabet"], longueur)
    ListeResultat = []
    for mot in ToutMot:
        if accepte(automate, mot):
            ListeResultat.append(mot)
    return ListeResultat

#1.3.6
#On ne peut pas faire le langage accepté par l'automate car ce dernier peut avoir des mots infinis
#ce qui n'est ps vérifiable
 
#2

#2.1
def deterministe(auto):
    if len(auto["I"])>1:
        return False
    
    for transi in auto['transitions']:
        for transi2 in auto['transitions']:
            if transi[0]==transi2[0] and transi[1]==transi2[1] and transi[2] != transi2[2]:
                return False
    return True

#2.2
def determinise(auto):
    if deterministe(auto):
        return auto
    
    newAuto = {}
    newAuto['I']=copy([auto['I']])
    newAuto['F']=copy(auto['F'])
    newAuto['alphabet']=copy(auto['alphabet'])
    newAuto['etats']=copy([newAuto["I"]])
    newAuto['transitions']=[]

    noeudATraiter=copy(newAuto['I'])
    index=0
    while True:

        
        for lettre in newAuto["alphabet"]:
            
            etat=lirelettre(auto["transitions"],noeudATraiter[index],lettre)

            if etat!=[]:
                if [noeudATraiter[index],lettre,etat] not in newAuto["transitions"]:
                    newAuto["transitions"].append([noeudATraiter[index],lettre,etat])
                
                if etat not in newAuto["etats"]:
                    newAuto["etats"].append(etat)
                
                if etat not in noeudATraiter:
                    noeudATraiter.append(etat)
                    
        
        if index==len(noeudATraiter)-1:
            break

        index+=1
            
        
   
    return newAuto

#3

#3.1
def complet(auto):
    for etat in auto["etats"]:
        aVerifier=[]

        for transi in auto["transitions"]:
            if transi[0]==etat:
                aVerifier.append(transi)
        
        estDedans=False
        for lettre in auto['alphabet']:
            for transi in aVerifier:
                if transi[1]==lettre:
                    estDedans=True
            
            if not estDedans:
                return False
        
    return True

#3.2
def complete(auto):

    if complet(auto):
        return auto

    newAuto = deepcopy(auto)

    newAuto['etats'].append('LaPOUBELLE')

    for etat in newAuto["etats"]:
        aVerifier=[]

        for transi in newAuto["transitions"]:
            if transi[0]==etat:
                aVerifier.append(transi)
        
        print(aVerifier)
        
        
        for lettre in auto['alphabet']:
            estDedans=False
            for transi in aVerifier:
                if transi[1]==lettre:
                    estDedans=True
            
            if not estDedans:
                newAuto['transitions'].append([etat,lettre,'LaPOUBELLE'])

    return newAuto

        
        


  




        
if __name__=='__main__':

    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],
    "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}

    auto ={"alphabet":['a','b'],"etats": [1,2,3,4],
    "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[2,'b',4],[3,'a',4]],
    "I":[1],"F":[4]}

    auto1 ={"alphabet":['a','b'],"etats": [0,1],
    "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

    print(complete(auto0))