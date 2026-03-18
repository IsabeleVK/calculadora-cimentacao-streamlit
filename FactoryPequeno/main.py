from notFactory import notificacaoFac
print("TIPOS: email | sms | push")

tipo= input("Escolha o tipo de notificacao: ")

notificacao= notificacaoFac.enviar(tipo)
mensagem= input("Digite a mensagem: ")

notificacao.enviar(mensagem)