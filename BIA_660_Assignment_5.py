#importing libraries
import spacy
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from collections import Counter

nlp = spacy.load("en_core_web_lg") 
Book = requests.get('https://www.gutenberg.org/files/1661/1661-h/1661-h.htm')
soup = BeautifulSoup(Book.content,'lxml')

for script in soup(["pre","script", "style"]):
    script.extract()    
Book_content = soup.get_text()

text_file = open("SHERLOCK.txt", "w")
text_file.write(str(Book_content))
text_file.close()
Bookcontent = nlp(open("SHERLOCK.txt").read())


#Q1 How many tokens are in the document?
tokens = []
for token in Bookcontent:
    tokens.append(token.text)
print("The number of tokens in the document: ", len(tokens))


#Q2 How many verbs are in the document?
verbs = []
for verb in Bookcontent:
    if verb.pos_ == "VERB":
        verbs.append(verb.text)
print("The number of verbs in the document:" ,len(verbs))


#Q3 What is the most frequent named entity?
named_entity = [entity.label_ for entity in Bookcontent.ents]
print("The most frequently named entity:" ,Counter(named_entity).most_common(1))


#Q4 How many sentences are in the document?
sentence = []
for sent in Bookcontent.sents:
    sentence.append(sent.text)
print("The number of sentences in the document:",len(sentence))

#Q5 Of all the sentences in the text that are at least 10 words in length, which two are most similar (but not identical)?
dictionary = [sent for sent in list(Bookcontent.sents) if len(sent) >= 10]

similar_sentence = 0
for i in range(len(dictionary)-1):
    for j in range(i+1,len(dictionary)-1):
        s1 = dictionary[i]
        s2 = dictionary[j]
        similarity = s1.similarity(s2)
        if similarity > similar_sentence and s1.text != s2.text and similarity <.99:
            s1_high = i
            s2_high = j
            similar_sentence = similarity
print('Sentence 1: {}'.format(dictionary[s1_high].text))
print('Sentence 2: {}'.format(dictionary[s2_high].text))
print('Similarity: {}'.format(similar_sentence))


#Q6 What is the vector representation of the first word in the 15th sentence in the document?
vector = []
vector = sentence[15]
print("First word from sentence 15:", vector.split()[0])
print(vector)
vector1=nlp(str(vector.split()[0]))
print("Vector representation of first word:",vector1.vector)
