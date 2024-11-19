lista = ['banana', 'maca', 'pera', 'banana']
tupla = (1, 2, 3, 4, 5)
meu_set = {1, 2, 3, 4}
dicionario = {"nome": "Caique", "idade": 22}

def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("Limão", "Morango")

for frutas in lista:
    print(f"Os elementos contidos na lista sâo: {frutas}")

var_txt = "Texto"
for letras in var_txt:
    print(letras)

for x in lista:
     print(f"Os elementos contidos na lista são: {x}")

dicionario = {"nome": "Caique", "idade": 22}

for chave in dicionario:
    print(f"As chaves neste dicionario são: {chave}")

for w in dicionario.values():
    print(f"Os valores neste dicionário são: {w}")

for chave,valor in dicionario.items():
    print(dicionario["idade"])
    print(dicionario["nome"])
    print(f"Chave: {chave}, Valor: {valor}")


lista = ['banana', 'maca', 'uva']

def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("Abacate", "Sorvete")

def del_fruta():
    lista.pop()
    print(lista)

del_fruta()

for x in lista:
    print(f"Esta fruta está na lista {x}")
