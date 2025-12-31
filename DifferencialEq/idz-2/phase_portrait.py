import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Определяем систему
def system(t, z):
    x, y = z
    dxdt = 0.5 * x
    dydt = x + y
    return [dxdt, dydt]

# Поле направлений
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

DX, DY = system(None, [X, Y])
M = np.hypot(DX, DY)
M[M == 0] = 1
DX /= M
DY /= M

plt.figure(figsize=(8, 8))
plt.quiver(X, Y, DX, DY, M, pivot='mid', cmap='viridis', alpha=0.7, width=0.005)

# Интегрируем траектории
initial_points = []
for x0 in np.linspace(-2, 2, 7):
    for y0 in np.linspace(-2, 2, 7):
        initial_points.append([x0, y0])

# Интегрируем в обе стороны для каждой начальной точки
for point in initial_points:
    # Вперёд во времени
    sol_f = solve_ivp(system, [0, 3], point, 
                     t_eval=np.linspace(0, 3, 300),
                     method='RK45')
    # Назад во времени
    sol_b = solve_ivp(system, [0, -3], point,
                     t_eval=np.linspace(0, -3, 300),
                     method='RK45')
    
    # Объединяем траектории
    x_traj = np.concatenate([sol_b.y[0][::-1], sol_f.y[0]])
    y_traj = np.concatenate([sol_b.y[1][::-1], sol_f.y[1]])
    
    plt.plot(x_traj, y_traj, 'r-', lw=1.2, alpha=0.8)

# Точка покоя
plt.scatter([0], [0], color='black', s=150, zorder=5, 
            label='Точка покоя (0,0)')

# Настройки графика
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.axhline(0, color='k', lw=0.5)
plt.axvline(0, color='k', lw=0.5)
plt.grid(True, linestyle='--', alpha=0.3)
plt.title('Фазовый портрет: $dx/dt = 0.5x$, $dy/dt = x + y$\nНеустойчивый узел', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('phase_portrait.png', dpi=150, bbox_inches='tight')