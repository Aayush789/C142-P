from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd 
import numpy as np
import statistics 

df = pd.read_csv("articles.csv")

C = df['vote_average'].mean()

m = df['vote_count'].quantile(0.9)

total_events = df.copy().loc[df['vote_count']>=m]

def weighted_rating(x,m = m,C = C ):
  v = x['vote_count']
  R = x['vote_average']
  return (v/(v+m)*R) + (m/(m+v)*C)

total_events['score'] = total_events.apply(weighted_rating, axis = 1)

total_events = total_events.sort_values('score', ascending = False)
output = total_events[['eventType,contentId,authorPersonId,authorSessionId,authorUserAgent,authorRegion,authorCountry,contentType,url,title,text,lang,total_events']].head(20).values.tolist()

