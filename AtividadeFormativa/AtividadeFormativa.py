
estudantes = {}

# Menu principal
def menu_principal():
      print("\nOlá, selecione uma das opições abaixo para prosseguir\n"
            "A) Estudantes\n"
            "B) Disciplinas\n"
            "C) Matrículas\n"
            "D) Professores\n"
            "E) Turmas\n")
      return input("Digite uma opção: ").upper()

opcao = menu_principal()

while opcao== "A" or opcao == "B" or opcao == "C" or opcao == "D" or opcao =="E":
      match opcao:
            case "A":
                  numero = 0
                  while numero!= 5:

                        print("menu de operações Estudande:"
                        "1. Atualizar\n"
                        "2. Excluir\n"
                        "3. Inclui\n"
                        "4. Listar\n"
                        "5. Voltar ao menu anterior\n")

                        #Coletar a opção do menu secundario
                        numero = int(input('Digite um numero valido'))
                        if numero == 1:
                              print("EM DESENVOLVIMENTO\n1")
                        elif numero == 2:
                              print("EM DESENVOLVIMENTO\n2")
                        elif numero == 3:
                              print("EM DESENVOLVIMENTO\n3")
                        elif numero == 4:
                              print("EM DESENVOLVIMENTO\n4")
            case _:
                  print("EM DESENVOLVIMENTO\n")

      opcao = menu_principal()





