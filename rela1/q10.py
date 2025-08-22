import numpy as np
import matplotlib.pyplot as plt

def translate_matrix(tx, ty, tz):
    """Matriz de translação homogênea 4x4"""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ], dtype=float)

# --- Entrada do usuário ---
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

# Ponto original em coordenadas homogêneas
P = np.array([x, y, z, 1], dtype=float)

# Matriz de translação T
T = translate_matrix(2, 3, 5)

# Ponto transladado
P2 = T @ P

print("\nMatriz de Translação T:")
print(T)
print(f"\nP  = ({P[0]}, {P[1]}, {P[2]})")
print(f"P' = ({P2[0]}, {P2[1]}, {P2[2]})")

# --- Plot 3D ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Eixos
ax.quiver(0,0,0, 5,0,0, color="r", arrow_length_ratio=0.1)  # X
ax.quiver(0,0,0, 0,5,0, color="g", arrow_length_ratio=0.1)  # Y
ax.quiver(0,0,0, 0,0,5, color="b", arrow_length_ratio=0.1)  # Z

# Pontos
ax.scatter(P[0], P[1], P[2], color="blue", s=60, label="P original")
ax.scatter(P2[0], P2[1], P2[2], color="red", s=60, label="P transladado")

# Conexão entre eles
ax.plot([P[0], P2[0]], [P[1], P2[1]], [P[2], P2[2]], "k--")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Translação 3D (Questão 1)")

plt.show()
