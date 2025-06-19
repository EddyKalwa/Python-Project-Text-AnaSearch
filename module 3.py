from collections import defaultdict
def creer_index(documents):
    index = defaultdict(set)
    for nom,mots in documents.items():
        for mot in mots:
            index[mot].add(nom)
    return dict(index)

def recherche_mot(index,mot_cle):
    mot_cle = mot_cle.lower()
    return index.get(mot_cle,set())

def recherche_mot_dans_contenu(documents,mot):
    resultat={}
    mot=mot.lower()
    for nom,lignes in documents.items():
        lignes_trouvees = []
        for ligne in lignes:
            if mot in ligne.lower():
                lignes_trouvees.append(ligne.strip())
        if lignes_trouvees:
            resultats[nom]= lignes_trouvees
    return resultats
    
