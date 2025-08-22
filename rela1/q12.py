import numpy as np
import matplotlib.pyplot as plt

# --- Entrada ---
theta_deg = float(input("Digite o ângulo de rotação em graus: "))
theta = np.radians(theta_deg)  # converte para radianos

# Ponto original (coordenadas homogêneas)
P = np.array([4, 5, 6, 1])

# Matriz de rotação em torno do eixo Z
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta),  np.cos(theta), 0, 0],
    [0,              0,             1, 0],
    [0,              0,             0, 1]
])

# Aplica rotação
P_rot = Rz @ P

# --- Resultados ---
print(f"Ponto original: {P[:3]}")
print(f"Ponto após rotação de {theta_deg}° em torno de Z: {P_rot[:3]}")

# --- Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Pontos
ax.scatter(P[0], P[1], P[2], color="blue", label="Ponto Original", s=80)
ax.scatter(P_rot[0], P_rot[1], P_rot[2], color="red", label="Após Rotação", s=80)

# Conectar os dois pontos
ax.plot([P[0], P_rot[0]], [P[1], P_rot[1]], [P[2], P_rot[2]], "k--")

# Ajustes do gráfico
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Rotação de {theta_deg}° em torno do eixo Z")
ax.legend()

plt.show()
