#
#   Autor: Edgard Diaz
#   Este programa aproxima la raiz de una función mediante la técnica de bisección
#
from BisectionMethod import BisectionMethod

if __name__ == '__main__':
    a = float(input("Intervalo a: "))
    b = float(input("intervalo b: "))
    obj = BisectionMethod(a,b)

    obj.Aproximar_Raiz()
