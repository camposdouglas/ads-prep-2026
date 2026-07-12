# Exercício: Avaliador de sessão de estudo
#
# Crie um programa que avalia uma sessão de estudo informada pelo usuário.
#
# O programa deve pedir as seguintes informações:
#
# - tecnologia estudada
# - duração da sessão em minutos
# - nível de dificuldade percebido
# - se houve distração durante a sessão
#
# Regras:
#
# 1. A tecnologia não pode estar vazia.
#
# 2. A duração deve ser maior que zero.
#
# 3. O nível de dificuldade deve ser um número entre 1 e 5.
#
# 4. A resposta sobre distração deve ser "sim" ou "nao".
#
# 5. Se algum dado for inválido, mostre uma mensagem de erro correspondente.
#
# 6. Se os dados forem válidos, classifique a sessão:
#
#    - duração menor que 30 minutos:
#      "Sessão curta."
#
#    - duração entre 30 e 90 minutos:
#      "Sessão normal."
#
#    - duração maior que 90 minutos:
#      "Sessão longa."
#
# 7. Depois, avalie a qualidade da sessão:
#
#    - Se não houve distração e a dificuldade foi menor ou igual a 3:
#      "Sessão produtiva."
#
#    - Se houve distração e a dificuldade foi maior ou igual a 4:
#      "Sessão difícil."
#
#    - Caso contrário:
#      "Sessão regular."
#
# Nesta versão, use:
#
# - input()
# - int()
# - variáveis
# - if / elif / else
# - operadores lógicos: and / or
# - print()
#
# Não use:
#
# - funções
# - classes
# - listas
# - dicionários
# - arquivos
# - banco de dados

tecnologia_estudada = input("Qual tópico está sendo estudado? ")
duracao_minutos = int(input("Quanto tempo de estudo? (em minutos) "))
nivel_dificuldade = int(input("Qual o nivel de dificuldade percebido? (de 1 a 5) "))
houve_distracao = input("Houve distração? (responda 'sim' ou 'nao') ")

if tecnologia_estudada == "":
    print("Tecnologia inválida.")
elif duracao_minutos <= 0:
    print("Duração inválida.")
elif nivel_dificuldade < 1 or nivel_dificuldade > 5:
    print("Nível de dificuldade inválido.")
elif houve_distracao != "sim" and houve_distracao != "nao":
    print("Notação sobre distração inválida.")
else:
    if duracao_minutos < 30:
        print("Tempo de sessão: curta.")
    elif duracao_minutos <= 90:
        print("Tempo de sessão: normal.")
    else:
        print("Tempo de sessão: longa.")

    if houve_distracao == "nao" and nivel_dificuldade <= 3:
        print("Qualidade de sessão: produtiva.")
    elif houve_distracao == "sim" and nivel_dificuldade >= 4:
        print("Qualidade de sessão: difícil.")
    else:
        print("Qualidade de sessão: regular.")
