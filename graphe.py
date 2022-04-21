from copy import copy, deepcopy
# 1.1 Mots:

def pref(mot):
    '''fonction qui calcul tout les prefixes d'un mot'''
    tab=[]
    for index in range(len(mot)+1):
        tab.append(mot[0:index])
    return tab

def suf(mot):
    '''fonction qui calcul tout les suffixes d'un mot'''
    tab=[]
    for index in range(len(mot)+1):
        tab.append(mot[index:])
    return tab

def fact(mot):
    '''fonction qui calcul tout les facteurs d'un mot'''
    fact=[]
    for i in range(len(mot)+1):
        for j in range(len(mot)+1):
            if mot[i:j] not in fact:
                fact.append(mot[i:j])
    return fact

def miroir(mot):
    '''fonction renverse un mot donné en parametre'''
    tab=''
    for i in range(len(mot)):
        tab+=mot[-i-1]
    return tab

# 1.2:

def concatene(lang1,lang2):
    '''fonction qui calcul tous les produits de concatenation
        possibles dans deux languages'''

    lang3 = []                     
    for mot in lang1:               #on parcours les deux languages
        for mot2 in lang2:          #puis on additionne chaque mot
            newMot = mot+mot2       #à tout les mots de l'autre language.
            if newMot not in lang3: 
                lang3.append(newMot)#si le nouveau mot n'existe pas déja on l'ajoute à la liste de retour
    return lang3

def puis(lang,nombre):
    '''fonction qui calcule la puissance d'un language'''
    save=copy(lang)
    for puiss in range(nombre-1):  #On vient concatener le language
        concat=concatene(save,lang)#a lui même autant de fois qu'il y a de puissance
        save=copy(concat)
    return concat

    # 1.2.3 On ne peut faire la fonction calculant l'étoile d'un langage car elle 
    # tourenerai à l'infini et ne renverrai donc rien

def tousmots(lang,taille):
    '''fonction qui renvoie tout les mots entre 0 et taille
        composé de lettre apartenant à lang'''

    langTousMots = copy(lang)       #les mots de longueur 1 sont les lettres qui composnet le language
    for i in range(2,taille+1):     #Trouver les mots de longueur 2 revien a faire lang^2
        langTousMots+=puis(lang,i)  #En utilisant ce principe et la fonction puis on trouve tout les mots que l'on cherche
    langTousMots+=['']                    
    return langTousMots
    
#1.3:

#1.3.1:
def defauto() : 
    '''fonction permettant de saisir un automate'''

    autoVide={"alphabet":[],"etats": [],"transitions":[], "I":[],"F":[]} #initialisation

    saisie = ""
    while saisie != "stop": #saisie de l'alphabet
        saisie=input("entrez une lettre de votre alphabet (stop pour tout arreter)\n")
        if saisie in autoVide["alphabet"]:
            print("Cette lettre est déja dans l'alphabet")
        elif len(saisie)==1:
            autoVide['alphabet'].append(saisie)
        elif saisie!="stop":
            print("Une seul lettre!\n")
        

    saisie = ""     
    while saisie != "stop": #saisie des etats
        saisie=input("entrez un de vos etats sous forme de nombre (stop pour tout arreter)\n")
        if saisie.isnumeric():
            if int(saisie) in autoVide["etats"]:
                print("Deja dans la liste")
            else:
                autoVide['etats'].append(int(saisie))
        elif saisie!="stop":
            print("Un etat doit être un nombre")

        
    saisie = "" #saisie des transitions
    while saisie != "stop":
        saisie=input("entrez une de vos transition sous la forme etat-lettre-etat, ex : 1-a-2 (stop pour tout arreter)\n")
        
        i=0
        etat1=''
        alpha=''
        etat2=''
        while saisie[i]!='-' and saisie!='stop': #les etats peuvent être des nombres de plusieurs chiffre
            etat1+=saisie[i]
            i+=1
        i+=1

        while saisie[i]!='-' and saisie!='stop':#les étiquettes peuvent être des mots
            alpha+=saisie[i]
            i+=1  
        i+=1

        if saisie!='stop' :
            for lettre in saisie[i:] :
                etat2+=lettre
        
            if (not etat1.isnumeric()) or (not etat2.isnumeric()):#on verifie la validité de la transition
                print(etat1)
                print(etat2)
                print("Les etats douvent être des nombres")
            else:
                etat1=int(etat1)
                etat2=int(etat2)
                if [int(etat1),alpha,int(etat2)] in autoVide["transitions"]:#on verifie que l'etat n'est pas déja contenu dans la liste
                    print("Deja dans la liste")
                elif (etat1 in autoVide["etats"]) and (etat2 in autoVide["etats"]) and (alpha in autoVide["alphabet"]):
                    autoVide['transitions'].append([int(etat1),alpha,int(etat2)])
                else:
                    print("Cette transition n'est pas valable")
            
    saisie = ""
    while saisie != "stop": #saisie des etats initiaux
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
    while saisie != "stop":#saisie des etats finaux
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
    '''fonction qui renvoie la liste des etats accessible en lisant 'lettre' '''
   
    retour = []   
    for etatDepart in etats:
        for transition in transitions:                                                                 #on parcour les transition
            if transition[0] == etatDepart and transition[1]==lettre and transition[2] not in retour:  #si l'etiquette et la bonne et que la transition 
                retour.append(transition[2])                                                           #n'est pas déja enregistrée on l'ajoute
     
    return retour

#1.3.3:
def liremot(transitions, etats, mot): 
    '''fonction qui renvoie la liste des etats dans lesquel on peut arriver
       en partant de 'etat' et en lisant  'mot' ''' 
    for lettre in mot:                                  #pour chacune des lettres on recupère l'etat
        etats = lirelettre(transitions, etats, lettre)  #dans lequel on arrive en lisant cette lettre
    return etats                                        

#1.3.4:
def accepte(auto,m):
    '''renvoie vrai si 'm' est accepté par 'auto' false sinon'''
    resultat = False
    EtatFinDeMot = liremot(auto['transitions'],auto["I"],m) #On récupère les etats dans lesquels on arrive avec le mot
    if len(EtatFinDeMot)>0:                                 #Si il y en as et que l'un d'entre eux est final alors on 
        for etat in EtatFinDeMot:                           #renvoie vrai, sinon on renvoie false
            if etat in auto["F"]:
                resultat = True
                break
    return resultat

#1.3.5
def langage_accept(automate, longueur):
    '''renvoie le language accepté comportant des mots de taille maximum 'longueur' '''
    
    ToutMot = tousmots(automate["alphabet"], longueur) #on créé tout les mots possibles avec l'alphabet du graph
    ListeResultat = []
    for mot in ToutMot:                                #pour chacun de ses mots
        if accepte(automate, mot):                     #on regarde si il est accepté
            ListeResultat.append(mot)
    return ListeResultat

#1.3.6
#On ne peut pas faire le langage accepté par l'automate car ce dernier peut avoir des mots infinis
#ce qui n'est ps vérifiable
 
#2

#2.1
def deterministe(auto):
    '''renvoie true si l'auto est deterministe, false sinon'''
    if len(auto["I"])>1:                     #Si il y a plus d'un etat initial
        return False                         #
                                             #
    for transi in auto['transitions']:       #ou qu'il existe deux transition partant du
        for transi2 in auto['transitions']:  #même etat avec la même étiquette
            if transi[0]==transi2[0] and transi[1]==transi2[1] and transi[2] != transi2[2]:
                return False                 #on renvoie false
    return True

#2.2
def determinise(auto):
    '''fonction qui determinise un auto'''

    if deterministe(auto): #si l'auto est déja determinisé on ne le fait pas
        return auto
    
    newAuto = {}
    newAuto['alphabet']=copy(auto['alphabet'])
    newAuto['I']=copy([auto['I']])
    newAuto['etats']=copy(newAuto["I"])
    newAuto['transitions']=[]

    noeudATraiter=copy(newAuto['I']) #on commence en partant de l'ensemble des états initiaux
    index=0
    while True:

        
        for lettre in newAuto["alphabet"]:
            
            etat=lirelettre(auto["transitions"],noeudATraiter[index],lettre) #on récupère les etats accessible pour chacune des lettres

            if etat!=[]:
                if [noeudATraiter[index],lettre,etat] not in newAuto["transitions"]: #on ajoute la transition qui en découle
                    newAuto["transitions"].append([noeudATraiter[index],lettre,etat])
                
                if etat not in newAuto["etats"]:    #on ajoute le nouvel etat si il n'est pas deja dedans
                    newAuto["etats"].append(etat)
                
                if etat not in noeudATraiter:       #puis on ajoute ce nouvel etat dans la liste de ceux à traiter (si il n'est pas déja dedans)
                    noeudATraiter.append(etat)
                    
        
        if index==len(noeudATraiter)-1:#si on arrive au bout de la boucle on sors de la boucle
            break

        index+=1     
    
    newAutoEtatFinal = []
    for etat in newAuto["etats"]: #On viens ensuite remplir les etats et les etats finaux 
        for etatFinal in auto["F"]:
            if etatFinal in etat and etat not in newAutoEtatFinal:
                newAutoEtatFinal.append(etat)
    
    newAuto['F']=newAutoEtatFinal
    return newAuto

#2.3
def renommage(auto):
    '''fonction qui renomme les etats d'un automate'''

    dictRenommage = {}
    nouvEtat = 0

    for etat in auto["etats"]: #on associe chaque etat à un nombre en partant de 0
        dictRenommage[str(etat)]=nouvEtat
        nouvEtat+=1
    
    nouvEtatInit = []
    for etat in auto["I"]:#on parcours tout les états initiaux et on récupère le nombre associé
        nouvEtatInit.append(dictRenommage[str(etat)])

    nouvEtatFin = []
    for etat in auto["F"]:#la même chose avec les etats finaux
        nouvEtatFin.append(dictRenommage[str(etat)])

    nouvEtats = []
    for etat in auto["etats"]:#La même chose avec l'integralité des etats
        nouvEtats.append(dictRenommage[str(etat)])

    nouvTransi = []
    for transition in auto["transitions"]:#Principe similaire, cette fois ci sur deux états en même temps
        nouvTransi.append([dictRenommage[str(transition[0])],transition[1],dictRenommage[str(transition[2])]])

    #enfin on copie le tout dans un nouvel automate
    return {"alphabet":auto["alphabet"], "etats":nouvEtats, "transitions":nouvTransi , "I":nouvEtatInit, "F":nouvEtatFin}

#3

#3.1
def complet(auto):
    '''renvoie true si l'automate est complet, false sinon'''
    
    for etat in auto["etats"]: #on aprcours tout les etats
        aVerifier=[]

        for transi in auto["transitions"]: #puis toute les transition
            if transi[0]==etat:            #si il y en a une qui part de l'etat
                aVerifier.append(transi)   #on l'ajoute à la liste des transitions a verifier
        
        estDedans=False
        for lettre in auto['alphabet']: #pour chacune des lettres
            for transi in aVerifier:    #on regarde si elle sont dans au moins une des transition
                if transi[1]==lettre:
                    estDedans=True
            
            if not estDedans:   #si une lettre n'est pas dans les transition à verifier 
                return False    #alors l'automate est incomplet
        
    return True

#3.2
def complete(auto):
    '''fonction qui complète un automate passé en paramettre'''

    if complet(auto):#si l'automate est complet alors on ne le complète pas
        return auto

    newAuto = deepcopy(auto)

    laPOUBELLE = auto['etats'][-1]+1 #On crée un etat puis
    newAuto['etats'].append(laPOUBELLE)

    for etat in newAuto["etats"]: 
        aVerifier=[]

        for transi in newAuto["transitions"]:
            if transi[0]==etat:
                aVerifier.append(transi)       
        
        for lettre in auto['alphabet']:
            estDedans=False
            for transi in aVerifier:
                if transi[1]==lettre:
                    estDedans=True
                                                                        #en reprenant le principe de complete
            if not estDedans:                                           #si un etat n'est pas complet on ajoute 
                newAuto['transitions'].append([etat,lettre,laPOUBELLE]) #des transitions avec les lettres manquantes dans le puis

    return newAuto

#3.3
def complement(auto):  
    '''fonction qui renvoie le complement d'un automate passé en parametre'''

    auto=renommage(determinise(auto)) #on commence par le determiniser

    if complet(auto):                 #puis on le complète
        newAuto=deepcopy(auto)
    else:
        newAuto=complete(auto)

    final=[]
    
    for  etat in newAuto['etats']: #on remplace les etats finaux par tout les etats qui ne le sont pas
        if etat not in newAuto['F']:
            final.append(etat)
    newAuto['F']=final

    return newAuto   

#4
def prod(auto1,auto2):
    '''fonction qui renvoie le produit de deux automates passés en parametre'''

    #on récupère tout ce qu'on peut récupérer sans traitement (les nouveaux etats initiaux)
    newAuto={}
    newAuto["I"] = [(auto1["I"][0],auto2["I"][0])]
    newAuto["F"] = []
    newAuto["etats"]=[(auto1["I"][0],auto2["I"][0])]
    alphabet = list(set(copy(auto1["alphabet"]+auto2["alphabet"])))
    alphabet.sort()
    newAuto["alphabet"] = alphabet
    newAuto["transitions"]=[]

    aVerifier = copy(newAuto["I"])
    while len(aVerifier)!=0: #tant qu'il y a des etats a verifier

        Etat1 = aVerifier[-1][0] #on récupère le couple a la fin de la liste
        Etat2 = aVerifier[-1][1] #
        aVerifier.pop()          #couple qu'on retire

        for lettre in newAuto["alphabet"]:                              #pour chacune des lettres
            Etat1Tmp = lirelettre(auto1["transitions"],[Etat1],lettre)  #on récupère les transition d'arrivé
            Etat2Tmp = lirelettre(auto2["transitions"],[Etat2],lettre)  #des deux états
            
            if len(Etat1Tmp)!=0 and len(Etat2Tmp)!=0:   #si aucun des etats d'arrivés est null
                newEtat1 = Etat1Tmp[0]
                newEtat2 = Etat2Tmp[0]
                
                if (newEtat1,newEtat2) not in newAuto["etats"]:                          #on verifie qu'il ne soient pas déja traité
                    aVerifier.append((newEtat1,newEtat2))                                #puis on les ajoute dans la liste des etats à traiter
                    newAuto["etats"].append((newEtat1,newEtat2))                         #et dans les etats du nouvel auto
                newAuto["transitions"].append([(Etat1,Etat2),lettre,(newEtat1,newEtat2)])#puis on ajoute la nouvelle transition
        
    return newAuto

#4.1

def inter(auto1, auto2):
    '''fonction qui renvoie l'intersection entre deux automates'''

    newAuto=prod(auto1,auto2)                               #On fait l'automate produit
    for etat in newAuto["etats"]:                           #puis on déclare finaux les états qui ne contienne 
        if etat[0] in auto1["F"] and etat[1] in auto2["F"]: #que des etats finaux des deux etats initiaux
            newAuto["F"].append((etat[0],etat[1]))
    return newAuto

#4.2

def difference(auto1, auto2):
    '''fonction qui renvoie la différence entre deux automates'''

    if (not complet(auto1)): #on complète les deux automates
        auto1=complete(auto1)

    if (not complet(auto2)):
        auto2=complete(auto2)

    newAuto = prod(auto1,auto2) #on fait le produit entre les deux

    for etat in newAuto["etats"]:
        if etat[0] in auto1["F"] and etat[1] not in auto2["F"]: #on déclare comme finaux les etats
            newAuto["F"].append((etat[0],etat[1]))              #qui contienne des etats finaux du premier automate
    return newAuto                                              #sans contenir un etat final du second

#5 

def EtatsCoaccessibles(auto):
    '''fonction qui renvoie les etats coaccessibles d'un automate passé en parametre'''

    index = 0
    etatsCoaccessibles = copy(auto["F"])
    while index <len(etatsCoaccessibles):                                                           #tant qu'on ajoute des etats aux etats coaccessible
        for transition in auto["transitions"]:                                                      #on regarde quels sont les etats depuis lesquels on 
            if transition[2]==etatsCoaccessibles[index] and transition[0] not in etatsCoaccessibles:#accède aux etats coaccessible, que l'on vient ajouter
                etatsCoaccessibles.append(transition[0])                                            #a la liste des etats coaccessible
        index+=1
    return etatsCoaccessibles

def EtatsAccessibles(auto):
    '''fonction qui renvoie les etats accessibles d'un automate passé en parametre'''
    
    index = 0
    EtatsAccessibles = copy(auto["I"])
    while index <len(EtatsAccessibles):             #même principes en regardant cette fois ci les etats
        for transition in auto["transitions"]:      #accessible depuis la liste des etats accessibles
            if transition[0]==EtatsAccessibles[index] and transition[2] not in EtatsAccessibles:
                EtatsAccessibles.append(transition[2])
        index+=1
    return EtatsAccessibles


def emondage(auto):
    '''fonction renvoyant un automate emondé d'un automate passé en parametre'''

    newAuto = deepcopy(auto)
    etatsAccesibles = EtatsAccessibles(auto)     #on récupère les états accessibles
    etatsCoaccessibles = EtatsCoaccessibles(auto)#et coaccessible
    
    for etat in auto["etats"]: #on vient retirer les etats qui ne sont ni accessibles ni coaccessible
        if (etat not in etatsAccesibles) or (etat not in etatsCoaccessibles):
            newAuto["etats"].remove(etat)

    for transition in auto["transitions"]:#puis on retire les transitions qui sont devenues inutiles
        if (transition[0] not in newAuto["etats"]) or (transition[2] not in newAuto["etats"]):
            newAuto["transitions"].remove(transition)    
        
    return newAuto

#5.1

def prefixe(auto):
    '''fonction qui renvoie un automate acceptant les prefixe d'un automate passé en parametre'''

    auto=emondage(auto) #on émonde l'automate
    newAuto=deepcopy(auto)
    newAuto["F"]=copy(newAuto["etats"]) #on designe tout les etats comme finaux
    return newAuto

#5.2

def suffixe(auto):
    '''fonction qui renvoie un automate acceptant les suffixes d'un automate passé en parametre'''

    auto=emondage(auto) #on émonde l'automate
    newAuto=deepcopy(auto)
    newAuto["I"]=copy(newAuto["etats"]) #on designe tout les etats comme initiaux
    return newAuto

#5.3
def facteur(auto):
    '''fonction qui renvoie un automate acceptant les facteurs d'un automate passé en parametre'''

    auto=emondage(auto) #on émonde l'automate
    newAuto=deepcopy(auto)
    newAuto["I"]=copy(newAuto["etats"])#on designe tout les etats comme initiaux
    newAuto["F"]=copy(newAuto["etats"])#on designe tout les etats comme finaux
    return newAuto

#5.4
def mirroir(auto):
    '''fonction qui renvoie l'automate miroir d'un automate passé en parametre'''

    #on copie tout l'automate sans les transition, en inversant les etats initiaux et finaux
    newAuto={}
    newAuto["alphabet"]=copy(auto["alphabet"])
    newAuto["etats"]=copy(auto["etats"])
    newAuto["I"]=copy(auto["F"])
    newAuto["F"]=copy(auto["I"])
    newAuto["transitions"]=[]

    for transition in auto["transitions"]:#on ajoute les transition en les inversants au passage
        newAuto["transitions"].append([transition[2],transition[1],transition[0]])
    return newAuto

#6
def accesible(auto):
    '''fonction qui renvoie l'automate accessible d'un automate passé en parametre'''

    etatsAccessibles = EtatsAccessibles(auto)#on récupère tout les etats accessibles
    etatsCorriges = []
    
    for etat in auto["etats"]:#puis on actualise les etats
        if (etat not in etatsAccessibles) and (etat not in auto["I"]):
            continue
        etatsCorriges.append(etat)
    auto["etats"]=etatsCorriges
    
    return auto

def premiereDecoupe(auto):
    '''fonction qui renvoie une liste contenant une liste d'etat finaux
        et une liste d'etats non finaux d'un automate passé en parametre'''

    etatsMini=[auto["F"]]#on récupère les etats finaux
    temporaire=[]
    
    for etat in auto["etats"]:
        if etat not in auto["F"]:#puis les etats non finaux
            temporaire.append(etat)
    
    etatsMini.append(temporaire)
    
    return etatsMini
    
def equivalent(listeEquivPre,auto):
    '''fonction qui renvoie une découpe actualisée des états équivalents'''

    listeEquivFin = []
    
    for liste in listeEquivPre:#pour chacune des classes d'équivalence
        triage={}

        if len(liste)==1:#si la classe est composé d'un seul etat pas besoin de l'actualiser
            listeEquivFin.append(liste)
            continue
        
        for etat in liste:#pour chacun des etats dans la classe d'équivalence
            value={}
            for lettre in auto["alphabet"]: #pour chacune des lettres de l'alphabet
               etatTmp = lirelettre(auto["transitions"],[etat],lettre)#on regarde la classe d'equivalence dans laquel arrive l'etat en lisant la lettre
               for classeEquiv in listeEquivPre:
                   if etatTmp[0] in classeEquiv:
                       classe = classeEquiv
                       break
               value[lettre]=tuple(classe) #a chacune des lettres on associe la classe d'equivalence de l'etat
            
            assos=False
            for key,values in triage.items():#pour chaque classe d'equivalence et classe d'arrivée associée
                if values==value:            #si la classe d'arrivée est égale à celle calculée pour l'état
                    assos=True

                    newkey=[]
                    for elem in key:        #on crée une nouvelle clef contenant l'etat
                        newkey.append(elem)
                    newkey.append(etat)

                    triage[tuple(newkey)]=values #on remplace la classe déquivalence en y ajoutant la nouvelle clef
                    triage.pop(key)              #sans oublier de supprimer l'ancienne clef
                    break

            if not assos:                       #si aucune des classes d'arrivé ne correspond a celle de l'etat
                triage[tuple([etat])]=value     #on génère un nouvelle classe d'équivalence
        
        for key in triage.keys():   #on renvoie une nouvelle liste de classe d'equivalence 
            listeEquivFin.append(list(key))

    return listeEquivFin        
               
def minimise(auto):
    '''fonction qui renvoie l'automate minimal d'un automate passé en paramettre'''

    newAuto = {}
    newAuto["alphabet"]=deepcopy(auto["alphabet"])
    ListeEquiv = premiereDecoupe(auto)
    ListeEquivPre=[]
    
    while ListeEquiv != ListeEquivPre: #tant que l'ancienne et la nouvelle liste de classe d'équivalence n'est pas identique
        ListeEquivPre = ListeEquiv
        ListeEquiv = equivalent(ListeEquivPre,auto) #on actualise la liste de classe d'équivalence

    newAuto["etats"] =ListeEquiv #une fois la liste de classe d'equivalence calculé elle est considéré comme les etats de l'automate
    
    ListeEtatFinaux=[]
    for etat in auto["F"]: #on ajoute aux etats finaux tout les etats qui contienne au moins un etat final
        for classe in newAuto["etats"]:
            if etat in classe and classe not in ListeEtatFinaux:
                ListeEtatFinaux.append(classe)
    newAuto["F"] = ListeEtatFinaux

    EtatInitial=[]
    for classe in newAuto["etats"]:#definie l'etat initial 
        if auto["I"][0] in classe:
            EtatInitial.append(classe)
            break
    newAuto["I"] = EtatInitial

    newAuto["transitions"]=[]#on redefinie les transitions
    for classe in newAuto["etats"]:
        etat = classe[0]
        for lettre in newAuto["alphabet"]:
            etatArrivee = lirelettre(auto["transitions"],[etat],lettre)
            if len(etatArrivee)!=0:
                for classeEqui in newAuto["etats"]:
                    if etatArrivee[0] in classeEqui:
                        newAuto["transitions"].append([classe,lettre,classeEqui])
                        break
    return newAuto 





if __name__=='__main__':

    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],
    "transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}

    auto ={"alphabet":['a','b'],"etats": [1,2,3,4],
    "transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[2,'b',4],[3,'a',4]],
    "I":[1],"F":[4]}

    auto1 ={"alphabet":['a','b'],"etats": [0,1],
    "transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

    auto2={"alphabet":['a','b'],"etats": [0,1],
    "transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}

    auto3 ={"alphabet":['a','b'],"etats": [0,1,2,],
    "transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}

    auto4 ={"alphabet":['a','b'],"etats": [0,1,2,],
    "transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}

    auto5 ={"alphabet":['a','b'],"etats": [0,1,2],
    "transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]],
    "I":[0],"F":[0,1]}

    auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],
    "transitions":[[0,'a',1],[1,'b',2],[3,'a',3], [0,'a',4], [5,'b',2]],
    "I":[0],"F":[2]}
    
    auto7 ={"alphabet":['a','b'], "etats":[1,2,3,4,5], "I":[1],"F":[4,5],"transitions":[[1,'a',1],[1,'a',2],[2,'a',5],[2,'b',3],[5,'b',5],[3,'b',3],[3,'a',4]]}
    
    auto8 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],"transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],"I":[0],"F":[0,1,2,5]}

    #print(complement(auto3))
    #print(prod(auto4,auto5))
    #print(renommage(inter(auto4,auto5)))
    #print(renommage(difference(auto4,auto5)))
    #print(emondage(auto6))
    #print(mirroir(auto7))
    print(renommage(minimise(auto8)))