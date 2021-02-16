import json
import csv

def recherche(villeRecherche):
    with open('Alentours de Toulouges.csv', newline='') as f:
        tableau = []
        csvCity = []
        lire = csv.reader(f)
        for ligne in lire:
            tableau.append(ligne)
            if ligne[0] == villeRecherche:
                if len(csvCity) < 40:
                   yolo = ligne[1].split(";")
                   dic = {"ville":ligne[0], "pays": yolo[0], "date": yolo[1],"temp":yolo[2],"min":yolo[3],"max":yolo[4]}
                   csvCity.append(dic)
    jsondata = json.dumps(csvCity).encode("utf8")
    copieJson(jsondata)
    return csvCity

def copieJson(tab):
    fichier = open("json.json", "wb")
    fichier.write(tab)
    fichier.close()
    print("Copie Json Terminée")

def copie(tab):
    entetes = [
        u'Ville',
        u'Temp',
        u'Min',
        u'Max',
        u'Date'
    ]
    yolo = tab.split(";")
    f = open('data.csv', 'w')
    ligneEntete = ";".join(entetes) + "\n"
    f.write(ligneEntete)
    i = 0
    print(yolo)
    for valeur in yolo:
        print(valeur)
        if i < 5 :
            f.write(valeur)
            f.write(";")
            i = i +1
        else:
            i = 0
            f.write("\n")
    f.close()