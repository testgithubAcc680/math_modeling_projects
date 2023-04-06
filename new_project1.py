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
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6,
     x7, v_x7, y7, v_y7,
     x8, v_x8, y8, v_y8) = s

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
    
    dxdt5 = v_x5
    dv_xdt5 = (
      	    - G * m1 * (x5 - x1) 
               / ((x5 - x1)**2 + (y5 - y1)**2)**1.5
            - G * M * x5 
               / (x5**2 + y5**2)**1.5)
    dydt5 = v_y5
    dv_ydt5 = (
      	    - G * m1 * (y5 - y1) 
               / ((x5 - x1)**2 + (y5 - y1)**2)**1.5
            - G * M * y5 
               / (x5**2 + y5**2)**1.5)
    dxdt6 = v_x6
    dv_xdt6 = (
      	    - G * m1 * (x6 - x1) 
               / ((x6 - x1)**2 + (y6 - y1)**2)**1.5
            - G * M * x6 
               / (x6**2 + y6**2)**1.5)
    dydt6 = v_y6
    dv_ydt6 = (
      	    - G * m1 * (y6 - y1) 
               / ((x6 - x1)**2 + (y6 - y1)**2)**1.5
            - G * M * y6 
               / (x6**2 + y6**2)**1.5)
    
    dxdt7 = v_x7
    dv_xdt7 = (
      	    - G * m1 * (x7 - x1) 
               / ((x7 - x1)**2 + (y7 - y1)**2)**1.5
            - G * M * (x7) 
               / ((x7)**2 + (y7)**2)**1.5)
    dydt7 = v_y7
    dv_ydt7 = (
      	    - G * m1 * (y7 - y1) 
               / ((x7 - x1)**2 + (y7 - y1)**2)**1.5
            - G * M * (y7) 
               / ((x7)**2 + (y7)**2)**1.5)
    dxdt8 = v_x8
    dv_xdt8 = (
      	    - G * m1 * (x8 - x1) 
               / ((x8 - x1)**2 + (y8 - y1)**2)**1.5
            - G * M * x8 
               / (x8**2 + y8**2)**1.5)
    dydt8 = v_y8
    dv_ydt8 = (
      	    - G * m1 * (y8 - y1) 
               / ((x8 - x1)**2 + (y8 - y1)**2)**1.5
            - G * M * y8 
               / (x8**2 + y8**2)**1.5)

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt5, dv_xdt5, dydt5, dv_ydt5,
            dxdt6, dv_xdt6, dydt6, dv_ydt6,
            dxdt7, dv_xdt7, dydt7, dv_ydt7,
            dxdt8, dv_xdt8, dydt8, dv_ydt8)

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

x50 = 151 * 10**9 
v_x50 = 8000
y50 = 500000
v_y50 = -26000

x60 = 151 * 10**9 
v_x60 = -14000
y60 = 0
v_y60 = -2200

x70 =  151 * 10**9 
v_x70 = 20000
y70 = 0
v_y70 = -10000

x80 = 150 * 10**9 
v_x80 = 0
y80 = 20000
v_y80 = 10000

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80)

M = 2 * 10 ** 30
m1 = 6 * 10** 24

N = 6
G = 6.67 * 10**(-11)

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)
print(sol)
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

balls = []
balls_lines = []

for i in range(N):
    balls.append(plt.plot([], [], 'o', color='r'))
    balls_lines.append(plt.plot([], [], '-', color='r'))

def animate(i):
    for j in range(N):
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

ani.save('new.gif')