import numpy as np

import matplotlib.pyplot as plt



# Definir las ecuaciones del sistema

# -2x + 5y + 9z = 1

# 7x + 3y + 2z = 6

# -3x + 7y - 2z = -26



# Coeficientes de las ecuaciones

A = np.array([[-2, 5, 9], [7, 3, 2], [-3, 7, -2]])

B = np.array([1, 6, -26])



# Resolver el sistema de ecuaciones

sol = np.linalg.solve(A, B)



# Imprimir la solución

print("La solución del sistema de ecuaciones es:", sol)



# Graficar las ecuaciones en un plano 2D

fig, ax = plt.subplots()



# Definir los valores de x y y para graficar las ecuaciones

x = np.linspace(-10, 10, 100)

y1 = (1 + 2*x + 9*sol[2])/5

y2 = (6 - 7*x - 2*sol[2])/3

y3 = (-26 + 3*x + 2*sol[2])/7



# Graficar las ecuaciones

ax.plot(x, y1, label='-2x + 5y + 9z = 1')

ax.plot(x, y2, label='7x + 3y + 2z = 6')

ax.plot(x, y3, label='-3x + 7y - 2z = -26')



# Configurar la leyenda y el título

ax.legend()

ax.set_title('Sistema de ecuaciones')



# Mostrar la gráfica

plt.show()
