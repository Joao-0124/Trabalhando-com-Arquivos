#1  Desenvolver um algoritmo que colete as seguintes informações: Nome do aluno, Nota 1, Nota 2, Nota 3 
#    Salvar dados coletados em um arquivo chamado notas.txt
while True:
    nome = input("Nome do Aluno:\n")
    nota1 = float(input("Nota 1:\n"))
    nota2 = float(input("Nota 2:\n"))
    nota3 = float(input("Nota 3:\n"))
    with open("Alunos.txt" , "a") as arquivo:
        arquivo.write(f"{nome} {nota1} {nota2} {nota3} \n")  
    if(input("Deseja Acrescentar mais um Aluno?? (S, N)" )) != "S":
        break
#2  Desenvolver um algoritmo que: Leia o arquivo notas.txt Calcule a média das notas de cada aluno; 
#   Verifique o resultado: (Aprovado = Média>=7, Exame= Média <7 e Média >=5, Reprovado < 5)
#   Salve as informações (Todas que achar necessário) em 3 arquivos:
#   aprovados.txt   exame.txt   reprovados.txt
    
with open("Alunos.txt" , "r") as arquivo:
    linhas = arquivo.readlines()
for linha in linhas:

    soma = nota1 + nota2 + nota3
    media = soma / 3
    if media >= 7:
        with open("Aprovados.txt", "a") as arquivo_aprovados:
            arquivo_aprovados.write(f"{nome} {media}\n")
    elif media < 7 and media >= 5:
        with open("Exame.txt", "a") as arquivo_exame:
            arquivo_exame.write(f"{nome} {media}\n")
    elif media < 5:
        with open("Reprovado.txt", "a") as arquivo_reprovado:
            arquivo_reprovado.write(f"{nome} {media}\n")

#3  Desenvolver um algoritmo que: Leia o arquivo exame.txt Coletar a nota do exame dos alunos em exame (alunos do arquivo exame.txt);
#   Calcule a média entre média anterior e a nota do exame; Verifique o resultado do aluno: Se a média calculada for >=5 o aluno 
#   estará aprovado, caso contrário reprovado; Caso o aluno for aprovado, adicionar ao final do arquivo aprovados.txt com a seguinte
#   legenda = Aprovado após exame; Caso o aluno for reprovado, adicionar ao final do arquivo reprovados.txt com a seguinte
#   legenda = Reprovado após exame;

with open("Exame.txt" , "r") as arquivo:
    linhas = arquivo.readlines()
