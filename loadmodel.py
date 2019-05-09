from gensim.models import doc2vec
import pandas as pd

def game_recommadation(appid_):
    '''
    給定 steam appid，返回推薦的遊戲名稱與網址
    Example:
        https://store.steampowered.com/app/629760/MORDHAU/
        appid_ = 629760
    '''
    try:
        recom = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0])
        for idx, value in enumerate(recom):
            print(data.iloc[value[0], 8], ':', value[1])
            print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))
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


models.wv.similar_by_word('good', topn=7)
models.wv.similar_by_word('fun', topn=7)
models.wv.similar_by_word('loli', topn=10)


