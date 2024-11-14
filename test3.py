# Solicita o valor ao usuário
valor = float(input("Digite um valor: "))

# Calcula o dobro, triplo, quadrado, raiz quadrada e raiz cúbica
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor ** 0.5  # Raiz quadrada usando a potência de 0.5
raiz_cubica = valor ** (1/3)  # Raiz cúbica usando a potência de 1/3

# Exibe os resultados
print(f"O dobro de {valor} é: {dobro}")
print(f"O triplo de {valor} é: {triplo}")
print(f"O quadrado de {valor} é: {quadrado}")
print(f"A raiz quadrada de {valor} é: {raiz_quadrada:.2f}")
print(f"A raiz cúbica de {valor} é: {raiz_cubica:.2f}")