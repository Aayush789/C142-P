import csv 
all_articles = []

with open('articls.csv', encoding = "utf-8") as f:
    reader = csv.reader(f)
    data = list(reader) 
    all_articls = data[1:]

liked_articles = []

not_liked_articles = []
