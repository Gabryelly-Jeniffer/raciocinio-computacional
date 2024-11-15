#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

estudantes = ['Lucas', 'Gabryel','Vitoria']

# Menu principal, realizado desse modo para não duplicar, em ordem alfabetica
def menu_principal():
      print("\nOlá, selecione uma das opições abaixo para prosseguir\n"
            "A) Estudantes\n"
            "B) Disciplinas\n"
            "C) Matrículas\n"
            "D) Professores\n"
            "E) Turmas\n")
      return input("Digite uma opção: ").upper()


# Menu principal, realizado desse modo para não duplicar, em ordem alfabetica
# param submenu - com o objetivo de identificar qual submenu foi selecionado
def menu_secundario(submenu):
      print(f"menu de operações: {submenu}\n"
            "1. Atualizar\n"
            "2. Excluir\n"
            "3. Inclui\n"
            "4. Listar\n"
            "5. Voltar ao menu anterior\n")

      # Coletar a opção do menu secundario
      return int(input('Digite um numero valido: '))

opcao = menu_principal()
numero = 0

while opcao== "A" or opcao == "B" or opcao == "C" or opcao == "D" or opcao =="E":
      match opcao:
            case "A":
                  while True:
                        numero = menu_secundario("Estudantes")
                        if numero == 1 or numero==2:
                              print("EM DESENVOLVIMENTO\n")
                        elif numero == 3:
                              print("===== INCLUSÃO =====")
                              nome=input('Informe o nome do estudante: ')
                              estudantes.append(nome)
                              input('Pressione ENTER para continuar\n')

                        elif numero == 4:
                              if not len(estudantes):
                                    print("Não há estudantes cadastrados\n")
                              else:
                                    print("===== LISTAR =====")
                                    for valor in estudantes:
                                          print("- ", valor)
                                    input('Pressione ENTER para continuar\n')
                        elif numero == 5:
                              break

            case _:
                  print("EM DESENVOLVIMENTO\n")

      opcao = menu_principal()






