import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models import doc2vec

def sentence_tokenize(article):
    # transfer article into sentence list
    sent_tokenize_list = sent_tokenize(article)
    sent_list = [x.lower() for x in sent_tokenize_list]
    return sent_list


idname = pd.read_csv('applist_name.csv', encoding='utf-8')
idname['appname'] = idname['appname'].astype(str).str.lower()

data = pd.read_csv('allreviews.csv', encoding='utf-8')
data = data.merge(idname, on='appid', how='left')
data = data.drop_duplicates(subset='appname').reset_index(drop=True)
data.to_csv('allreviews.csv', index=None, encoding='utf-8')



stop_words = set(stopwords.words('english'))

trainD2v = []
n = 0
for row in data['allReviews']:
    sentenceList = []
    sentences = sentence_tokenize(row)
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word in words:
            word = word.replace('\\n', ' ').replace('\n', ' ').strip()
            word = re.sub(r'[^\w]', '',word)
            if word not in stop_words:
                if len(word) > 1:
                    sentenceList.append(word)
                    
    trainD2v.append(doc2vec.TaggedDocument(sentenceList, [n]))
    n += 1
    

d2vmodel = doc2vec.Doc2Vec(trainD2v, vector_size=100, window=5, min_count=3, workers=6)

output_name='d2v_weights_new'
d2vmodel.save(output_name) 