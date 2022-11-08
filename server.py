import rpyc 

from rpyc.utils.server import ThreadedServer  # or ForkingServer

import sympy as sp


class Calculadora(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        self.stop()
        
    #usamos esta funcion para establecer las variables de ecuaciones
    def exposed_create_symbol(self,character):
        if sp.Symbol(character) not in self.symbols:
            self.symbols.append(sp.Symbol(character))
            return "Variable creada"
        else:
            return "Variable ya existe"
    #este es un paso necesario, ya que el módulo sympy necesita saber cuales son las variables que se van a usar
    
    #esta es la función expuesta al cliente para resolver ecuaciones
    def exposed_find_roots(self,eq):
        return self.solve_eq(eq)
    
    
    def solve_eq(self,eq):
        return sp.solve(eq,self.symbols)
    
    def exposed_get_answer(self):  # this is an exposed method
        return 42
    symbols = []
    

if __name__ == "__main__":
    t = ThreadedServer(Calculadora, port=18861)
    t.start()
    