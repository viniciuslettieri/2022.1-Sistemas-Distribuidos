import socket

from Utils import constroi_mensagem, reconstroi_mensagem, printLog


class ModuloCliente:
    def __init__(self, HOST, PORT):
        printLog("Novo ModuloCliente", HOST, PORT)
        self.HOST = HOST
        self.PORT = int(PORT)
        self.inicializa()

    def inicializa(self):
        """ Cria e retorna o socket passivo para o servidor """
        if not hasattr(self, "sock"):
            sock = socket.socket()
            sock.connect((self.HOST, self.PORT))
            self.sock = sock    
            printLog("Novo ModuloCliente Inicializado")
    
    def enviaMensagem(self, msg):
        """ Envia a msg para o socket do objeto atual """
        printLog("enviaMensagem")
        byte_msg = constroi_mensagem(msg)
        self.sock.send(byte_msg)

    def recebeMensagem(self):
        """ Recupera mensagem enviada pelo servidor """
        printLog("recebeMensagem")
        response = reconstroi_mensagem(self.sock)
        return response

    def encerra(self):
        """ Encerra o socket atual """
        self.sock.close()
        printLog(f"Logoff ModuloCliente com Sucesso")