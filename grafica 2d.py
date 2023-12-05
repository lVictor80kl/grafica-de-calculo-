import numpy as np
import matplotlib.pyplot as plt

def figura(solucion):
    """Muestra los datos y la figura"""
    fig, ax = plt.subplots()

    x = np.linspace(-10, 10, 100)
    y1 = (1 + 2*x + 9*solucion[2])/5
    y2 = (6 - 7*x - 2*solucion[2])/3
    y3 = (-26 + 3*x + 2*solucion[2])/7

    ax.plot(x, y1, label='-2x + 5y + 9z = 1')
    ax.plot(x, y2, label='7x + 3y + 2z = 6')
    ax.plot(x, y3, label='-3x + 7y - 2z = -26')

    ax.legend()
    ax.set_title('Sistema de ecuaciones')

    plt.show()
def resuelve():
    """Aqui se resuelve el sistema de ecuaciones"""
    
    A = np.array([[-2, 5, 9], [7, 3, 2], [-3, 7, -2]])
    B = np.array([1, 6, -26])

    solucion = np.linalg.solve(A, B)

    print("La solución del sistema de ecuaciones es:", solucion)

    return solucion


if __name__ == "__main__":
    soluciones = resuelve()
    figura(soluciones)
