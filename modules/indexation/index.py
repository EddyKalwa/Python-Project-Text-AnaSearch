from collections import defaultdict

def creer_index(documents):
    index = defaultdict(lambda: defaultdict(int))
    for nom, mots in documents.items():
        for mot in mots:
            mot = mot.lower()
            index[mot][nom] += 1
    return {mot: dict(freqs) for mot, freqs in index.items()}

def recherche_mot(index, mot_cle):
    mot_cle = mot_cle.lower()
    return index.get(mot_cle, {})

def recherche_mot_dans_contenu(documents, mot):
    resultat = {}
    mot = mot.lower()
    for nom, lignes in documents.items():
        lignes_trouvees = []
        for ligne in lignes:
            if mot in ligne.lower():
                lignes_trouvees.append(ligne.strip())
        if lignes_trouvees:
            resultat[nom] = lignes_trouvees
    return resultat
