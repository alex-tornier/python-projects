import random

cheat = 0

print("NIVEAUX : \"Débutant\" (10 vies) \"Intermédiaire\" (5 vies) \"Expert\" (1 vie)")
lvl = input("choisissez votre niveaux : ")

if lvl == "débutant" or lvl == "debutant" or lvl == "Débutant" or lvl == "Debutant":
    vie = 10
    print("vous avez choisit le mode débutant")
elif lvl == "intermédiaire" or lvl == "intermediaire" or lvl == "Intermédiaire" or lvl == "Intermediaire":
    vie = 5
    print("vous avez choisit le mode intermédiaire")
elif lvl == "Expert" or lvl == "expert":
    vie = 1
    print("vous avez choisit le mode expert")
elif lvl == "cheat":
    vie = 100
    cheat = 1
else:
    print("\naucun niveaux choisit, niveaux débutant (10 vies) sélectioné par default\n")
    vie = 10

with open('dico_france.txt', 'rt', encoding='latin1') as dico:
    """#lit le nombre de lignes (mais empeche la suite de fonctionner)
    nb_lignes = len(dico.readlines())
    print('lignes : ', nb_lignes)
    """

    rd_nb = random.randint(0, 22740)


    all_lines = dico.readlines()

mot_choisis = all_lines[rd_nb]

mot_choisis=mot_choisis.lower()

dico.close()

if cheat == 1:
    print(mot_choisis)
longueur = len(mot_choisis) - 1

mot_choisis = mot_choisis.rstrip()
mot_devine = "-" * len(mot_choisis)
print(mot_devine)

lettres_deja_proposees = []

while mot_devine != mot_choisis and vie != 0:
    print("il vous reste : ", vie, " vies")
    print("Vous avez proposée : ", lettres_deja_proposees)
    lettre = input("\nEntrez une lettre : ")

    if lettre not in mot_choisis and lettre not in lettres_deja_proposees:
        vie -= 1

    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [lettre]

    elif lettre in lettres_deja_proposees:
        print("\nla lettre \"", lettre,"\" à déja été proposé !\nAucune vie ne vous à été déduite\n")

    for i in range(len(mot_choisis)):
        if lettre == mot_choisis[i]:
            mot_devine = mot_devine[:i] + lettre + mot_devine[i + 1:]
    print(mot_devine)

if vie == 0:
    print("\nGame Over !\nLe mot a trouver était :", mot_choisis)
if mot_choisis == mot_devine:
    print('\n Félicitation ! Le mot :', mot_choisis, 'a été trouvé\n')
