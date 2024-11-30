#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

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

def excluir_item(lista, item_procura):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for item in lista:
        if item[item_procura] == codigo_para_excluir:
            print("Estamos prontos para remover essa Matricula.")
            lista.remove(item)
            input('Pressione ENTER para continuar\n')
            return