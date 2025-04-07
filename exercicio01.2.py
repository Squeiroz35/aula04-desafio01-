numero= int(input("digite um numero"))
meses= ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
if numero > 12:
    print("valor invalido")
else:
    print(meses[numero-1])