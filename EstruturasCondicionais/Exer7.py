print("Informe os três lados de um triângulo")
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado3 + lado1 < lado2:
    print("Estes lados não formam um triângulo")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("é um triãngulo equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("é um triangulo isosceles")
    else:
        print("é um triangulo escaleno")

