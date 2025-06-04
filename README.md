# Python-Project-Text-AnaSearch
Créer un système en ligne de commande permettant de déﬁnir des "tables" (similaires à des tables de base de données mais stockées en mémoire et sauvegardées dans des ﬁchiers JSON ou CSV), d'y insérer des enregistrements, de les modiﬁer, supprimer, et d'e ectuer des requêtes simples (ﬁltrage, tri).


# 🧠 TextAnaSearch

**TextAnaSearch** est un outil Python en ligne de commande permettant d’analyser un ou plusieurs fichiers texte. Il offre des fonctionnalités d’analyse de fréquence, de recherche de mots ou d'expressions, et de classement de documents selon leur pertinence.

## 🎯 Objectif du projet

Développer une application modulaire qui permet de :
- Charger et nettoyer des fichiers texte
- Compter la fréquence des mots
- Rechercher des mots dans les documents
- Classer les documents en fonction d’une requête utilisateur

---

## 📁 Structure du projet

Le projet est divisé en 5 modules (un par membre du groupe) :

| Module | Nom du fichier            | Description |
|--------|----------------------------|---------------------------------------------------------------------------
| 1      | `text_processor.py`        | Chargement et nettoyage du texte (minuscules, ponctuation, tokenisation) |
| 2      | `frequency_analyzer.py`    | Calcul des fréquences de mots, tri, top-N mots |
| 3      | `simple_indexer.py`        | Création d’un index mot → documents/lignes |
| 4      | `document_retriever.py`    | Moteur de recherche de documents + classement par pertinence |
| 5      | `cli_manager.py`           | Interface utilisateur en ligne de commande |

---

