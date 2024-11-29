
def listar_matricula(lista):
    print("===== LISTAR =====")
    for matricula in lista:
        print(matricula)
    input('Pressione ENTER para continuar\n')

def excluir_matricula (lista):
    print("===== EXCLUSÃO =====")
    codigo_para_excluir = int(input("Qual é o codigo que deseja excluir?"))
    for matricula in lista:
        if matricula["cod_est"] == codigo_para_excluir:
            print("Estamos prontos para remover essa Matricula.")
            lista.remove(matricula)
            input('Pressione ENTER para continuar\n')


