# 📱 AHP - Sélection du Meilleur Téléphone

Ce projet implémente la méthode AHP (Analytical Hierarchy Process) pour aider à choisir le meilleur téléphone parmi plusieurs alternatives, selon plusieurs critères pondérés.

---

## 🧠 Objectif du projet
Choisir le téléphone idéal en fonction des critères suivants :
- RAM
- Stockage
- Fréquence CPU
- Prix
- Marque

---

## 🚀 Fonctionnalités
- Comparaison par paire des critères selon vos préférences
- Calcul automatique des poids avec vérification de cohérence (Consistency Ratio)
- Évaluation de plusieurs téléphones selon leurs caractéristiques techniques
- Deux modes disponibles : en console et en interface graphique (Tkinter)

---

## 📦 Contenu du projet

```
📁 ahp-phone-selection/
├── ahp.py                ← Version console complète
├── tkinter_ahp_gui.py    ← Version GUI avec Tkinter
├── README.md             ← Fichier explicatif (ce document)
```

---

## ▶️ Exécution

### 📍 Version console
#### Prérequis :
- Python 3
- numpy (`pip install numpy`)

#### Commande d'exécution :
```bash
python3 ahp.py
```
Cette version :
- Calcule les poids des critères à partir d'une matrice AHP codée en dur
- Vérifie la cohérence (CR)
- Évalue les téléphones selon les critères
- Affiche le téléphone idéal dans le terminal

### 📍 Version interface graphique (GUI avec Tkinter)
#### Prérequis :
- Python 3
- tkinter (inclus avec Python par défaut)
- numpy (`pip install numpy`)

#### Commande d'exécution :
```bash
python3 tkinter_ahp_gui.py
```
Cette version :
- Ouvre une fenêtre graphique avec un bouton
- Effectue le calcul complet AHP et la synthèse en un clic
- Affiche les scores et le téléphone recommandé dans une boîte de dialogue

### Modifier les alternatives ou critères ?
Vous pouvez modifier :
- Les critères de comparaison dans la matrice `A` (5x5)
- Les alternatives (liste de téléphones dans `phones`)

Dans les deux fichiers (`ahp.py` et `tkinter_ahp_gui.py`), cherchez les sections suivantes :
```python
# Matrice A = [...]
# phones = [...]
```
et remplacez les valeurs selon vos besoins.
---

## 🧑‍💻 Auteur
Projet académique - INF4178 | Avril 2025
