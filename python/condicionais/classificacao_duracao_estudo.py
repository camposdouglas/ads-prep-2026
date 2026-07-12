# Exercício: Classificação de duração de estudo
#
# Crie um programa que classifique uma sessão de estudo com base na duração.
#
# O programa deve trabalhar com uma informação:
#
# - duracao_minutos
#
# Regras:
#
# 1. Se a duração for menor ou igual a 0, mostre:
# "Duração inválida."
#
# 2. Se a duração for menor que 30 minutos, mostre:
# "Sessão curta."
#
# 3. Se a duração for entre 30 e 90 minutos, mostre:
# "Sessão normal."
#
# 4. Se a duração for maior que 90 minutos, mostre:
# "Sessão longa."
#
# Nesta versão, use:
#
# - variáveis
# - if / elif / else
# - operadores de comparação
# - print()
#
# Não use input(), funções, classes, listas, arquivos ou banco de dados.

duracao_minutos = 45

if duracao_minutos <= 0:
    print("Duração inválida.")
elif duracao_minutos < 30:
    print("Sessão curta.")
elif duracao_minutos <= 90:
    print("Sessão normal.")
else:
    print("Sessão longa.")
