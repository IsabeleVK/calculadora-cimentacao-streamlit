from factory import CalculoFactory

def calcular_volume(tipo, dados):
    calculo = CalculoFactory.criar(tipo)  # PEGA O OBJETO CERTO
    return calculo.calcular(dados)         # RETORNA O RESULTADO