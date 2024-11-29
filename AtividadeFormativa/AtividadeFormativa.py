#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

# Importando as funções criadas na atividade formativa
import FuncaoMenu as fun
import FuncaoEstudante as fun_estudante

estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []



opcao = fun.menu_principal()
numero = 0

while opcao== "A" or opcao == "B" or opcao == "C" or opcao == "D" or opcao =="E":
      match opcao:
            case "A":
                  while True:
                        numero = fun.menu_secundario("Estudantes")
                        if numero == 1:
                              fun_estudante.editar_estudante(estudantes)
                        elif numero == 2:
                              fun_estudante.excluir_estudante(estudantes)
                        elif numero == 3:
                              fun_estudante.cadastrar_estudante(estudantes)
                        elif numero == 4:
                              if not len(estudantes):
                                    print("Não há estudantes cadastrados\n")
                              else:
                                    fun_estudante.listar_estudantes(estudantes)
                        elif numero == 5:
                              break
            case _:
                  print("EM DESENVOLVIMENTO\n")

      opcao = fun.menu_principal()






