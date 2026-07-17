def validador(ruc):
    longitud = len(ruc)
    if longitud == 14:
        if ruc[0:13].isdigit() and ruc[13].isalpha():
            suma = 0
            pesos = [14, 4, 9, 8, 7, 10, 2, 4, 8, 5, 10, 9, 7]
            letras_validas = "ABCDEFGHJKLMNPRSTUVWXYZA"
            lista_usuario = [int(digito) for digito in ruc[:13]]
            
            for digito, peso in zip(lista_usuario, pesos):
                suma += digito * peso
                
            residuo = suma % 11
            resto = 11 - residuo
            num_letra = 0 if resto == 10 else resto
            
            if ruc[13].upper() == letras_validas[num_letra]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    ruc = input("INGRESE SU NUMERO  RUC: ")
    if validador(ruc):
        print("RUC valido")
    else:
        print("Error: RUC inválido")
