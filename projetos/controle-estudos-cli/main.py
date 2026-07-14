# Micro-projeto: Controle de Estudos CLI
#
# Objetivo:
# Criar um programa de terminal para registrar, listar e resumir sessões de estudo.
#
# O programa deve ser desenvolvido em etapas. Não tente fazer tudo de uma vez.
#
# Etapa 1 — Menu principal
#
# Crie um menu que mostre as opções:
#
# 1 - Registrar sessão de estudo
# 2 - Listar sessões registradas
# 3 - Mostrar resumo geral
# 0 - Sair
#
# O menu deve continuar aparecendo até o usuário escolher a opção 0.
#
# Nesta etapa, as opções 1, 2 e 3 ainda podem mostrar apenas uma mensagem
# provisória, como "opção ainda não implementada".
#
# Etapa 2 — Lista de sessões
#
# Crie uma lista vazia para armazenar as sessões de estudo.
#
# Cada sessão de estudo será representada por um dicionário.
#
# Etapa 3 — Registrar sessão
#
# Implemente a opção 1 do menu.
#
# O programa deve pedir:
#
# - tecnologia estudada
# - conteúdo estudado
# - duração em minutos
# - nível de dificuldade, de 1 a 5
# - se houve distração, respondendo "sim" ou "nao"
#
# Depois de receber os dados, o programa deve criar um dicionário representando
# a sessão e adicionar esse dicionário à lista de sessões.
#
# Etapa 4 — Validar dados
#
# Antes de registrar a sessão, valide os dados:
#
# - tecnologia não pode estar vazia
# - conteúdo estudado não pode estar vazio
# - duração deve ser maior que zero
# - dificuldade deve estar entre 1 e 5
# - distração deve ser "sim" ou "nao"
#
# Se algum dado for inválido, mostre uma mensagem de erro e não registre a sessão.
#
# Etapa 5 — Listar sessões
#
# Implemente a opção 2 do menu.
#
# O programa deve mostrar todas as sessões registradas até o momento.
#
# Para cada sessão, mostre:
#
# - tecnologia
# - conteúdo
# - duração
# - dificuldade
# - distração
#
# Se nenhuma sessão tiver sido registrada, mostre uma mensagem informando isso.
#
# Etapa 6 — Mostrar resumo geral
#
# Implemente a opção 3 do menu.
#
# O resumo deve mostrar:
#
# - total de sessões registradas
# - total de minutos estudados
# - total de horas estudadas
#
# Se não houver sessões registradas, mostre uma mensagem informando isso.
#
# Etapa 7 — Organizar com funções
#
# Depois que o programa funcionar de forma simples, organize o código em funções.
#
# Funções sugeridas:
#
# - mostrar_menu()
# - registrar_sessao(sessoes)
# - listar_sessoes(sessoes)
# - mostrar_resumo(sessoes)
# - validar_sessao(...)
#
# Etapa 8 — Persistência em arquivo JSON
#
# Depois que o programa funcionar em memória, adicione persistência.
#
# O programa deve:
#
# - carregar as sessões salvas ao iniciar
# - salvar a lista de sessões depois de registrar uma nova sessão
#
# Use um arquivo chamado:
#
# data/sessoes.json
#
# Restrições da versão atual:
#
# Use:
#
# - input()
# - print()
# - variáveis
# - if / elif / else
# - while
# - for
# - funções
# - listas
# - dicionários
# - arquivos JSON
#
# Não use ainda:
#
# - classes
# - banco de dados
# - frameworks
#
# Critério de conclusão:
# O programa deve permitir registrar sessões, listar sessões, mostrar um resumo
# geral e encerrar pelo menu.


def main():
    sessoes = []
    saudacao()
    while True:
        mostrar_menu()
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 0:
            print()
            print("Encerrando o programa. Até mais!")
            break
        elif opcao_escolhida == 1:
            registrar_sessao(sessoes)
        elif opcao_escolhida == 2:
            listar_sessoes(sessoes)
        elif opcao_escolhida == 3:
            mostrar_resumo(sessoes)
        else:
            print()
            print("Opção desconhecida.")
            print()


def saudacao():
    print("Bem-vindo ao Controle de Estudos por CLI!")
    print()


def mostrar_menu():
    print("""1 - Registrar sessão de estudo
2 - Listar sessões registradas
3 - Mostrar resumo geral
0 - Sair""")
    print()


def registrar_sessao(sessoes):
    tecnologia_estudada = ler_campo(
        "Qual tecnologia você estudou hoje? ", "Erro: Campo não pode estar vazio."
    )
    conteudo_estudado = ler_campo(
        "Qual conteúdo você aprendeu hoje? ", "Erro: Campo não pode estar vazio."
    )
    duracao_minutos = ler_tempo(
        "Quanto tempo você estudou, em minutos? ",
        "Erro: Tempo deve ser maior do que zero.",
    )
    nivel_dificuldade = ler_nivel(
        "Qual o nível de dificuldade percebido, de 1 a 5? ",
        "Erro: Nível deve ser um número de 1 a 5.",
    )
    houve_distracao = ler_distracao(
        "Houve distração durante os estudos? ", "Erro: Responda com 'sim' ou 'nao'."
    )

    sessao = {
        "tecnologia": tecnologia_estudada,
        "conteudo": conteudo_estudado,
        "duracao": duracao_minutos,
        "nivel": nivel_dificuldade,
        "distracao": houve_distracao,
    }

    sessoes.append(sessao)

    print()
    print("Sessão registrada com sucesso!")
    print()


def ler_campo(mensagem_pergunta, mensagem_erro):
    while True:
        campo = input(mensagem_pergunta)
        if campo == "":
            print(mensagem_erro)
        else:
            return campo


def ler_tempo(mensagem_pergunta, mensagem_erro):
    while True:
        tempo = int(input(mensagem_pergunta))
        if tempo <= 0:
            print(mensagem_erro)
        else:
            return tempo


def ler_nivel(mensagem_pergunta, mensagem_erro):
    while True:
        nivel = int(input(mensagem_pergunta))
        if nivel < 1 or nivel > 5:
            print(mensagem_erro)
        else:
            return nivel


def ler_distracao(mensagem_pergunta, mensagem_erro):
    while True:
        distracao = input(mensagem_pergunta)
        if distracao != "sim" and distracao != "nao":
            print(mensagem_erro)
        else:
            return distracao


def listar_sessoes(sessoes):
    if sessoes == []:
        print()
        print("Não há sessões registradas.")
        print()
    else:
        for indice, sessao in enumerate(sessoes):
            print()
            print(f"Sessão {indice + 1}:")
            for chave, valor in sessao.items():
                print(f"{chave.capitalize()}: {valor}")
        print()


def mostrar_resumo(sessoes):
    print()
    print("Função Mostrar não habilitada ainda.")
    print()


main()
