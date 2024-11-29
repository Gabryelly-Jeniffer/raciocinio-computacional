# Faça um algoritmo que:
# a) receba a quantidade de cupons apresentados a cada nova mesa ocupada
# b) informe a quantidade de cupons restantes até atingir o limite da noite
# c) mostre a mensagem: "Não devem mais ser aceitos cupons de desconto" quando o limite for atingido
#
# O limite pode ser fixado em 10.

limite = 10

while limite > 0:

    
    qtde = int(input("Quantos cupons foram apresentados?"))

    limite = limite - qtde

    if limite > 0:
        print("Ainda temos {} cupons." .format (limite))
    else:
        print("Não devem mais ser aceitos cupons de desconto")

        
        
    

