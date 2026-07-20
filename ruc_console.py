def validador(ruc):
    # 1. Limpieza estándar (eliminar guiones y pasar a mayúsculas)
    ruc_limpio = ruc.replace("-", "").strip().upper()
        
    # Validación previa: Garantiza siempre una tupla (bool, str)
    if len(ruc_limpio) != 14:
        return False, "Longitud incorrecta"
        
    # Centralización: Extraer componentes comunes una sola vez
    num_parte = ruc_limpio[0:13] if not ruc_limpio.startswith("J") else ruc_limpio[1:13]
    letra_original = ruc_limpio[13]
    
    if not num_parte.isdigit() or not letra_original.isalpha():
        return False, "Formato numérico o letra inválida"
    
    # Despachador: Enrutar flujo según el tipo de documento
    if ruc_limpio.startswith("J"):
        es_valido = validador_juridico(num_parte, letra_original)
        return es_valido, ("RUC Jurídico" if es_valido else "RUC Jurídico Inválido")
    else:
        es_valido = validador_natural(num_parte, letra_original)
        return es_valido, ("Cédula / RUC Natural" if es_valido else "Cédula / RUC Natural Inválido")


def validador_juridico(num_parte, letra_original):
    # Matemática oficial Módulo 11 de la DGI para jurídicos
    pesos = [14, 4, 9, 8, 7, 10, 2, 4, 8, 5, 10, 9]
    letras_juridica = "ABCDEFGHJKL"
        
    suma = sum(int(digito) * peso for digito, peso in zip(num_parte, pesos))
            
    residuo = suma % 11
    resto = 11 - residuo
    posicion_letra = 0 if resto == 10 else resto
        
    return letra_original == letras_juridica[posicion_letra]


def validador_natural(num_parte, letra_original):
    # Matemática oficial Módulo 23 para personas naturales
    residuo = int(num_parte) % 23
    letras_natural = "ABCDEFGHJKLMNPQRSTUVWXY"
    
    return letra_original == letras_natural[residuo]
    

if __name__ == "__main__":
    ruc = input("INGRESE SU NUMERO RUC O CÉDULA: ")
    es_valido, tipo_doc = validador(ruc)
    
    if es_valido:
        print(f"Éxito: {tipo_doc}")
    else:
        print(f"Error: {tipo_doc}")
