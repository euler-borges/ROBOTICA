import numpy as np
import matplotlib.pyplot as plt

# -------- Matriz DH --------
def dh_matrix(theta, d, a, alpha):
    ct, st = np.cos(theta), np.sin(theta)
    ca, sa = np.cos(alpha), np.sin(alpha)
    return np.array([
        [ct, -st*ca, st*sa, a*ct],
        [st, ct*ca, -ct*sa, a*st],
        [0, sa, ca, d],
        [0, 0, 0, 1]
    ])

# -------- Cinemática direta --------
def forward_kinematics(params):
    """
    params: lista de (theta, d, a, alpha)
    Retorna: lista de pontos homogêneos [p0, p1, ..., pN]
    """
    T = np.eye(4)
    points = [np.array([0, 0, 0, 1])]  # base
    for i, (theta, d, a, alpha) in enumerate(params, start=1):
        T = T @ dh_matrix(np.radians(theta), d, a, np.radians(alpha))
        p = T @ np.array([0, 0, 0, 1])
        points.append(p)
        print(f"P{i} -> x={p[0]:.3f}, y={p[1]:.3f}, z={p[2]:.3f}")
    return points

# -------- Plot 3D --------
def plot_robot(params):
    points = forward_kinematics(params)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs, "-o", linewidth=2, markersize=6, color="blue")

    # labels
    ax.text(xs[0], ys[0], zs[0], "Base", fontsize=10)
    ax.text(xs[-1], ys[-1], zs[-1], "TCP", fontsize=10)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Robô com DH (3D)")

    # escala proporcional
    max_range = max(np.ptp(xs), np.ptp(ys), np.ptp(zs))
    mid_x = (max(xs) + min(xs)) / 2
    mid_y = (max(ys) + min(ys)) / 2
    mid_z = (max(zs) + min(zs)) / 2
    ax.set_xlim(mid_x - max_range/2, mid_x + max_range/2)
    ax.set_ylim(mid_y - max_range/2, mid_y + max_range/2)
    ax.set_zlim(mid_z - max_range/2, mid_z + max_range/2)

    plt.show()

# ------------------ EXEMPLO ------------------
params = [
    (45, 1, 2.0, 0),    # θ=45°, d=1, a=2.0, α=0
    (30, 0.5, 1.5, 45)  # θ=30°, d=0.5, a=1.5, α=45°
]

plot_robot(params)
