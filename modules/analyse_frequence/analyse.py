from collections import Counter

def analyse_frequence_globale(documents_tokens):
    """
    Analyse la fréquence globale des mots dans tous les documents.
    :param documents_tokens: dict {filename: [tokens]}
    :return: dict {mot: fréquence totale}
    """
    frequence_globale = Counter()
    for tokens in documents_tokens.values():
        frequence_globale.update(tokens)
    return dict(frequence_globale)

def analyse_frequence_par_document(documents_tokens):
    """
    Calcule la fréquence des mots pour chaque document.
    :param documents_tokens: dict {filename: [tokens]}
    :return: dict {filename: {mot: fréquence dans ce document}}
    """
    frequence_par_doc = {}
    for filename, tokens in documents_tokens.items():
        frequence_par_doc[filename] = dict(Counter(tokens))
    return frequence_par_doc
