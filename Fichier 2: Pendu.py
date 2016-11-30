score=0
pseudo=input("Bienvenue, quel est votre nom ? ")
print("Vous avez le droit à 8 coups pour deviner, vous gagnerez autant de points qu'il vous restera de chances. C'est parti, {} !".format(pseudo))
import pickle
try:
    with open("scores","rb") as sco:
        m=pickle.Unpickler(sco)
        dicoScore=m.load()
        if pseudo in dicoScore.keys():
            score=dicoScore[pseudo]
except:
    with open("scores","wb")as sco:
        dicoScore={"initialisation":1}
        p=pickle.Pickler(sco)
        p.dump(dicoScore)
print("Votre score est de {}".format(score))
jouer=True
from random import randrange
while jouer==True:
    mot=dico[randrange(len(dico)-1)]
    print("Voyons le mot une première fois :")
    for i in mot : print("*",end="")
    i=0
    lettresTrouvees=[]
    while i<8:
        essai=input("\nVeuillez essayer une lettre : ")
        if essai in mot:
            print("Bravo ! Cette lettre est dans le mot")
            lettresTrouvees.append(essai)
        else:
            print("Tant pis ! Cette lettre n'est pas dans le mot.")
        j=0
        print("Voyons le mot après cet essai :")
        entracte=""
        while j<len(mot):
            if mot[j] in lettresTrouvees :
                entracte+=mot[j]
            else:
                entracte+="*"
            j+=1
        print(entracte)
        if entracte == mot:
            print("Bravo !! Vous avez trouvé au tour", (i+1), "vous gagnez donc", (7-i),"point(s)")
            score=score+7-i
            break
        i+=1
    print("Votre score est maintenant de",score,"point(s)")
    n=input("Voulez-vous encore jouer ? Tapez o pour continuer, ou n pour quitter ")
    if n=="n":
        jouer=False
dicoScore[pseudo]=score
with open("scores","wb") as sco:
    m=pickle.Pickler(sco)
    m.dump(dicoScore)
dico=["moins","de","huit","lettres","ces","sympa"]
