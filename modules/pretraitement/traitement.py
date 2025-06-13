import os
import re
from typing import List, Tuple, Dict

def read_text_file(filepath: str) -> str | None:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERREUR] Fichier non trouvé : {filepath}")
    except Exception as e:
        print(f"[ERREUR] Lecture échouée ({filepath}) : {e}")
    return None

def read_text_files_from_folder(folder_path: str) -> List[Tuple[str, str]]:
    documents = []
    if not os.path.isdir(folder_path):
        print(f"[ERREUR] Dossier inexistant : {folder_path}")
        return []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.txt'):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath):
                content = read_text_file(filepath)
                if content:
                    documents.append((filename, content))
    return documents

def clean_and_tokenize_text(text: str) -> List[str]:
    if not isinstance(text, str):
        return []
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    return [word for word in words if word]

def clean_and_tokenize_lines(text: str) -> List[str]:
    """
    Nettoie chaque ligne du texte en minuscules et sans ponctuation (pour la recherche ligne par ligne).
    """
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.lower()
        line = re.sub(r'[^\w\s]', ' ', line)
        cleaned_lines.append(line.strip())
    return cleaned_lines

def manage_document_collection(documents_raw: List[Tuple[str, str]]) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """
    Applique nettoyage et tokenisation à une collection de documents bruts.
    Retourne deux dictionnaires :
    - {filename: list of tokens}
    - {filename: list of cleaned lines}
    """
    processed_tokens = {}
    processed_lines = {}
    for filename, content in documents_raw:
        processed_tokens[filename] = clean_and_tokenize_text(content)
        processed_lines[filename] = clean_and_tokenize_lines(content)
    return processed_tokens, processed_lines
