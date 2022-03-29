# 1.1 Mots:

from copy import copy


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
    
if __name__=='__main__':
    auto = defauto()
    print(auto)