class CalculoCimentacao:        #cria uma classe abstrata simples, dizendo q toda classe q herdar vai ter q ter esse metodo
    def calcular(self, dados):
        pass

class CalculoSimples(CalculoCimentacao):
    def calcular(self, dados):
        return dados['area'] * dados['altura']

class CalculoAvancado(CalculoCimentacao):
    def calcular(self, dados):
        return dados['area'] * dados['altura'] * 1.1

class CalculoPersonalizado(CalculoCimentacao):
    def calcular(self, dados):
        coef = dados.get('coef', 1.0)
        return dados['area'] * dados['altura'] * coef