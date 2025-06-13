# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from modules.pretraitement.traitement import read_text_files_from_folder, manage_document_collection
from modules.analyse_frequence.analyse import analyse_frequence_globale
from modules.indexation.index import creer_index, recherche_mot, recherche_mot_dans_contenu
from modules.moteur_recherche.moteur import search


def afficher_frequences(freqs, top_n=20):
    print(f"\n[INFO] Top {top_n} mots les plus fréquents :")
    top_items = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for mot, freq in top_items:
        print(f"{mot}: {freq}")

def afficher_resultats_recherche_docs(resultats):
    if resultats:
        print("\n[INFO] Documents contenant le mot clé :")
        for doc in resultats:
            print(f" - {doc}")
    else:
        print("\n[INFO] Aucun document ne contient ce mot clé.")

def afficher_resultats_recherche_lignes(resultats):
    if resultats:
        print("\n[INFO] Occurrences dans les documents :")
        for doc, lignes in resultats.items():
            print(f"\nDans {doc} :")
            for ligne in lignes:
                print(f"   > {ligne}")
    else:
        print("\n[INFO] Aucun contenu trouvé pour ce mot clé.")

def main():
    folder_path = input("Entrez le chemin du dossier contenant les fichiers texte : ").strip()

    print("[INFO] Chargement et prétraitement des documents...")
    documents_raw = read_text_files_from_folder(folder_path)
    if not documents_raw:
        print("[ERREUR] Aucun document chargé, arrêt du programme.")
        return
    
    documents_tokens = manage_document_collection(documents_raw)
    
    # Analyse fréquence globale
    freqs = analyse_frequence_globale(documents_tokens)
    afficher_frequences(freqs, top_n=20)
    
    # Création de l'index inversé pour la recherche
    index = creer_index(documents_tokens)
    
    while True:
        choix = input("\nQue voulez-vous faire ?\n"
                      "1 - Rechercher un mot clé dans les documents\n"
                      "2 - Quitter\n"
                      "Votre choix : ").strip()
        
        if choix == '1':
            mot_cle = input("Entrez le mot clé à rechercher : ").strip()
            if not mot_cle:
                print("[ERREUR] Mot clé vide.")
                continue
            
            docs_trouves = recherche_mot(index, mot_cle)
            afficher_resultats_recherche_docs(docs_trouves)
            
            # Recherche des lignes contenant le mot clé
            resultats_lignes = recherche_mot_dans_contenu(
                {nom: contenu.splitlines() for nom, contenu in documents_raw}, mot_cle
            )
            afficher_resultats_recherche_lignes(resultats_lignes)
        
        elif choix == '2':
            print("Fin du programme.")
            break
        
        else:
            print("[ERREUR] Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
