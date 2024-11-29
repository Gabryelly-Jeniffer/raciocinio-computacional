#Escreva um algoritmo que receba cindo numeros do usuario e imprima a metade de cada número
#Mostre a soma de todas as metades no final

soma = 0 

for c in range(5):    

    n = float(input("Informe um valor"))

    metade = n / 2

    print(metade)

    soma = soma + metade

print("soma: {}". format(soma))


