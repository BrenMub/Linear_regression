def main():
    pesos = [0.1, 0.2, 0.15, 0.1, 0.2, 0.15, 0.1]
    vector1 = [1,3,2,4,5,6,3]
    vector2 = [2,6,4,8,10,12,6]
    vector3 = [1,5,3,7,9,11,5]
    vector4 = [7,2,6,3,1,4,2]

    print(calcular_producto_interno(pesos, vector4, vector4))



def calcular_producto_interno(pesos: list, vector1, vector2):
    sum = 0
    for i in range(len(vector1)):
        sum += pesos[i]*vector1[i]*vector2[i]
    return sum


if __name__ == "__main__":
    main()