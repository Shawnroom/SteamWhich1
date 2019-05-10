from gensim.models import doc2vec
import pandas as pd
import webbrowser

def game_recommadation(appid_):
    '''
    給定 steam appid，返回推薦的遊戲名稱與網址
    Example:
        https://store.steampowered.com/app/629760/MORDHAU/
        appid_ = 629760
    '''
    try:
        webbrowser.open(url_prefix+str(appid_), new=0, autoraise=True)
        recom = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0], topn=5)
        for idx, value in enumerate(recom):
            print(data.iloc[value[0], 8], ':', round(value[1], 2))
            webbrowser.open(url_prefix+str(data.iloc[value[0], 0]), new=0, autoraise=True)
    except IndexError:
        print('This game is not in training data.')


data = pd.read_csv('allreviews.csv', encoding='utf-8')
url_prefix = 'https://store.steampowered.com/app/'

models = doc2vec.Doc2Vec.load("d2v_weights_new")

# mordhau
game_recommadation(629760)

# pix ark
game_recommadation(593600)

#mirror
game_recommadation(644560)

#magica 2
game_recommadation(238370)



models.wv.similar_by_word('good', topn=7)
models.wv.similar_by_word('casino', topn=7)
models.wv.similar_by_word('loli', topn=10)



tokens ="i dont have money, but i want to be a millionair".split()
new_vector = models.infer_vector(tokens)
sims = models.docvecs.most_similar([new_vector], topn=5)
for idx, value in enumerate(sims):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))
    
