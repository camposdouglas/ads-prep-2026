# Exercício: Status da meta diária
#
# Crie um programa que diga se uma meta diária de estudo foi atingida.
#
# O programa deve trabalhar com duas informações:
#
# - minutos_estudados
# - meta_minutos
#
# Regras:
#
# 1. Se a meta for menor ou igual a 0, mostre:
# "Meta inválida."
#
# 2. Se os minutos estudados forem menores que 0, mostre:
# "Tempo estudado inválido."
#
# 3. Se os minutos estudados forem maiores ou iguais à meta, mostre:
# "Meta atingida."
#
# 4. Caso contrário, mostre:
# "Meta não atingida."
#
# Nesta versão, use:
#
# - variáveis
# - if / elif / else
# - operadores de comparação
# - print()
#
# Não use input(), funções, classes, listas, arquivos ou banco de dados.

minutos_estudados = 120
meta_minutos = 60

if meta_minutos <= 0:
    print("Meta inválida.")
elif minutos_estudados < 0:
    print("Tempo estudado inválido.")
elif minutos_estudados >= meta_minutos:
    print("Meta atingida.")
else:
    print("Meta não atingida.")
