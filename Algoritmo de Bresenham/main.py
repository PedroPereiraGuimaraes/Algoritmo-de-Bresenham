import matplotlib.pyplot as plt

plt.title("Algoritmo de Bresenham")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()


def AlgotimoBresenham(x1, y1, x2, y2):
    x = x1
    y = y1

    # Variação de X e Y
    dx = x2 - x1
    dy = y2 - y1

    # Valor inicial de D
    p = 2 * dy - dx

    # Incremento para mover E
    incE = 2 * dy

    # Incremento para mover NE
    incNE = 2 * (dy - dx)


    while x <= x2:
        plt.plot(x, y, "g.")
        x += 1
        if p <= 0:  # Escolhe E
            p += incE
        else:  # Escolhe NE
            p += incNE
            y += 1
    plt.plot([x1,x2],[y1, y2])
    plt.show()


def main():
    x1 = int(input("Digite o valor inicial de x: "))
    y1 = int(input("Digite o valor inicial de y: "))
    x2 = int(input("Digite o valor final de x: "))
    y2 = int(input("Digite o valor final de y: "))

    AlgotimoBresenham(x1, y1, x2, y2)


if __name__ == '__main__':
    main()
