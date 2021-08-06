import sys

from foo import Foo
from saudar import Cumprimentando

# Após compilar, uma saudação é mostrada em tela

if __name__ == "__main__":
    classe = sys.argv[0].capitalize()
    klasse = globals()[classe if classe in ["Foo"] else "Cumprimentando"]
    instancia = klasse()
    print(instancia.cumprimentar())
