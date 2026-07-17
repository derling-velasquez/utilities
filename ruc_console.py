def validador(ruc):
    # 1. Limpieza estándar (eliminar guiones y pasar a mayúsculas)
    ruc_limpio = ruc.replace("-", "").strip().upper()
    
    # 2. Verificar estructura básica jurídica: J + 12 números + 1 letra = 14 caracteres
    if len(ruc_limpio) != 14 or not ruc_limpio.startswith("J"):
        return False
        
    num_parte = ruc_limpio[1:13]  # Extraer los 12 números del centro
    letra_original = ruc_limpio[13]
    
    if not num_parte.isdigit() or not letra_original.isalpha():
        return False
        
    # 3. Matemática oficial Módulo 11 de la DGI para jurídicos
    # Se usan 12 pesos (uno por cada dígito numérico intermedio)
    pesos = [14, 4, 9, 8, 7, 10, 2, 4, 8, 5, 10, 9]
    letras_validas = "ABCDEFGHJKL"
    
    suma = 0
    for digito, peso in zip(num_parte, pesos):
        suma += int(digito) * peso
        
    residuo = suma % 11
    resto = 11 - residuo
    posicion_letra = 0 if resto == 10 else resto
    
    # 4. Validar contra la letra de control
    if letra_original == letras_validas[posicion_letra]:
        return True
    else:
        return False

if __name__ == "__main__":
    ruc = input("INGRESE SU NUMERO RUC JURÍDICO: ")
    if validador(ruc):
        print("RUC Jurídico válido")
    else:
        print("Error: RUC Jurídico inválido")
