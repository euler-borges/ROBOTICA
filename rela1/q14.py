import numpy as np
import matplotlib.pyplot as plt

# --- Função matriz de rotação (em torno de Z) ---
def rotation_matrix(angle_deg):
    angle = np.radians(angle_deg)
    return np.array([
        [np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle),  np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# --- Função matriz de translação ---
def translation_matrix(tx, ty):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# --- Entrada do usuário ---
tx = float(input("Digite a translação em X: "))
ty = float(input("Digite a translação em Y: "))
theta_deg = float(input("Digite o ângulo de rotação (em graus): "))

# Ponto original
P = np.array([4, 5, 7, 1])

# Matrizes de transformação
T = translation_matrix(tx, ty)
R = rotation_matrix(theta_deg)

# --- Transformações sucessivas ---
# T·R → rotação depois translação
P_R = R @ P      # intermediário
P_TR = T @ P_R   # final

# R·T → translação depois rotação
P_T = T @ P      # intermediário
P_RT = R @ P_T   # final

# --- Resultados ---
print(f"\nPonto original: {P[:3]}")
print(f"Intermediário (após R): {P_R[:3]} → Final T·R: {P_TR[:3]}")
print(f"Intermediário (após T): {P_T[:3]} → Final R·T: {P_RT[:3]}")

# --- Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Ponto original
ax.scatter(P[0], P[1], P[2], color="blue", label="Ponto Original", s=80)

# Intermediários
ax.scatter(P_R[0], P_R[1], P_R[2], color="orange", label="Intermediário R", s=60)
ax.scatter(P_T[0], P_T[1], P_T[2], color="purple", label="Intermediário T", s=60)

# Finais
ax.scatter(P_TR[0], P_TR[1], P_TR[2], color="red", label="Final T·R", s=80)
ax.scatter(P_RT[0], P_RT[1], P_RT[2], color="green", label="Final R·T", s=80)

# Conectar pontos com linhas (sequência T·R)
ax.plot([P[0], P_R[0], P_TR[0]], [P[1], P_R[1], P_TR[1]], [P[2], P_R[2], P_TR[2]], "r--")

# Conectar pontos com linhas (sequência R·T)
ax.plot([P[0], P_T[0], P_RT[0]], [P[1], P_T[1], P_RT[1]], [P[2], P_T[2], P_RT[2]], "g--")

# Configurações do gráfico
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Transformações T·R vs R·T (com intermediários)")
ax.legend()

plt.show()
