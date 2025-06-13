import argparse
from modules.pretraitement.traitement import read_text_files_from_folder, manage_document_collection
from modules.analyse_frequence.analyse import analyse_frequence_globale, analyse_frequence_par_document
from modules.indexation.indexeur import creer_index, recherche_mot

def main():
    parser = argparse.ArgumentParser(description="TextAnaSearch - Analyseur de texte et moteur de recherche simple.")
    parser.add_argument("chemin", help="Chemin du dossier contenant les fichiers texte.")
    parser.add_argument("--frequence", action="store_true", help="Afficher la fréquence des mots.")
    parser.add_argument("--recherche", type=str, help="Mot-clé à rechercher dans les documents.")

    args = parser.parse_args()

    print("[INFO] Lecture et prétraitement des documents...")
    documents_raw = read_text_files_from_folder(args.chemin)
    
    # Manage collection renvoie deux dicts : tokens et lignes
    documents_tokens, documents_lines = manage_document_collection(documents_raw)

    if args.frequence:
        print("\n[INFO] Analyse de fréquence des mots :")
        freqs = analyse_frequence_globale(documents_tokens)
        for mot, freq in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
            print(f"{mot}: {freq}")

    if args.recherche:
        print(f"\n[INFO] Recherche du mot '{args.recherche}' :")
        # Préparer un index avec fréquence par document (dictionnaire imbriqué)
        freqs_par_doc = analyse_frequence_par_document(documents_tokens)
        index = creer_index(freqs_par_doc)
        resultats = recherche_mot(index, args.recherche)
        if resultats:
            print("Mot trouvé dans :")
            for doc in resultats:
                print(f" - {doc}")
        else:
            print("Aucune occurrence trouvée.")

if __name__ == "__main__":
    main()
