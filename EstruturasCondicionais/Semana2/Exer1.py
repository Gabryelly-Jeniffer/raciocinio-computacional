# 1) Tendo como  dados de entrada a altura e o sexo de uma pessoa, construa um programa em python que calcule seu peso
# ideal, utilizando as seguintes formulas:
# - para homens: (72.7*h) - 58
# - para mulheres(62.h) - 44.7

sexo = input("Você é homem ou mulher?")
altura = float(input(f"Qual a sua altura?"))

if sexo == "mulher":
    peso_ideal = 62.1 * altura - 44.7
    print("Seu peso ideal é:", peso_ideal)
elif sexo == "homem":
    peso_ideal = 72.7* altura - 58
    print("Seu peso ideal é:", peso_ideal)
