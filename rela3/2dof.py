import numpy as np
import matplotlib.pyplot as plt

# Função para gerar matriz DH
def dh_matrix(theta, alpha, a, d):
    theta = np.radians(theta)
    alpha = np.radians(alpha)
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Valores de entrada
theta1 = 45   # graus
theta2 = 30   # graus
L1 = 5
L2 = 3

# Matrizes DH
T01 = dh_matrix(theta1, 90, 0, L1)
T12 = dh_matrix(theta2, 0, L2, 0)
T02 = T01 @ T12

# Pontos dos elos
p0 = np.array([0,0,0,1])   # base
p1 = T01 @ np.array([0,0,0,1])  # junta 1
p2 = T02 @ np.array([0,0,0,1])  # efetor final

# Print das coordenadas
print("Coordenadas:")
print(f"Base (p0): {p0[:3]}")
print(f"Junta 1 (p1): {p1[:3]}")
print(f"Efetor final (p2): {p2[:3]}")

# Plot em 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Desenho dos elos
ax.plot([p0[0], p1[0]], [p0[1], p1[1]], [p0[2], p1[2]], 'r-', linewidth=2, label="Elo 1")
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'b-', linewidth=2, label="Elo 2")

# Pontos
ax.scatter(p0[0], p0[1], p0[2], c='k', s=50)
ax.scatter(p1[0], p1[1], p1[2], c='g', s=50)
ax.scatter(p2[0], p2[1], p2[2], c='m', s=50)

# Ajustes do gráfico
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Manipulador 2 DOF em 3D")

plt.show()
