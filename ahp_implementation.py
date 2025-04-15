# === AHP Implementation in Python (Step-by-step) ===
import numpy as np

# Step 1: Define the pairwise comparison matrix (5x5) for the criteria
criteria = ["RAM", "Stockage", "CPU", "Prix", "Marque"]

# Matrix based on validated comparisons (decimal format)
A = np.array([
    [1,    3,    3,    5,    7],
    [1/3,  1,    1/3,  3,    5],
    [1/3,  3,    1,    5,    3],
    [1/5,  1/3,  1/5,  1,    3],
    [1/7,  1/5,  1/3,  1/3,  1]
])

# Step 2: Normalize the matrix and compute the weights
column_sums = np.sum(A, axis=0)
normalized_matrix = A / column_sums
weights = np.mean(normalized_matrix, axis=1)

# Step 3: Compute the consistency ratio (CR)
weighted_sum = np.dot(A, weights)
lambdas = weighted_sum / weights
lambda_max = np.mean(lambdas)
n = len(criteria)
CI = (lambda_max - n) / (n - 1)

# RI values for 1 to 10 criteria
RI_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
RI = RI_dict[n]
CR = CI / RI if RI != 0 else 0

# Step 4: Display results
print("\n--- AHP Criteria Weights ---")
for crit, w in zip(criteria, weights):
    print(f"{crit:<10} : {w:.4f}")

print(f"\nλ max        : {lambda_max:.4f}")
print(f"Consistency Index (CI): {CI:.4f}")
print(f"Consistency Ratio (CR): {CR:.4f}")

if CR < 0.1:
    print("\n✅ La matrice est cohérente.")
else:
    print("\n❌ La matrice est incohérente, il faut revoir les jugements.")

# Step 5: Synthesis - Evaluate alternatives
# Define the alternatives and their pairwise comparison matrix

phones = [
    {"nom": "iPhone 12", "RAM": 4, "Stockage": 128, "CPU": 3.1, "Prix": 450000, "Marque": 9},
    {"nom": "Infinix Hot 10", "RAM": 4, "Stockage": 64, "CPU": 2.0, "Prix": 100000, "Marque": 5},
    {"nom": "Xiaomi Redmi Note 10", "RAM": 6, "Stockage": 128, "CPU": 2.2, "Prix": 150000, "Marque": 6},
    {"nom": "Samsung Galaxy S22", "RAM": 8, "Stockage": 256, "CPU": 3.0, "Prix": 500000, "Marque": 9},
    {"nom": "Tecno Camon 12", "RAM": 4, "Stockage": 64, "CPU": 1.8, "Prix": 90000, "Marque": 4}
]

# Noramlisation des critères
max_ram = max(p["RAM"] for p in phones)
max_stock = max(p["Stockage"] for p in phones)
max_cpu = max(p["CPU"] for p in phones) 
min_prix = min(p["Prix"] for p in phones)
max_marque = max(p["Marque"] for p in phones)

print("\n--- Resultats de la synthèse ---")
best_score = -1
best_phone = ""

for phone in phones:
    # Normalisation des critères
    ram_score = phone["RAM"] / max_ram
    stock_score = phone["Stockage"] / max_stock
    cpu_score = phone["CPU"] / max_cpu
    prix_score = min_prix / phone["Prix"]  # Inversé pour le prix   
    marque_score = phone["Marque"] / max_marque

    # Calcul du score final
    score = (weights[0] * ram_score + 
             weights[1] * stock_score + 
             weights[2] * cpu_score + 
             weights[3] * prix_score + 
             weights[4] * marque_score)

    print(f"{phone['nom']:<25} : {score:.4f}")

    if score > best_score:
        best_score = score
        best_phone = phone["nom"]
print(f"\nLe meilleur téléphone est : {best_phone} avec un score de {best_score:.4f}")