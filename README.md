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

	P(spam/word): is probability that an email has particular word given the      email is spam
	
	P(spam): is probability that any given message is spam
		
	P(word/spam): is probability that the particular word appears in spam          message
	
	P(not-spam): is the probability that any particular word is not spam
	
	P(word/not-spam): is the probability that the particular word appears in not-spam message


