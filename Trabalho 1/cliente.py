import socket
import Utils

HOST = 'localhost'  # ip/server to send messages. If it's in another computer, input the ip
DOOR = 7678       # Door used by both client/server

MESSAGE_SIZE = 256 # We will use one unsigned byte to represent size of message. 1 byte for length of message, and 2^8 - 1 for message.

# create socket (instantiation)
activeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect with client server side
activeSock.connect((HOST, DOOR))

# Keep sending message to server
userInput = input()

while (userInput != "exit"):  # exit will close communication
    #message_length_byte = len(userInput).to_bytes(1, 'little', )
    #encodedMessage = message_length_byte
    #encodedMessage += bytes(userInput, encoding='utf-8')
    activeSock.sendall(Utils.constroi_mensagem(userInput))

    # application blocked until receives message
    message = Utils.reconstroi_mensagem(activeSock)

    # Print received message
    print(message)

    # Keep receiving user input
    userInput = input()


# Close connection
activeSock.close()
