import os # Importe le module 'os' pour interagir avec le système d'exploitation, comme lister le contenu des répertoires.
import re # Importe le module 're' pour les expressions régulières, utile pour le nettoyage de texte.

def read_text_file(filepath):
    """
    Lit le contenu d'un seul fichier texte.

    Args:
        filepath (str): Le chemin d'accès au fichier texte.

    Returns:
        str: Le contenu du fichier sous forme de chaîne de caractères unique, ou None si une erreur survient.
    """
    try:
        # Ouvre le fichier en mode lecture avec l'encodage UTF-8.
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()  # Lit tout le contenu du fichier.
        return content  # Retourne le contenu lu.
    except FileNotFoundError:
        # Gère le cas où le fichier n'existe pas.
        print(f"Erreur : Fichier non trouvé à {filepath}")
        return None
    except Exception as e:
        # Gère toute autre erreur potentielle lors de la lecture du fichier.
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
        return None

def read_text_files_from_folder(folder_path):
    """
    Lit le contenu de tous les fichiers texte dans un dossier spécifié.

    Args:
        folder_path (str): Le chemin d'accès au dossier contenant les fichiers texte.

    Returns:
        list: Une liste de tuples, où chaque tuple contient (nom_fichier, contenu_fichier).
              Retourne une liste vide si le dossier n'est pas trouvé ou s'il n'y a pas de fichiers texte.
    """
    documents = [] # Initialise une liste vide pour stocker le contenu des documents.
    if not os.path.isdir(folder_path):
        # Vérifie si le chemin fourni est un répertoire valide.
        print(f"Erreur : Dossier non trouvé à {folder_path}")
        return []

    # Itère sur tous les fichiers du dossier spécifié.
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename) # Construit le chemin complet du fichier.
        # Vérifie si l'élément actuel est un fichier et se termine par .txt.
        if os.path.isfile(filepath) and filename.lower().endswith('.txt'):
            content = read_text_file(filepath) # Lit le contenu du fichier texte.
            if content:
                documents.append((filename, content)) # Ajoute le nom du fichier et son contenu à la liste.
    return documents # Retourne la liste des documents.

def clean_and_tokenize_text(text):
    """
    Nettoie le texte d'entrée en le convertissant en minuscules, en supprimant la ponctuation,
    et en le tokenisant en une liste de mots.

    Args:
        text (str): La chaîne de caractères du texte d'entrée.

    Returns:
        list: Une liste de mots nettoyés et tokenisés.
    """
    if not isinstance(text, str):
        # S'assure que l'entrée est une chaîne de caractères.
        return []

    # Convertit le texte en minuscules.
    text = text.lower()

    # Supprime la ponctuation spécifique et remplace par un espace.
    # Utilise re.sub avec une expression régulière pour remplacer les caractères non alphanumériques (sauf les espaces)
    # par un seul espace. Cela gère une plus large gamme de ponctuation.
    text = re.sub(r'[^\w\s]', ' ', text)

    # Divise le texte en mots (tokenisation) en se basant sur les espaces.
    words = text.split()

    # Nettoie davantage en supprimant les chaînes vides qui pourraient résulter de plusieurs espaces.
    words = [word for word in words if word]
    return words # Retourne la liste des mots.

def manage_document_collection(documents_raw):
    """
    Gère une collection de documents en nettoyant et en tokenisant leur contenu.

    Args:
        documents_raw (list): Une liste de tuples, où chaque tuple est (nom_fichier, contenu_brut).

    Returns:
        dict: Un dictionnaire où les clés sont les noms de fichiers et les valeurs sont des listes de mots tokenisés.
    """
    processed_documents = {} # Initialise un dictionnaire pour stocker les documents traités.
    # Itère sur chaque document brut (nom du fichier et son contenu).
    for filename, content in documents_raw:
        # Nettoie et tokenise le contenu de chaque document.
        tokenized_words = clean_and_tokenize_text(content)
        # Stocke les mots tokenisés avec le nom du fichier comme clé.
        processed_documents[filename] = tokenized_words
    return processed_documents # Retourne le dictionnaire des documents traités.

if __name__ == "__main__":
    # Ce bloc démontre comment utiliser les fonctions de ce module.
    # Exemple d'utilisation :
    # 1. Crée un dossier factice et quelques fichiers texte pour les tests.
    if not os.path.exists("test_documents"):
        os.makedirs("test_documents") # Crée un répertoire nommé 'test_documents'.

    # Écrit du contenu dans les fichiers de test.
    with open("test_documents/doc1.txt", "w", encoding="utf-8") as f:
        f.write("Ceci est le premier document. Il parle de Python et d'algorithmes.\nAvec de la ponctuation!")
    with open("test_documents/doc2.txt", "w", encoding="utf-8") as f:
        f.write("Le deuxième document. Il contient des mots comme algorithmes et données.")
    with open("test_documents/empty.txt", "w", encoding="utf-8") as f:
        f.write("") # Crée un fichier vide.
    with open("test_documents/doc3.pdf", "w", encoding="utf-8") as f: # Fichier non-texte à ignorer.
        f.write("Ceci est une simulation de PDF.")


    print("--- Lecture d'un seul fichier ---")
    single_file_content = read_text_file("test_documents/doc1.txt") # Lit un fichier spécifique.
    if single_file_content:
        print(f"Contenu de doc1.txt :\n{single_file_content}\n")

    print("--- Lecture des fichiers d'un dossier ---")
    # Lit tous les fichiers texte du dossier 'test_documents'.
    raw_docs = read_text_files_from_folder("test_documents")
    print("Documents bruts trouvés :")
    for name, content in raw_docs:
        print(f"  - {name} : {content[:50]}...") # Affiche un extrait de chaque document.
    print("\n")

    print("--- Nettoyage et Tokenisation de Texte ---")
    sample_text = "Bonjour le monde ! Ceci est un test. Comment allez-vous aujourd'hui ?"
    # Nettoie et tokenise un texte d'exemple.
    tokenized_sample = clean_and_tokenize_text(sample_text)
    print(f"Texte original : '{sample_text}'")
    print(f"Mots tokenisés : {tokenized_sample}\n")

    print("--- Gestion de la Collection de Documents (Traitement de tous les documents lus) ---")
    # Traite les documents bruts obtenus du dossier.
    processed_documents = manage_document_collection(raw_docs)
    for filename, tokens in processed_documents.items():
        print(f"'{filename}' traité : {tokens}") # Affiche les tokens traités pour chaque document.

    # Nettoyage des fichiers et du dossier factices
    import shutil # Importe shutil pour les opérations de fichiers de haut niveau.
    shutil.rmtree("test_documents") # Supprime le répertoire de test créé et son contenu.
    print("\n--- Dossier 'test_documents' nettoyé ---")