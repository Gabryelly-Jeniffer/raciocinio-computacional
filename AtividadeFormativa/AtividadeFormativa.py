#Aluna: Gabryelly Jeniffer
#Disciplia: Raciociono Computacional

# Importando as funções criadas na atividade formativa
import FuncaoMenu as fun
import FuncaoEstudante as fun_estudante
import FuncaoProfessor as fun_professor
import FuncaoDisciplina as fun_disciplina


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

            case "B":
                  while True:
                        numero = fun.menu_secundario("Disciplinas")
                        if numero == 1:
                              fun_disciplina.editar_disciplina(disciplinas)
                        elif numero == 2:
                              fun_disciplina.excluir_disciplina(disciplinas)
                        elif numero == 3:
                              fun_disciplina.cadastrar_disciplina(disciplinas)
                        elif numero == 4:
                              if not len(disciplinas):
                                    print("Não há disciplinas cadastrados\n")
                              else:
                                    fun_disciplina.listar_disciplina(disciplinas)
                        elif numero == 5:
                              break
            case "C":
                  print("EM DESENVOLVIMENTO\n")
            case "D":
                  while True:
                        numero = fun.menu_secundario("Professor")
                        if numero == 1:
                              fun_professor.editar_professor(professores)
                        elif numero == 2:
                              fun_professor.excluir_professor(professores)
                        elif numero == 3:
                              (fun_professor.cadastrar_professor(professores))
                        elif numero == 4:
                              if not len(professores):
                                    print("Não há professores cadastrados\n")
                              else:
                                    fun_professor.listar_professor(professores)
                        elif numero == 5:
                              break
            case "E":
                  print("EM DESENVOLVIMENTO\n")
            case _:
                  print("EM DESENVOLVIMENTO\n")

      opcao = fun.menu_principal()






