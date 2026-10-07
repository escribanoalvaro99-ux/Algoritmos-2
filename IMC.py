
#ALGORITMO: CLASIFICAR_IMC
#ENTRADAS: peso, altura
#SALIDA: categoria
#imc = peso / (altura ** 2)
#SI imc < 18.5:
#categoria = "Bajo peso"
#SI NO:
#SI imc < 25:
#categoria = "Normal"
#SI NO:
#categoria = "Sobrepeso”
#DEVOLVER categoria
def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Bajo peso"
    else:
        if imc < 25:
            categoria = "Normal"
        else:
            categoria = "Sobrepeso"
    return categoria
