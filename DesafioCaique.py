nome = "PAULA MARTINS"
mes = "Janeiro"
valor_compra = 500
desconto = 10
cupom = "PAULAÉ10"

print("Olá, " + nome + ". Em " + mes + " você realizou uma compra no valor de R$" + str(valor_compra) + " e ganhou um desconto de " + str(desconto) + "% em sua próxima compra. Use o cupom " + cupom + ".")

nome = input("Qual é seu nome completo?:")
mes = int(input("Qual foi o mês da sua compra?"))
valor_compra = float(input("Qual é o valor da sua compra?"))
desconto = 10
cupom = "É10"
print(f"Olá, {nome}. Em {mes} você realizou uma compra no valor de R${valor_compra} e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom}.