import numpy as np
import matplotlib.pyplot as plt

# Ponto inicial
P = np.array([3, 4, 7, 1])  # coordenadas homogêneas

# Matrizes de transformação
T0 = np.array([
    [1, 0, 0, 2],
    [0, 1, 0, 3],
    [0, 0, 1, 5],
    [0, 0, 0, 1]
])

T1 = np.array([
    [1, 0, 0, -1],
    [0, 1, 0, 4],
    [0, 0, 1, 2],
    [0, 0, 0, 1]
])

# Transformações sucessivas
P_T0_T1 = (T0 @ T1) @ P   # aplica T1 depois T0
P_T1_T0 = (T1 @ T0) @ P   # aplica T0 depois T1

# Intermediários (para plotar os passos)
P_T1 = T1 @ P
P_T0 = T0 @ P

# Impressão dos resultados
print("Ponto original:", P[:3])
print("Após T1:", P_T1[:3])
print("Após T0:", P_T0[:3])
print("Transformação T0.T1:", P_T0_T1[:3])
print("Transformação T1.T0:", P_T1_T0[:3])

# ---------------- PLOT ----------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Lista de pontos para visualização
points = {
    "P": P,
    "T1(P)": P_T1,
    "T0(P)": P_T0,
    "T0.T1(P)": P_T0_T1,
    "T1.T0(P)": P_T1_T0
}

# Cores diferentes para cada transformação
colors = {
    "P": "black",
    "T1(P)": "blue",
    "T0(P)": "green",
    "T0.T1(P)": "red",
    "T1.T0(P)": "orange"
}

# Plota cada ponto
for label, coord in points.items():
    ax.scatter(coord[0], coord[1], coord[2], color=colors[label], s=80)
    ax.text(coord[0]+0.2, coord[1]+0.2, coord[2]+0.2, label)

# Configuração do gráfico
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Transformações Sucessivas T0.T1 e T1.T0")

plt.show()
