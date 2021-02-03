import csv
import os
import time
import nltk
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer
from collections import Counter
from BTrees.OOBTree import OOBTree
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

global refined_query    #original query string for or without stopwords 
global query_string     #original query string
global or_phrases       #list of query phrases/words to or

def not_empty(csvfile):
    has_rows = False
    for row in csvfile:
        has_rows = True
        break
    if has_rows:
        return True
    return False

#intersection between 2 posting lists
def intersection(a, b):
    c = [value for value in a if value in b]
    c = sorted(c)
    return c

#union of 2 posting lists
def union(a, b):
    c = list(set(a) | set(b))
    c = sorted(c)
    return c

#merging posting lists of query terms -making use of intersection function
def merge(query_terms):
    result = []
    iteration = 0
    for term in query_terms:
        if term in inverted_index.keys():
            if iteration == 0:
                result = inverted_index[term][1]     #1st term posting list
                iteration += 1
                #print(result)
                continue
            temp = intersection(result,inverted_index[term][1])
            iteration += 1
            result = temp
            #print(result)
    return result

def pre_processing(data):
    terms = []
    for row in data:
        snippet = row['Snippet']
        tks = tokenizer.tokenize(snippet)    #tokenized single snippet in single csv
        for i in tks:
            if i not in stop_words:
                terms.append(ps.stem(i))
        #tokens.extend(tks)                  #tokenized all snippets in a csv
    return terms

def cleaning(string):
    tks = tokenizer.tokenize(string)
    terms = []
    for i in tks:
            if i not in stop_words:
                terms.append(ps.stem(i))
    return terms

def printing(doc_id, row_index, row_details, score):
    print(score, '\t', doc_id,'\t', row_index, '\n')
    
    for key, value in row_details.items():
        print(key, '\t=======>\t', value,'\n')
    
    print('*******************\n')


def get_row_details(doc_id, query, score):
    query_terms = cleaning(query)
    path = doc_id_name[doc_id]
    
    with open(path, newline = '', encoding="utf-8") as csvfile:
        
        csvfile = csv.DictReader(csvfile)
        if not_empty(csvfile):
            
            # if ' or ' in query:
            #     temp = or_phrases
            #     and_terms = []
            #     for phrase_index in range(len(temp)):
                        
            #         and_terms = tokenizer.tokenize(temp[phrase_index])
            row_index = 0

            for row in csvfile:
                
                snippet_terms = cleaning(row['Snippet'])
                row_details = {}
                temp = []
                #print('or_phrases: ',or_phrases)
                
                if ' or ' in query:
                
                    for phrase_index in range(len(or_phrases)):
                        
                        phrase = or_phrases[phrase_index]
                        #print('temp: ',temp)
                        and_terms = tokenizer.tokenize(phrase)
                        
                        if len(and_terms) > 1:
                            x = all([item in snippet_terms for item in and_terms])
                            if x:
                                temp.append(True)
                            else:
                                temp.append(False)
                        else:
                            if or_phrases[phrase_index] in snippet_terms:
                                temp.append(True)
                            else:
                                temp.append(False)
                    
                    present = any(temp)

                    if present:
                        row_details['URL'] = row['\ufeffURL']
                        row_details['MatchDateTime'] = row['MatchDateTime']
                        row_details['Station'] = row['Station']
                        row_details['Show'] = row['Show']
                        row_details['IAShowID'] = row['IAShowID']
                        row_details['IAPreviewThumb'] = row['IAPreviewThumb']
                        row_details['Snippet'] = row['Snippet']

                        printing(doc_id, row_index, row_details, score)


                else:

                    present = all([item in snippet_terms for item in query_terms])
                    #print(all_present)
                
                    if present:
                        row_details['URL'] = row['\ufeffURL']
                        row_details['MatchDateTime'] = row['MatchDateTime']
                        row_details['Station'] = row['Station']
                        row_details['Show'] = row['Show']
                        row_details['IAShowID'] = row['IAShowID']
                        row_details['IAPreviewThumb'] = row['IAPreviewThumb']
                        row_details['Snippet'] = row['Snippet']

                        printing(doc_id, row_index, row_details, score)
                
                row_index += 1



#INVERTED INDEX

#initializing basic requirements
inverted_index = {}
ii_tree = OOBTree()
ps = PorterStemmer()
tokenizer = nltk.RegexpTokenizer(r"\w+") 
stop_words = set(stopwords.words('english'))
doc_id_name = {}
vectorizer = TfidfVectorizer()

start1 = time.time()
#path of documents
#path1 ='D:\AIR\TelevisionNews'
#path1 = "/Users/varuntheboss/Documents/School/PES/4th year/AIR/AIR project/AIR PROJECT/TelevisionNews"
path1 = "C:\\Users\\pbhav\\Desktop\\Finale\\AIR\\Project\\TelevisionNews"
doc_id = 0
for filename in os.listdir(path1): 
    full_path = os.path.join(path1, filename)
    with open(full_path, newline = '', encoding="utf-8") as csvfile:
        data = csv.DictReader(csvfile)
        if not_empty(data):
            doc_id += 1
            #doc_id_name.update({doc_id:full_path})
            doc_id_name[doc_id] = full_path
            terms = pre_processing(data)
            #print(type(data))
            terms = sorted(terms)
            dictionary = dict(Counter(terms))   #dictionary of all terms in a csv with respective frequencies
            # if doc_id == 1:
            #     #ii_tree.update(inverted_index)
            #     #print(inverted_index)
            #     break
            
            #creation ofn inverted index
            for term in dictionary.keys():
                if term not in inverted_index.keys():
                    inverted_index[term] = [ dictionary[term], [doc_id] ]    
                else:
                    inverted_index[term][0] += dictionary[term]
                    inverted_index[term][1].append(doc_id)
            #print(inverted_index)

            # if doc_id == 418:
            #     #ii_tree.update(inverted_index)
            #     break
end1 = time.time()
print("The total indexing time taken is ", end1 - start1, " seconds")
#QUERYING

#input query 


query = str(input('Enter your Query:')) 
start = time.time()
query_string = query 
#if or present 
if " or " in query:
    qtokens = tokenizer.tokenize(query)             #tokenize query
    stop_word = stop_words - {"or"}
    filtered_query = [word for word in qtokens if not word in stop_word]    #remove stopwords other than or
    #print(filtered_query)
    query_terms = []
    for word in filtered_query:
        query_terms.append(ps.stem(word))           #perform stemming
    #print(query_terms)
    query_terms = ' '.join(query_terms)     
    refined_query = query_terms             #original query string without stopwords
    #print(query_terms)
    split = query_terms.split(' or ')             #split based on or
    or_phrases = split                            #list of query phrases/words to or
    to_or = []                                    #list of posting lists to or
    
    for phrase in split: 
        tokens = tokenizer.tokenize(phrase)       #tokenize the phrase to consider each phrase as a separate query
        sub_query = list(tokens)
        #print(sub_query)
        sub_postinglist = merge(sub_query)  #posting list of subquery
        #print(sub_postinglist)
        to_or.append(sub_postinglist)           #to_or consists of all sub query posting lists which need to be or'ed
    #print(to_or)
    result = []
    iteration = 0
    for posting_list in to_or:
        if iteration == 0:
            result = posting_list
            iteration += 1
            #print(result)
            continue
        temp = union(result,posting_list)
        iteration += 1
        result = temp
        #print(result)
    final_ps = result
    #print(final_ps)

#if or absent then simply merge
else:
    qtokens = tokenizer.tokenize(query)                 #tokenize query
    filtered_query = [word for word in qtokens if not word in stop_words]   #remove stopwords from query
    #print(filtered_query)
    query_terms = []
    for word in filtered_query:
        query_terms.append(ps.stem(word))                   #stemming query
    #print(query_terms)

    refined_query = ' '.join(query_terms)
    query_terms = sorted(query_terms)
    #print(query_terms)
    final_ps = merge(query_terms)                            #applying simple merge function
    #print(final_ps)



#VECTORIZER

corpus = []
#mapping = {}
#final_terms = cleaning(query_string)

#corpus creation 
for doc_id in final_ps:
    #print(doc)
    with open(doc_id_name[doc_id], newline = '', encoding="utf-8") as csvfile:
        #print(doc_id_name[doc_id])
        data = csv.DictReader(csvfile)
        
        if not_empty(data):
            terms = pre_processing(data)
            #print(terms)
            doc_text = ' '.join(terms)
            #print(doc_text)
            corpus.append(doc_text)

#print(corpus)

X = vectorizer.fit_transform(corpus)
#print(X)
df = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names())
#print(df)
#print(refined_query)
query_vec = vectorizer.transform([refined_query])
#print(query_vec)
similarity = cosine_similarity(X,query_vec).reshape((-1))
#print(similarity)
dict_similarity = dict( zip(similarity,final_ps))
#print(dict_similarity)
top_ten = {}
count = 0

for key in sorted(dict_similarity, reverse = True):
    if count < 10:
        top_ten[key] = dict_similarity[key]     #assigns doc_id (value) to score (key)
        count += 1
#print(sorted_dict)



#OUPUT

for score, doc_id in top_ten.items():
    #print(top_ten[key], doc_id_name[top_ten[key]], key)     #prints doc_id, path, score
    #print(score)
    #print('\n***************\n')
    #print(mapping[doc_id][row_index], '\n***************\n')
    #print(mapping[doc_id])
    get_row_details(doc_id,query_string,score)

end = time.time()
total_time = end - start
print("The total querying time taken is ", total_time, " seconds")