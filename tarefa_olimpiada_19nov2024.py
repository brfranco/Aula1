def determinar_grupo(matricula):
    """
    Função para determinar o grupo do aluno com base no número de matrícula.
    """
    if matricula % 2 == 0:  # Verifica se o número é par
        print("VOCÊ ESTÁ NO TIME AZUL.")
    else:  # Caso contrário, é ímpar
        print("VOCÊ ESTÁ NO TIME AMARELO.")

# Solicita o número de matrícula ao usuário
numero_matricula = int(input("Digite o número de matrícula do aluno: "))

# Chama a função para determinar o grupo
determinar_grupo(numero_matricula)
