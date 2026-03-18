from notificacao import Email, Sms, Push

class notificacaoFac:
    @staticmethod
    
    def enviar(tipo):
        if tipo == "email":
            return Email()
        elif tipo == "sms":
            return Sms()
        elif tipo== "push":
            return Push()
        else:
            raise ValueError("Tipo de notificacao inválido")