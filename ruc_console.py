def validador(ruc):
    # 1. Limpieza estándar (eliminar guiones y pasar a mayúsculas)
    ruc_limpio = ruc.replace("-", "").strip().upper()
        
    if len(ruc_limpio) != 14:       # Si no es 14 no procesa nada
        return False
        
    if ruc_limpio.startswith("J"):  # Si empieza con jota lo mandamos a validador_juridico
        if validador_juridico(ruc_limpio):
            return True
    else:
        if validador_natural(ruc_limpio):   # Si no empieza con jota, lo mandamos a validador_natural
            return True
    return False
        
def validador_juridico(ruc_juridico):
    num_parte = ruc_juridico[1:13]  # Extraer los 12 números del centro
    letra_original = ruc_juridico[13]
    if not num_parte.isdigit() or not letra_original.isalpha():
        return False
    
    # 3. Matemática oficial Módulo 11 de la DGI para jurídicos
    # Se usan 12 pesos (uno por cada dígito numérico intermedio)
    pesos = [14, 4, 9, 8, 7, 10, 2, 4, 8, 5, 10, 9]
    letras_juridica = "ABCDEFGHJKL"
        
    suma = 0
    for digito, peso in zip(num_parte, pesos):
        suma += int(digito) * peso
            
    residuo = suma % 11
    resto = 11 - residuo
    posicion_letra = 0 if resto == 10 else resto
        
    # 4. Validar contra la letra de control
    if letra_original == letras_juridica[posicion_letra]:
        return True
    else:
        return False

def validador_natural(ruc_natural):
    num_parte = (ruc_natural[0:13])     # Extraer los 13 números del centro
    letra_original = ruc_natural[13]    # Extraer la letra final
    
    if not num_parte.isdigit() or not letra_original.isalpha():
        return False
        
    residuo = int(num_parte) % 23
    
    posicion_letra = residuo
    letras_natural = "ABCDEFGHJKLMNPQRSTUVWXY"

    if letra_original == letras_natural[posicion_letra]:
        return True
    else:
        return False
        

if __name__ == "__main__":
    ruc = input("INGRESE SU NUMERO RUC O CÉDULA: ")
    if validador(ruc):
        print("RUC válido")
    else:
        print("Error: RUC inválido")
