def contador_vocales(palabra):
    result = {}
    vocales = ("a", "e", "i", "o", "u")
    palabra = palabra.lower()
    for letra in palabra:
        if letra in vocales:
            if letra not in result:
                result[letra] = 0
            result[letra] += 1
    return result