if __name__ == "__main__":

    Numero = type("Numero", (), {"num": 100, "num_val": lambda x: x.num})

    retorno = Numero()

    print(type(Numero))
    print(Numero.num)
    print(retorno.__class__.__name__)
