from model import CalculoSimples, CalculoAvancado, CalculoPersonalizado

class CalculoFactory:
    @staticmethod
    def criar(tipo):
        if tipo == "Simples":
            return CalculoSimples()
        elif tipo == "Avançado":
            return CalculoAvancado()
        elif tipo == "Personalizado":
            return CalculoPersonalizado()
        else:
            raise ValueError("Tipo de cálculo desconhecido")