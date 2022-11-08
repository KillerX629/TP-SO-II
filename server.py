import rpyc 

from rpyc.utils.server import ThreadedServer  # or ForkingServer

import sympy as sp



class Calculadora(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    #usamos esta funcion para establecer las variables de ecuaciones
    def exposed_create_symbol(self,character):
        if character not in self.symbols:
            self.symbols.append(sp.Symbol(character))
            return "Variable creada"
        else:
            return "Variable ya existe"
    

    def exposed_find_roots(self,eq):
        return self.solve_eq(eq)
    
    
    def solve_eq(self,eq):
        return sp.solve(eq,self.symbols)
    
    def exposed_get_answer(self):  # this is an exposed method
        return 42

    exposed_the_real_answer_though = 43     # an exposed attribute

    symbols = []
    
    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"


if __name__ == "__main__":
    t = ThreadedServer(Calculadora, port=18861)
    t.start()
    