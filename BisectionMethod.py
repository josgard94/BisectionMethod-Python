#
#   Autor: Edgard Díaz
#
#   Esta clase contiene la lógica del método de bisección para aproximación de  raices a partir de un intervalo [a,b]
#
#

import math as m

class BisectionMethod:

    def __init__(self,a,b):
        self.a = a;
        self.b = b;

    def punto_medio(self, a, b):
        return (a+b)/2

    def funcion(self,x):
        return 10 - (m.pow(x,2))
        #return m.pow(x,3) + 4 * pow(x,2) - 10;
        #return pow(x,3) + 4 * pow(x,2)

    def Aproximar_Raiz(self):
        n = 1
        iteraciones = 1000
        print("n \t\ta \t\t\tb \t\t\tc \t\t  f(a) \t\t  f(b) \t\t  f(c)")
        while (True):
            c = self.punto_medio( self.a, self.b);
            #print(c, self.funcion(self.a), self.funcion(self.b), self.funcion(c))
            print(str(n),"\t","{0:.5f}".format(self.a),"\t","{0:.5f}".format(self.b),"\t","{0:.5f}".format(c), "\t{0:.5f}".format(self.funcion(self.a)),"\t{0:.5f}".format(self.funcion(self.b)),"\t{0:.5f}".format(self.funcion(c)))
            if n > iteraciones:
                print("El programa no converge con el intervalo dado. . .")
                break
            else:
                if m.fabs(self.funcion(c)) <= 0.01:

                    print("\nResultado: \nRaiz aproximada: {0: .5f}".format(c)," Iteraciones realizadas: ", str(n), " Error: {0: .5f}".format(m.fabs(self.funcion(c))))
                    break

                else:
                    if self.funcion(c) * self.funcion(self.a) > 0:
                        self.a = c
                    elif self.funcion(c) * self.funcion(self.b) > 0:
                        self.b = c

            n = n + 1
