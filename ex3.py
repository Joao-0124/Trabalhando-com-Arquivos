def ler_notas_exame():
    alunos_notas_exame = []
    with open("exame.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(": ")
            aluno = partes[0]
            nota_exame = float(input(f"Digite a nota de exame: {aluno}\n"))
            alunos_notas_exame.append((aluno, nota_exame))
    return alunos_notas_exame

def calcular_media_final(media_anterior, nota_exame):
    return (media_anterior + nota_exame) / 2

def verificar_status(media_final):
    if media_final >= 5:
        return "Aprovado apos o exame"
    else:
        return "Reprovado apos o exame"

def atualizar_arquivo_exame(aluno, status):
    with open("exame.txt", "a") as arquivo:
        arquivo.write(f"\n{aluno}: {status}")

def salvar_arquivo(nome_arquivo, alunos):
    with open(nome_arquivo, "a") as arquivo:
        for aluno, media in alunos:
            arquivo.write(f"{aluno}: {media}\n")

def main():
    alunos_notas_exame = ler_notas_exame()

    for aluno, nota_exame in alunos_notas_exame:
        with open("exame.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(": ")
                if aluno == partes[0]:
                    media_anterior = float(partes[1])

        media_final = calcular_media_final(media_anterior, nota_exame)
        status = verificar_status(media_final)

        if status == "Aprovado apos o exame":
            salvar_arquivo("aprovados.txt", [(aluno, media_final)])
        else:
            salvar_arquivo("reprovados.txt", [(aluno, media_final)])

        atualizar_arquivo_exame(aluno, status)

    print("Status dos alunos após o exame atualizados no arquivo exame.txt!")
    
if __name__ == "__main__":
    main()