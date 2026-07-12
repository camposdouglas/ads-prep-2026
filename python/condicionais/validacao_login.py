# Exercício: Validação de login
#
# Crie um programa que valide uma tentativa de login.
#
# O programa deve trabalhar com duas informações:
#
# - usuario
# - senha
#
# Regras:
#
# 1. O usuário não pode estar vazio.
# 2. A senha não pode estar vazia.
# 3. A senha deve ter pelo menos 8 caracteres.
#
# Se alguma regra for violada, mostre uma mensagem de erro correspondente.
#
# Se todos os dados forem válidos, mostre:
# "Login válido."
#
# Nesta versão, use:
#
# - variáveis
# - if / elif / else
# - len()
# - print()
#
# Não use input(), funções, classes, listas, arquivos ou banco de dados.

usuario = "admin"
senha = "admin"

if usuario == "":
    print("Usuário inválido.")
elif senha == "":
    print("Senha inválida.")
elif len(senha) < 8:
    print("Senha precisa de no mínimo 8 caracteres")
else:
    print("Login válido.")
