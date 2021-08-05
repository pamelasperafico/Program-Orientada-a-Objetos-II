from biblioteca import codigo_morse


def codificar_morse(texto_plano):
    texto_plano = ""
    for caracter in texto_plano:
        if caracter != " ":
            texto_plano += codigo_morse[caracter] + " "
        else:
            texto_plano += " "
    return texto_plano


def decodificar_morse(morse):
    morse += " "
    texto_plano = ""
    caracter_plano = ""
    for caracter in morse:
        if caracter != " ":
            i = 0
            caracter_plano += caracter
        else:
            i += 1
            if i == 2:
                texto_plano += " "
            else:
                texto_plano += list(codigo_morse.keys())[
                    list(codigo_morse.values()).index(caracter_plano)
                ]
                caracter_plano = ""
    return texto_plano


def main():
    message = "Exemplo de string!"
    result = codificar_morse(message.upper())
    print("Codificado:")
    print(result)
    print("Decodificado:")
    message = ". -..- . -- .--. .-.. ---  -.. .  ... - .-. .. --.-- --. −.−.−− "
    result = decodificar_morse(message)
    print(result)


if __name__ == "__main__":
    main()
