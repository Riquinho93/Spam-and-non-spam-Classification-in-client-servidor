# Email Spam Filtering in client-servidor

## Introduction

It is difficult to find a user who has never received an unwanted or unpleasant message from an unknown or little-known recipient. Spam is something that is present in our online lives and that seems to grow more each day. The purpose of these spams is to sell some products or services; however, these are the best cases.

Some spams aim to obtain personal data such as full name, address, bank card number and password, corporate information and various other personal information that can be used for despised purposes. To solve this problem exists for types of solutions.

One of the solutions is spammers who have to identify spam emails and direct them to an area for this type of activity. So I studied how spammers work and create my own. However, I needed to see this in practice, so I created and tested it on a client-server.

## Dataset

At the moment, the databases have a total of 6000 lines, in excel format, that are being prepared for training and testing. The distribution of the data set is as follows: 66.33% to train the algorithm and 33.33% for tests. 

An important task in the development of machine learning algorithm is cleaning the data. At this stage, we are checking for errors or inaccurate records of the data set. Even in the phase of cleaning the data set, which generally remains most of the time, since it is a phase
that must be done manually. The lucky thing that our data set does not contain null values
or inaccurate records.

## Naive Bayes

One of the best algorithms for conducting supervised learning classification is undoubtedly Naive Bayes. It is based on Bayes' theorem, being very efficient for text classification.
Bayes' theorem [7] is a principle of calculating a conditional probability, that is, a probability that involves two events A and B and calculating the probability of event A knowing that event B has already occurred. The formula is:

	P(A|B) = P(A) P(B|A)/P(B)
		P(A/B): how often A happens given that B happens
		P(A): the probability of A being on his own
		P(B/A): how often B happens given that A happens
		P(B): the probability of B being on his own
		
The following is Bayes' theorem re-written in terms of our events:

	P(spam|word) =  _______P(spam)P(word/spam)_________________
			 P(spam)P(word/spam)+P(not-spam)P(word/not-spam)

	P(spam/word): is probability that an email has particular word given the email is spam
	
	P(spam): is probability that any given message is spam
		
	P(word/spam): is probability that the particular word appears in spam message
	
	P(not-spam): is the probability that any particular word is not spam
	
	P(word/not-spam): is the probability that the particular word appears in not-spam message

## Count Vectorization

After cleaning and pre-processing the data, the step process is to try to create a vocabulary of known words. We will do this by CountVectorizer. The idea of CountVectorizer, is very simple, it's to return a vector encoded with a length of the entire vocabulary and a count of the number of times each word appears in the message.

![image](https://user-images.githubusercontent.com/38785749/140624629-488236da-2023-4ab7-9c87-0ad2f53c0259.png)

The main idea is converting words to vectors to use as characteristics to help with
classification.

The model was built with the scikit-learn library using train_test_split () for the training
and evaluation of our model.

The train-test split procedure is appropriate when you have a very large data set, an
expensive model to train, or require a good estimate of the model's performance quickly.

To count the repetitions of each vocabulary word in each message, we use the
Multinomial Naive Bayes. Multinomial classification is more suitable for discrete values,
such as word counts. Multinomial Naive Bayes implements the naive Bayes algorithm for
multinomially distributed data, and is one of the two classic naive Bayes variants used in
text classification (where the data are typically represented as word vector counts, although
tf-idf vectors are also known to work well in practice).

## Accuracy of the model

The model's accuracy is 98.48%, we can say that it obtained 98.48% of the results of a test set. the set
of tests are emails that were not presented to the model in the training phase, as they were not
be a test it turned out. With this precision, we consider that he obtained an excellent result.

## Save the model

With the model already developed, it's important to use this model in real environments,
in which we can see the performance of the model with messages from our daily lives. For this
we must save the template so it can be used for the production module.

## Client-Server

Client-Server is any program that offers a service and that can be reached through a
network. The server accepts a request over the network, performs its services and returns the
result to the client. The client is the one who sends the request to the server and waits for a
response. 

![image](https://user-images.githubusercontent.com/38785749/140624757-f9295323-e25c-4aee-802e-7f49331297f1.png)


The client logs on to the server through a TCP connection by sending a command line that is returned back by the server, establishing a connection. The server receives the IP address and port number from the client.

The TCP server is more complex than the TCP client because the server has to make requests made by the client while maintaining the proper connection. The server is also able to maintain a connection request queue. To do this, a server makes open calls on the master device, specifying that it wants to create a passive TCP device. The server uses two control calls to manipulate the passive device. First, the server calls the control using function code TCPC_LISTENQ to define the length of the received request queue. The server then enters a loop in which it calls the control using function code TCPC_ACCEPT to accept the next incoming connection. The system allocates a slave device for each new connection and returns the slave device descriptor. 


## References:

https://realpython.com/train-test-split-python-data

Comer , Douglas E. Internetworking with TCP/IP: principles, protocols and arquitectures. 4th ed. 

Comer, Douglas E.  Stevens, David L. Internetworking with TCPIP. vol. 2 Internals and Implementation.

https://scikit-learn.org/stable/modules/feature_extraction.html

Hackeling, Gavin. Mastering Machine Learning with Scikit-learn. 2th ed. Published by Packt Publising Ltd: July 2017. 

https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes 
