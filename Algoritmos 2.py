#ALGORITMO: verificar_voto(edad)
  #  SI edad >= 18:
  #       DEVOLVER "Puedes votar"
 #SI NO:
       # DEVOLVER "No puedes votar"

def verificar_voto(edad):
    if edad >= 18:
        return "Puedes votar"
    else:
        return "No puedes votar"

