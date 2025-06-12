from collections import defaultdict
def build_inverted_index(documents):
    """
    Construit un index inversé à partir d'une liste de tuples (doc_id, texte).
    
    Chaque document est supposé être prétraité et normalisé (par exemple, tout en minuscules,
    sans ponctuation et tokenisé par espace). Pour chaque document, on retire les doublons de tokens,
    de façon à ajouter chaque document une seule fois par mot.
    
    Retourne un dictionnaire où chaque clé est un terme et chaque valeur est une liste triée
    d'identifiants de documents dans lesquels ce terme apparaît.
    """
    # Utilisation d'un defaultdict avec pour valeur un ensemble (set) afin de garantir qu'un document
    # n'est ajouté qu'une seule fois par terme, optimisant ainsi l'utilisation d'espace.
    index = defaultdict(set)
    
    for doc_id, text in documents:
        # Tokenisation basique en se basant sur les espaces
        tokens = text.split()
        # On élimine les doublons dans le même document
        unique_tokens = set(tokens)
        
        for token in unique_tokens:
            index[token].add(doc_id)
    
    # Conversion de chaque ensemble en liste triée pour faciliter l'accès et la lisibilité
    inverted_index = {token: sorted(doc_ids) for token, doc_ids in index.items()}
    return inverted_index
def search_word(word, index):
    """
    Recherche un terme dans l'index inversé et renvoie la liste des identifiants de documents qui contiennent ce mot.
    Si le terme n'est pas présent, retourne une liste vide.
    """
    return index.get(word, [])
if __name__ == '__main__':
    # Exemples de documents prétraités et normalisés.
    documents = [
        (1, "le chat court vite"),
        (2, "le chien court lentement"),
        (3, "le chat et le chien dorment")
    ]
    
    # Construction de l'index inversé
    index = build_inverted_index(documents)
    
    # Affichage de l'index
    print("Index inversé:")
    for word, doc_ids in sorted(index.items()):
        print(f"{word} -> {doc_ids}")
    
    # Exemple de recherche dans l'index
    search_term = "chat"
    result = search_word(search_term, index)
    print(f"\nDocuments contenant le mot '{search_term}': {result}")
