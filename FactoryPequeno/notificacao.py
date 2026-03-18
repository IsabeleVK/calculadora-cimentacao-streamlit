class notificacao:
    def enviar(self, mensagem):
        pass
    
class Email:
    def enviar(self, mensagem):
        print("Enviando email...", mensagem)
        
class Sms:
    def enviar(self, mensagem):
        print("Enviando sms", mensagem)
        
class Push:
    def enviar(self, mensagem):
        print("Enviando push", mensagem)
    