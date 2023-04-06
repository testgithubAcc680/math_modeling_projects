import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 0.5
t = np.linspace(0, years*seconds_in_year, frames)

# 1 - Earth
# 2 - Aster
# 3 - ...

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2, 
     x3, v_x3, y3, v_y3 ,
     x4, v_x4, y4, v_y4) = s

    # Динамика первого тела под влиянием второго и третьего
    dxdt1 = v_x1
    dv_xdt1 = (
      	    - G * M * (x1) 
               / ((x1)**2 + (y1)**2)**1.5)
    dydt1 = v_y1
    dv_ydt1 = (
      	    - G * M * (y1) 
               / ((x1)**2 + (y1)**2)**1.5)

    # Динамика астероида
    dxdt2 = v_x2
    dv_xdt2 = (
      	    - G * m1 * (x2 - x1) 
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            - G * M * (x2) 
               / ((x2)**2 + (y2)**2)**1.5)
    dydt2 = v_y2
    dv_ydt2 = (
      	    - G * m1 * (y2 - y1) 
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            - G * M * (y2) 
               / ((x2)**2 + (y2)**2)**1.5)



#динамика 3

    dxdt3 = v_x3
    dv_xdt3 = (
      	    - G * m1 * (x3 - x1) 
               / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            - G * M * (x3) 
               / ((x3)**2 + (y3)**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (
      	    - G * m1 * (y3 - y1) 
               / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            - G * M * (y3) 
               / ((x3)**2 + (y3)**2)**1.5)


# динамика 4
    dxdt4 = v_x4
    dv_xdt4 = (
      	    - G * m1 * (x4 - x1) 
               / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
            - G * M * (x4) 
               / ((x4)**2 + (y4)**2)**1.5)
    dydt4 = v_y4
    dv_ydt4 = (
      	    - G * m1 * (y4 - y1) 
               / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
            - G * M * (y4) 
               / ((x4)**2 + (y4)**2)**1.5)
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3, 
            dxdt4, dv_xdt4, dydt4, dv_ydt4)


# Определяем начальные значения и параметры, 
# входящие в систему диф. уравнений
x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000

x20 = 151 * 10**9 
v_x20 = 10000
y20 = 0
v_y20 = 20000

x30 =  150 * 10**9 
v_x30 = 0
y30 = 1000
v_y30 = 20000

x40 =  150 * 10**9 
v_x40 = 0
y40 = 0
v_y40 =  - 14500

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20, 
      x30, v_x30, y30, v_y30 ,
      x40, v_x40, y40, v_y40)

M = 2 * 10 ** 30
m1 = 6 * 10** 24

N = 4
G = 6.67 * 10**(-11)

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)
print(sol)
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

balls = []
balls_lines = []

earth, = plt.plot([], [], 'o', color='b', ms=10)
plt.plot(0, 0, 'o', color='y', ms=20)

for i in range(N):
    balls.append(plt.plot([], [], 'o', color='r'))
    balls_lines.append(plt.plot([], [], '-', color='r'))

def animate(i):
    earth.set_data(sol[i, 0], sol[i, 2])

    for j in range(1, N):
        balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])
        balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('lec_13_N_body.gif')
