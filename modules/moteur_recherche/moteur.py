from typing import Dict, List, Tuple

def score_document(query_terms: List[str], index: Dict[str, Dict[str, int]], document_id: str) -> int:
    """
    Calcule le score de pertinence d'un document en fonction des termes de la requête,
    en utilisant la fréquence brute des termes (TF).

    Args:
        query_terms (list): Liste des mots de la requête.
        index (dict): Index inversé {mot: {doc_id: fréquence}}.
        document_id (str): Identifiant du document.

    Returns:
        int: Score de pertinence.
    """
    score = 0
    for term in query_terms:
        if term in index and document_id in index[term]:
            score += index[term][document_id]
    return score


def search(query: str, index: Dict[str, Dict[str, int]], top_n: int = 5) -> List[Tuple[str, int]]:
    """
    Recherche les documents les plus pertinents pour une requête donnée.

    Args:
        query (str): Chaîne de requête de l'utilisateur.
        index (dict): Index inversé {mot: {doc_id: fréquence}}.
        top_n (int): Nombre maximal de résultats retournés.

    Returns:
        list: Liste triée de tuples (doc_id, score).
    """
    # Nettoyage basique de la requête (minuscule, suppression ponctuation)
    import re
    query_clean = re.sub(r'[^\w\s]', '', query.lower())
    query_terms = query_clean.split()

    scores = {}
    for term in query_terms:
        if term in index:
            for doc_id, freq in index[term].items():
                scores[doc_id] = scores.get(doc_id, 0) + freq

    # Trier les documents par score décroissant
    ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_results[:top_n]


if __name__ == "__main__":
    # Test rapide
    index = {
        "chat": {"doc1": 3, "doc2": 1},
        "intelligent": {"doc2": 2},
        "robot": {"doc1": 1, "doc3": 2}
    }

    query = "chat robot"
    results = search(query, index)

    print("Résultats :")
    for doc_id, score in results:
        print(f"{doc_id} : pertinence {score}")
