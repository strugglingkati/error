strg = {}
def Entrer():
    global note2, note3
    print("0:retour")
    Ent = int(input("Déterminer le nombre de nouveaux stagiaires :"))
    if Ent == 0 or Ent == str:
        start()
    elif Ent == 1:
        print("0:retour")
        n = int(input("le nombre de stagiaire: "))
        if n == 0:
            start()
        elif n in strg.keys():
            print("Cet stagiaire est dans le système ")
            start()
        else:
            n = len(strg) + 1
            nom = input("ajouter nom: ")
            prenome = input("ajouter prenome: ")
            age = int(input("ajouter age: "))
            note1 = float(input("ajouter note1: "))
            if 0 <= note1 <= 20:
                note2 = float(input("ajouter note2: "))
            else:
                print("Ce format est incorrect ")
            if 0 <= note2 <= 20:
                note3 = float(input("ajouter note3: "))
            else:
                print("Ce format est incorrect ")
            if 0 <= note3 <= 20:
                moyenne = (note1 + note2 + note3) / 3
                strg[n] = {"nom": nom, "prenome": prenome, "age": age, "note1": note1, "note2": note2, "note3": note3,"moyenne":moyenne}
            else:
                print("Ce format est incorrect ")
    elif Ent > 1:
        for i in range(Ent):
            print("0:retour")
            n = int(input("le nombre de stagiaire: "))
            if n == 0:
                start()
            if n in strg.keys():
                print("Cet stagiaire est dans le système ")
            else:
                n = len(strg) + 1
                print("0:retour")
                nom = input("ajouter nom: ")
                prenome = input("ajouter prenome: ")
                age = int(input("ajouter age: "))
                note1 = float(input("ajouter note1: "))
                if 0 <= note1 <= 20:
                    note2 = float(input("ajouter note2: "))
                else:
                    print("Ce format est incorrect ")
                if 0 <= note2 < 20:
                    note3 = float(input("ajouter note3: "))
                else:
                    print("Ce format est incorrect ")
                if 0 <= note3 <= 20:
                    moyenne = (note1 + note2 + note3) / 3
                    strg[n] = {"nom": nom, "prenome": prenome, "age": age, "note1": note1, "note2": note2,"note3": note3,"moyenne":moyenne}
                else:
                    print("Ce format est incorrect ")
    else:
        start()
    start()
def Affichage():
    aff = int(input("0:retour \n1:Définir le stagiaire \n2:Consulter la liste de tous les stagiaires \n"))
    if aff == 1:
        print("0:retour")
        n = int(input("le nombre de stagiaire: "))
        if n == 0:
            start()
        if n in strg.keys():
            print(n, "=", strg[n])
            print(" ")
        else:
            print("Cet stagiaire n'est pas dans le système ")
            print(" ")
    elif aff == 2:
        for i in range(1, len(strg) + 1):
            print(i, "= ", strg[i])

    elif aff == 0:
        start()

    else:
        print("Le dossier est vide")
    start()
def Modifier():
    global note2, note3
    print("0:retour")
    n = int(input("le nombre de stagiaire: "))
    if n == 0:
        start()
    if n in strg.keys():
        print("0:retour")
        mod = int(input("1:Pour éditer le dossier complet du stagiaire \n2:Modification d'une case dans le dossier du stagiaire \n"))
        if mod == 0:
            start()
        elif mod == 1:
            nom = input("ajouter nom: ")
            prenome = input("ajouter prenome: ")
            age = int(input("ajouter age: "))
            note1 = float(input("ajouter note1: "))
            if 0 <= note1 <= 20:
                note2 = float(input("ajouter note2: "))
            else:
                print("Ce format est incorrect ")
            if 0 <= note2 <= 20:
                note3 = float(input("ajouter note3: "))
            else:
                print("Ce format est incorrect ")
            if 0 <= note3 <= 20:
                moyenne = (note1 + note2 + note3) / 3
                strg[n].update(
                    {"nom": nom, "prenome": prenome, "age": age, "note1": note1, "note2": note2, "note3": note3,"moyenne":moyenne})
            else:
                print("Ce format est incorrect ")
        elif mod == 2:
            print("0:retour")
            colonne = int(input("1:nom \n2:prenome \n3:age \n4:note1 \n5:note2 \n6:note3 \n"))
            if colonne == 0:
                start()
            elif colonne == 1:
                nom = str(input("ajouter nom: "))
                strg[n].update({"nom": nom})
            elif colonne == 2:
                prenome = str(input("ajouter prenome: "))
                strg[n].update({"prenome": prenome})
            elif colonne == 3:
                age = int(input("ajouter age: "))
                strg[n].update({"age": age})
            elif colonne == 4:
                note1 = float(input("ajouter note1: "))
                if 0 <= note1 <= 20:
                    strg[n].update({"note1": note1})
            elif colonne == 5:
                note2 = float(input("ajouter note2: "))
                if 0 <= note2 <= 20:
                    strg[n].update({"note2": note2})
                else:
                    print("Ce format est incorrect ")
            elif colonne == 6:
                note3 = float(input("ajouter note3: "))
                if 0 <= note3 <= 20:
                    strg[n].update({"note3": note3})
                else:
                    print("Ce format est incorrect ")
    else:
        print("Cet stagiaire n'est pas dans le système ")
    start()
def Supprimer():
    print("0:retour")
    n = int(input("le nombre de stagiaire: "))
    if n in strg.keys():
        strg.pop(n)
        if n< len(strg):


    elif n == 0:
        start()

    else:
        print("Cet stagiaire n'est pas dans le système ")
        start()
    start()
def Max():
    Maxc = strg[1].get("moyenne")
    for i in strg.keys():
        if Maxc <= strg[i].get("moyenne"):
            Maxc = strg[i].get("moyenne")
    print(Maxc)
    print()
    start()
def Min():
    Minc = strg[1].get("moyenne")
    for i in strg.keys():
        if Minc >= strg[i].get("moyenne"):
            Minc = strg[i].get("moyenne")
    print(Minc)
    print()
    start()
def Moyenne():
    Moyennec = 0
    for i in strg.keys():
        Moyennec = Moyennec + strg[i].get("moyenne")
    print(Moyennec / len(strg))
    print()
    start()
def start():
    print("Tapez le numéro de choix que vous voulez")
    tist = int(input("1:Entrer: \n2:Affichage: \n3:Modifier: \n4:Supprimer: \n5:Max: \n6:Min: \n7:Moyenne:  \n"))
    if tist == 1:
        Entrer()
    elif tist == 2:
        Affichage()
    elif tist == 3:
        Modifier()
    elif tist == 4:
        Supprimer()
    elif tist == 5:
        Max()
    elif tist == 6:
        Min()
    elif tist == 7:
        Moyenne()
    elif tist == 0:
        start()
    else:
        print("Ce format est incorrect! \nRappel Respectez de la ligne !!")
start()