import numpy as np
import matplotlib.pyplot as plt

# --- Função para criar matriz de rotação ---
def rotation_matrix(angle_deg, axis):
    angle = np.radians(angle_deg)
    if axis.upper() == "X":
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle), -np.sin(angle), 0],
            [0, np.sin(angle),  np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif axis.upper() == "Y":
        return np.array([
            [np.cos(angle), 0, np.sin(angle), 0],
            [0, 1, 0, 0],
            [-np.sin(angle), 0, np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    elif axis.upper() == "Z":
        return np.array([
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle),  np.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    else:
        raise ValueError("Eixo inválido! Use X, Y ou Z.")

# --- Entrada ---
theta_deg = float(input("Digite o ângulo da primeira rotação R1 (em graus): "))
axis1 = input("Digite o eixo da primeira rotação (X, Y ou Z): ")

alpha_deg = float(input("Digite o ângulo da segunda rotação R2 (em graus): "))
axis2 = input("Digite o eixo da segunda rotação (X, Y ou Z): ")

# Ponto original (coordenadas homogêneas)
P = np.array([6, 6, 8, 1])

# --- Matrizes de rotação ---
R1 = rotation_matrix(theta_deg, axis1)
R2 = rotation_matrix(alpha_deg, axis2)

# --- Transformações sucessivas ---
P_R1 = R1 @ P        # após primeira rotação
P_R2 = R2 @ P_R1     # após segunda rotação

# --- Resultados ---
print(f"\nPonto original: {P[:3]}")
print(f"Após R1 ({axis1}, {theta_deg}°): {P_R1[:3]}")
print(f"Após R1 + R2 ({axis2}, {alpha_deg}°): {P_R2[:3]}")

# --- Plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Pontos
ax.scatter(P[0], P[1], P[2], color="blue", label="Ponto Original", s=80)
ax.scatter(P_R1[0], P_R1[1], P_R1[2], color="orange", label="Após R1", s=80)
ax.scatter(P_R2[0], P_R2[1], P_R2[2], color="red", label="Após R1+R2", s=80)

# Linhas conectando os pontos
ax.plot([P[0], P_R1[0]], [P[1], P_R1[1]], [P[2], P_R1[2]], "k--")
ax.plot([P_R1[0], P_R2[0]], [P_R1[1], P_R2[1]], [P_R1[2], P_R2[2]], "k--")

# Ajustes do gráfico
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"R1({axis1} {theta_deg}°) → R2({axis2} {alpha_deg}°)")
ax.legend()

plt.show()
