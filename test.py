# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 09:50:47 2023

@author: 20060
"""

# Import the libraries
from newspaper import Article
import random
import string 
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings 
warnings.filterwarnings('ignore')

#Download the punkt package.
nltk.download('punkt', quiet=True)

#Get the article 
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse() 
article.nlp()
corpus = article.text 

# Print 
print(corpus)

#Tokenization
text =corpus
sentence_list = nltk.sent_tokenize(text) # A list of sentences

#Print the list of sentences
print(sentence_list)

# A function to return a random greeting response to a users greeting
def greeting_response(text):
    text = text.lower()
    
    #Bots greeting response
    bot_greetings = ['howdy' , 'hi' , 'hey' , 'hello' , 'hola']
    #Users greeting
    user_greetings = ['hi' , 'hey' , 'hello' , 'hola' , 'greetings' , 'wassup']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    
    return list_index
                
#Create the bots response 
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response= ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1] , cm) #iki vektör arası benzerliği ölçmek için kullanılır
    similarity_scores_list = similarity_scores.flatten() #matrisi düzleştirmeye yarar
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
    #print(similarity_scores_list)    
    if response_flag == 0:
        bot_response = bot_response+' '+"I apologize, I don't understand."
    
    sentence_list.remove(user_input)
    
    return bot_response
    
#Start the chat
print('Doc Bot: I am Doctor Bot or Doc Bot for short. I will answer your queries about Chronic Kidney Disease. If you want to exit , type bye')
   
exit_list = ['exit' , 'see you later' , 'bye' , 'quit' , 'break']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc Bot: Chat with you later !')
        break 
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot: '+greeting_response(user_input))
        else:
            print('Doc Bot: '+bot_response(user_input))
    
   
   
    
   
    
   
    
   
    
   
    
   
    
    
    
    
    