
import os
import text_processor
import frequency_analyzer
import simple_indexer
import document_retriever

def menu():
    documents = {}
    documents_bruts = {}
    index = {}
    frequences = {}

    while true:

        print("\n--- MENU PRINCIPAL ---")
        print("1. Charger fichiers texte")
        print("2. Afficher les mots les plus fréquents")
        print("3. Rechercher un mot")
        print("4. Rechercher des documents par mots_clés")
        print("5. Quitter")

        choix = input("Entrez votre choix")
        if choix == "1":
            dossier = input("chemin du dossier contenant les fichiers :")
            documents, documents.brut =text_processor.charger_documents(dossier)
            index = simple_indexer .creer_index(documents)
            frequency_analyzer .calculer_frequences(documents)
        elif choix == "2":
            n = int(input("combien de mots frequents affiches ? "))
            top_mots = frequency_analyzer .top_mor_frequents(frequences, n)
            for mot, freq in top_mots:
                        print(f"{mot} : {freq}")
        elif choix == "3":
            mot = input("mot a rechercher : ")
            resultats = simple_indexer .rechercher_mot_dans_contenu(documents_bruts, mot)
            for doc, lignes in resultats.items():
                        print(f"\n{doc}:")
                        for ligne in lignes:
                            print(f" - {ligne}")
        elif choix == "4":
            requete = input("Entrez les mots-cles separes par des espaces : ").split()
            scores = document_retriever_scorer_documents(frequences, requete)
            classes = document_retriever_classer_documents-par_score(scores)
            for doc, score in classes:
                        print(f"{doc} (score: {score})")
        elif choix == "5":
            print("fermeture du programme.")
            break
        else:
            print("choix invalide. veuillez reésayer.")                            
