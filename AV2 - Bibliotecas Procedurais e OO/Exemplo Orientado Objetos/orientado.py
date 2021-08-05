from biblioteca import codigo_morse


def morse_para_caracteres(morse):
    for caracter in codigo_morse:
        if codigo_morse[caracter] == morse:
            return caracter
    return ""


def decodificar_morse(morse):
    texto_plano = ""
    for caracter_morse in morse.split(" "):
        caracter_plano = morse_para_caracteres(caracter_morse)
        texto_plano += caracter_plano
    return texto_plano


def caracteres_para_morse(caracter):
    if caracter in codigo_morse:
        return codigo_morse[caracter]
    else:
        return ""


def codificar_morse(texto_plano):
    texto_plano = texto_plano.upper()
    morse = ""
    for caracter in texto_plano:
        caracter_codificado = caracteres_para_morse(caracter)
        morse += caracter_codificado + " "
    return morse


def main():
    string = "Exemplo de string!"
    print("Codificado:")
    codificado = codificar_morse(string)
    print(codificado)
    print("Decodificado:")
    decodificado = decodificar_morse(codificado)
    print(decodificado)


if __name__ == "__main__":
    main()
