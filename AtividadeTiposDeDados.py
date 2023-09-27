# 1 Google Colab
print("ola mundo")
# 2 Números
# A 961.56
qtv_19 = 3
tkt_19 = 320.52
vtv_19 = qtv_19 * tkt_19
print(vtv_19)
###
# B 337.01
tkt_20 = 834.47
vtv_20 = 119.21
qtv_20 = int(tkt_20 / vtv_20)
print(qtv_20)
###
# C 294.33
qtv_23 = 5
vtv_23 = 15478.12
tkt_23 = float(vtv_23/qtv_23)
###
# 3 Strings
print('{:.2f}' .format(tkt_23))
cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
print(cancao)
cancao = cancao.upper()
print(cancao)
cancao = cancao.lower()
print(cancao)
cancao = cancao.split()
print(cancao)
noticia = 'Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos.'
silic = noticia[12:17]
print(silic)
ano = noticia[62:68]
print(ano)
# 4 Booleanos
a = False
b = True

x = not a & b

print(x)  # x = True
