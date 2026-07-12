# Exercício: Validação de sessão de estudo
#
# Crie um programa que valide os dados de uma sessão de estudo.
#
# O programa deve trabalhar com três informações:
#
# - tecnologia estudada
# - duração da sessão em minutos
# - conteúdo estudado
#
# Regras:
#
# 1. A tecnologia não pode estar vazia.
# 2. A duração da sessão deve ser maior que zero.
# 3. O conteúdo estudado não pode estar vazio.
#
# Se alguma regra for violada, o programa deve mostrar uma mensagem de erro
# correspondente ao problema encontrado.
#
# Se todos os dados forem válidos, o programa deve mostrar que a sessão de
# estudo foi registrada com sucesso.
#
# Nesta versão, use apenas:
#
# - variáveis
# - if / elif / else
# - print()
#
# Não use input(), funções, classes, listas, arquivos ou banco de dados.

tecnologia = "git"
duracao_minutos = 60
conteudo = "Aprendeu-se comandos git introdutórios, como add, commit e push."

if tecnologia == "":
    print("Tecnologia ausente.")
elif duracao_minutos <= 0:
    print("Tempo insuficiente")
elif conteudo == "":
    print("Conteúdo ausente.")
else:
    print("Sessão de estudos registrada com sucesso.")
