from gensim.models import Word2Vec, doc2vec
import pandas as pd

model = Word2Vec.load("w400-5-5-model")

model.most_similar(['mordhau'],topn = 8)
model.most_similar(['dota'],topn = 8)
model.most_similar(['detention'],topn = 8)   
model.most_similar(['ark'],topn = 8)  

models = doc2vec.Doc2Vec.load("d2v_weights")

models.wv.similar_by_word('good')

data = pd.read_csv('allreviews.csv')

url_prefix = 'https://store.steampowered.com/app/'
for idx, value in enumerate(recom):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))

tokens = "best FPS game".split()
new_vector = models.infer_vector(tokens)
sims = models.docvecs.most_similar([new_vector])

for idx, value in enumerate(sims):
    print(data.iloc[value[0], 8], ':', value[1])
    
    
sims = models.docvecs.most_similar([new_vector])

appid_ = 629760
# mordhau
recom = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0])
for idx, value in enumerate(recom):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))
    
appid_ = 219740
recom = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0])
for idx, value in enumerate(recom):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))


recom2 = models.docvecs.most_similar(2368)
for idx, value in enumerate(recom2):
    print(data.iloc[value[0], 8], ':', value[1])
    

# ghost recon wildland 
data.query('appid == 460930')
recom3 = models.docvecs.most_similar(1438)
for idx, value in enumerate(recom3):
    print(data.iloc[value[0], 8], ':', value[1])


data.query('appid == 555220')




appid_ = 644560
url_prefix = 'https://store.steampowered.com/app/'
# mirrior 644560
recom2 = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0])
for idx, value in enumerate(recom2):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))
    
