import tkinter as tk
from tkinter import messagebox
import numpy as np

# --- Définition des critères ---
criteria = ["RAM", "Stockage", "CPU", "Prix", "Marque"]
n = len(criteria)

# --- Matrice de comparaison par paire ---
A = np.array([
    [1,    3,    3,    5,    7],
    [1/3,  1,    1/3,  3,    5],
    [1/3,  3,  1,    5,    3],
    [1/5,  1/3,  1/5,  1,    3],
    [1/7,  1/5,  1/3,  1/3,  1]
])

# --- Téléphones à comparer ---
phones = [
    {"nom": "iPhone 12", "RAM": 4, "Stockage": 128, "CPU": 3.1, "Prix": 450000, "Marque": 9},
    {"nom": "Infinix Hot 10", "RAM": 4, "Stockage": 64, "CPU": 2.0, "Prix": 100000, "Marque": 5},
    {"nom": "Xiaomi Redmi Note 10", "RAM": 6, "Stockage": 128, "CPU": 2.2, "Prix": 150000, "Marque": 6},
    {"nom": "Samsung Galaxy S22", "RAM": 8, "Stockage": 256, "CPU": 3.0, "Prix": 500000, "Marque": 9},
    {"nom": "Tecno Camon 12", "RAM": 4, "Stockage": 64, "CPU": 1.8, "Prix": 90000, "Marque": 4}
]

# --- Calcul des poids + CR ---
def compute_weights():
    col_sums = np.sum(A, axis=0)
    normalized = A / col_sums
    weights = np.mean(normalized, axis=1)

    weighted_sum = np.dot(A, weights)
    lambdas = weighted_sum / weights
    lambda_max = np.mean(lambdas)
    CI = (lambda_max - n) / (n - 1)

    RI_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12}
    RI = RI_dict[n]
    CR = CI / RI if RI != 0 else 0

    return weights, lambda_max, CI, CR

# --- Normalisation et évaluation des téléphones ---
def evaluate_phones():
    weights, lambda_max, CI, CR = compute_weights()

    max_ram = max(p["RAM"] for p in phones)
    max_stock = max(p["Stockage"] for p in phones)
    max_cpu = max(p["CPU"] for p in phones)
    min_prix = min(p["Prix"] for p in phones)
    max_marque = max(p["Marque"] for p in phones)

    best_score = -1
    best_phone = ""
    results = []

    for phone in phones:
        ram_score = phone["RAM"] / max_ram
        stock_score = phone["Stockage"] / max_stock
        cpu_score = phone["CPU"] / max_cpu
        prix_score = min_prix / phone["Prix"]
        marque_score = phone["Marque"] / max_marque

        total = (
            ram_score * weights[0] +
            stock_score * weights[1] +
            cpu_score * weights[2] +
            prix_score * weights[3] +
            marque_score * weights[4]
        )
        results.append((phone["nom"], total))

        if total > best_score:
            best_score = total
            best_phone = phone["nom"]

    # Affichage
    result_text = "--- Poids des critères ---\n"
    for crit, w in zip(criteria, weights):
        result_text += f"{crit:<10} : {w:.4f}\n"
    result_text += f"\nλ max = {lambda_max:.4f}\nCI = {CI:.4f}\nCR = {CR:.4f}\n"
    result_text += "\n--- Résultats des téléphones ---\n"
    for nom, score in results:
        result_text += f"{nom:<25} → Score: {score:.4f}\n"
    result_text += f"\n✅ Téléphone idéal : {best_phone} (Score: {best_score:.4f})"

    messagebox.showinfo("Analyse AHP", result_text)

# --- Interface graphique ---
root = tk.Tk()
root.title("Sélection Téléphone - AHP")
root.geometry("600x350")

label = tk.Label(root, text="Appuyez sur le bouton pour exécuter l'analyse AHP complète.\n(Comparaison, Poids, Cohérence, Synthèse)", font=("Arial", 11), pady=20)
label.pack()

btn = tk.Button(root, text="Lancer l'analyse AHP", command=evaluate_phones, font=("Arial", 12), bg="green", fg="white")
btn.pack(pady=20)

root.mainloop()
