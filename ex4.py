def situacao_alunos(arquivo):
    print(f"--- Alunos {arquivo[:-4]} ---")
    with open(arquivo, "r") as file:
        for linha in file:
            print(linha.strip())

def main():
    situacao_alunos("aprovados.txt")
    situacao_alunos("reprovados.txt")

if __name__ == "__main__":
    main()
