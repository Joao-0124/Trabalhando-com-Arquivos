def dados_alunos():
    nome_aluno = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    return nome_aluno, nota1, nota2, nota3

def salvar_dados_alunos(nome_aluno, nota1, nota2, nota3):
    with open("notas.txt", "a") as arquivo:
        arquivo.write(f"{nome_aluno} , {nota1} , {nota2} , {nota3}\n")

def adicionar_alunos():
    while True:
        nome_aluno, nota1, nota2, nota3 = dados_alunos()
        salvar_dados_alunos(nome_aluno, nota1, nota2, nota3)
        continuar = input("Deseja adicionar outro aluno? (s/n): ")
        if continuar.lower() != 's':
            break

def main():
    nome_aluno, nota1, nota2, nota3 = dados_alunos()
    salvar_dados_alunos(nome_aluno, nota1, nota2, nota3)
    print("Notas salvas com sucesso no arquivo notas.txt!")

if __name__ == "__main__":
    main()