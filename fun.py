import csv
import os
from elasticsearch import Elasticsearch , helpers
import pandas as pd 
es=Elasticsearch([{'host':'localhost','port':9200}])
import time 
 from sklearn.metrics import precision_recall_fscore_support

#print(es)
totaldocs = 0


for dirname, _, filenames in os.walk("C:\\Users\\pbhav\\Desktop\\Finale\\AIR\\Project\\TelevisionNews"):
    for filename in filenames:
        file_name = os.path.join(dirname,filename)
        #print(file_name)
        totaldocs+=1
        df = pd.read_csv(file_name ,delimiter =',' , nrows = None , error_bad_lines=False)
        #print(df)
        for ind,row in df.iterrows():
            Body ={
                "URL": str(row["URL"]),
                "MatchDateTime" : str(row["MatchDateTime"]),
                "Station" : str(row["Station"]),
                "Show": str(row["Show"]),
                "IAShowID" : str(row["IAShowID"]),
                "IAPreviewThumb" : str(row["IAPreviewThumb"]),
                "Snippet" : str(row["Snippet"])
            }
            #print(Body)
            Id = str(filename) + str(ind)
            res = es.index(index="air_index" , id = Id , body = Body)
            #print(res)
        print(totaldocs)
        # rs=es.get(index='air_index',id=Id)
        # print (rs)

        rs=es.search(index='air_index', body={'query':{'match_phrase' : {"Snippet" :"climate change" }} } )
        for hit in rs['hits']['hits']:
            print (hit['_source']['Snippet'])
            print (hit['_score']) 
            #print '**********************'

        if(totaldocs ==418):
            break


print(totaldocs)

'''
for dirname, _, filenames in os.walk("C:\\Users\\pbhav\\Desktop\\Finale\\AIR\\Project\\TelevisionNews"):
    for filename in filenames:
        file_name = os.path.join(dirname,filename)
        df = pd.read_csv(file_name ,delimiter =',' , nrows = None , error_bad_lines=False)
        for ind,row in df.iterrows():

'''