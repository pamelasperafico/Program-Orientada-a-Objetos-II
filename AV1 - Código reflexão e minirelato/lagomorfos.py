class Lagomorfos:
    def __new__(classe, classifica_lagomorf=None):
        objeto = super().__new__(classe)
        if classifica_lagomorf:
            objeto.nome = classifica_lagomorf
        else:
            objeto.nome = "Coelho"

        print(type(objeto))
        return objeto


coelho = Lagomorfos()

print(coelho.nome)

lebre = Lagomorfos("lebre")
print(lebre.nome)
