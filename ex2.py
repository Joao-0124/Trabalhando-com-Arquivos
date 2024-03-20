def ler_notas_arquivo():
    alunos_notas = []
    with open("notas.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(",")
            nome_aluno = partes[0]
            notas = [float(nota) for nota in partes[1:]]
            alunos_notas.append((nome_aluno, notas))
    return alunos_notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_alunos(alunos_notas):
    aprovados = []
    exame = []
    reprovados = []

    for aluno, notas in alunos_notas:
        media = calcular_media(notas)
        if media >= 7:
            aprovados.append((aluno, media))
        elif media >= 5:
            exame.append((aluno, media))
        else:
            reprovados.append((aluno, media))

    return aprovados, exame, reprovados

def salvar_arquivo(nome_arquivo, alunos):
    with open(nome_arquivo, "w") as arquivo:
        for aluno, media in alunos:
            arquivo.write(f"{aluno}: {media}\n")

def main():
    alunos_notas = ler_notas_arquivo()
    aprovados, exame, reprovados = classificar_alunos(alunos_notas)

    salvar_arquivo("aprovados.txt", aprovados)
    salvar_arquivo("exame.txt", exame)
    salvar_arquivo("reprovados.txt", reprovados)

    print("Informações salvas nos arquivos aprovados.txt, exame.txt e reprovados.txt!")

if __name__ == "__main__":
    main()