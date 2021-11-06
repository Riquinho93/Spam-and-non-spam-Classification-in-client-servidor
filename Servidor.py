#Import libraries
import socket
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

bind_ip = '127.0.0.1'   #IP connection
bind_port = 12345       #Port connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print(f"Escutando {bind_ip} e {bind_port}")
######################################################
### PRE-PROCESSING THE DATA
df = pd.read_csv("spam_or_not_spam.csv") # Read data
df_data = df[["email","label"]]
df_x = df_data['email']
corpus = df_x
cv = CountVectorizer()
X = cv.fit_transform(corpus.astype('U').values) # Fit the Data
######################################################
while True:
    """Accept a connection. The socket must be bound to an address and listening for connections. The return value
     is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection,
     and address is the address bound to the socket on the other end of the connection."""
    client_socket, addr = server.accept()
    print("Client connected: ",  addr)
    while True:
        request = client_socket.recv(1024) #the client uses any non-reserved port >1024 to connect to the server
        if not request or request.decode('utf-8')=='END':
            break


        try:
            client_socket.send( bytes('Hey Client', 'utf-8'))
            data = [request]
            spam_model = open("spam_model.pkl", "rb")   #load the model
            new_model = pickle.load(spam_model)
            vec = cv.transform(data).toarray() # pre-preocessing client menssage
            new_model.predict(vec) # Predict the model
            if new_model.predict(vec) == 1:
                print("Spam")
            else:
                print("Ham")
            print("Received from Client: %s" % request.decode('utf-8'))
            print('\n===========================\n')
        except:
            print('Exit!!')
    client_socket.close()


