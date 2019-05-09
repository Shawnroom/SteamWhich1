# SteamWhich1
Steam content-based recommendation system 


# 操作流程
**1. 爬網站 & 擷取資訊**：透過 requests爬取 steam API資訊。存取每個遊戲的評論到 csv檔。

執行`python steamParser.py`

**2. 文字預處理**：使用 nltk與 re對文字進行預處理。

執行`python wordPreprocess.py`

**3. 訓練**：透過在 gensim 中實作的 Doc2Vec，設定參數對資料進行訓練，產生詞向量與模型。

執行`python modelTrain.py`

**4. 使用**：調用模型權重，輸入英文詞彙或 steam appid，推薦對應的遊戲。

執行`loadModel.py`


# 專案成果
本次共訓練 5899 個遊戲評論，訓練結果為 100維詞向量。由於訓練數量蠻小的，所以訓練速度很快。

1. 先載入 gensim 套件與剛剛訓練好的 model
```python
from gensim.models import doc2vec
# load fresh model
models = doc2vec.Doc2Vec.load("d2v_weights")
```
接下來就可以開始玩啦！關於好遊戲，玩家們除了 good之外還會用哪些形容詞呢？
```python
models.wv.similar_by_word('good', topn=7)
[('decent', 0.8043760061264038),
 ('great', 0.7898209691047668),
 ('gamegood', 0.7109229564666748),
 ('nice', 0.697540819644928),
 ('awesome', 0.6696457862854004),
 ('fantastic', 0.655768632888794),
 ('excellent', 0.6513001322746277)]
```
我很喜歡玩 Ark這個遊戲，有哪些詞語跟 Ark相似呢？
```python
models.wv.similar_by_word('ark', topn=7)
[('evolved', 0.7574654817581177),
 ('subnautica', 0.6752661466598511),
 ('terraria', 0.6497236490249634),
 ('rust', 0.6383152008056641),
 ('exiles', 0.6306138038635254),
 ('kairosoft', 0.6045154333114624),
 ('fittest', 0.599312424659729)]
```
從結果中可以發現有 3個結果不是遊戲名稱，如果我只想知道與 Ark相似的遊戲，可以使用
```python
# steam商店中的 appid
appid_ = 593600
# PixelArk
recom = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0])
for idx, value in enumerate(recom):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))

citadel: forged with fire : 0.8330956697463989
Steam商店頁面: https://store.steampowered.com/app/487120
dark and light : 0.8013544678688049
Steam商店頁面: https://store.steampowered.com/app/529180
metatron : 0.7723658084869385
Steam商店頁面: https://store.steampowered.com/app/454680
conan exiles : 0.7697832584381104
Steam商店頁面: https://store.steampowered.com/app/440900
stranded deep : 0.7561972141265869
Steam商店頁面: https://store.steampowered.com/app/313120
ylands : 0.7502149939537048
Steam商店頁面: https://store.steampowered.com/app/298610
valnir rok : 0.7472282648086548
Steam商店頁面: https://store.steampowered.com/app/658980
the wild eight : 0.7458113431930542
Steam商店頁面: https://store.steampowered.com/app/526160
chkn : 0.7420089244842529
Steam商店頁面: https://store.steampowered.com/app/420930
animallica : 0.7305570840835571
Steam商店頁面: https://store.steampowered.com/app/638850
```

