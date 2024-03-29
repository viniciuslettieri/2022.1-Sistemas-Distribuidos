
def constroi_mensagem(string_msg):
    byte_msg = string_msg.encode("utf-8")
    msg = len(byte_msg).to_bytes(2, 'big')
    msg += byte_msg
    return msg

def reconstroi_mensagem(socket):
    msg = socket.recv(2)
    length = int.from_bytes(msg[:2], 'big')
    full_msg = socket.recv(length)
    return full_msg.decode("utf-8")

log = False

def activateLog():
    global log
    log = True

def printLog(message, *args):
    global log
    if log: 
        print(f"[Log: ${message}]", *args)