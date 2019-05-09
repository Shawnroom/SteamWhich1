# SteamWhich1
這是一個基於 word2vec的 steam遊戲推薦系統

# 專案緣起
身為一個 Steam的重度玩家，每次特價時總會想買點遊戲，但又懶得花時間研究= =。所以想做個推薦模型來幫助我花錢(荷包君表示QQ)

# 操作流程
**1. 爬網站 & 擷取資訊**：透過 requests爬取 steam API資訊。存取每個遊戲的評論到 csv檔。

執行`python steamParser.py`

**2. 訓練**：透過在 gensim 中實作的 Doc2Vec，設定參數對資料進行訓練，產生詞向量與模型。

執行`python modelTrain.py`

**3. 使用**：調用模型權重，輸入英文詞彙或 steam appid，推薦對應的遊戲。

執行`loadModel.py`


# 專案成果
本次共訓練 5983個遊戲的 20-100則評論，訓練結果為 100維詞向量。由於訓練數量蠻小的，所以訓練速度很快。

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
# PixArk
recom = models.docvecs.most_similar(data.query('appid == @appid_').index.values[0])
for idx, value in enumerate(recom):
    print(data.iloc[value[0], 8], ':', value[1])
    print('Steam商店頁面:', url_prefix+str(data.iloc[value[0], 0]))
```
整理一下結果為 :
- [citadel: forged with fire](https://store.steampowered.com/app/487120) : 0.833
- [dark and light](https://store.steampowered.com/app/529180) : 0.801
- [metatron](https://store.steampowered.com/app/454680) : 0.772
- [conan exiles](https://store.steampowered.com/app/440900) : 0.769
- [stranded deep](https://store.steampowered.com/app/313120) : 0.756
- [ylands](https://store.steampowered.com/app/298610) : 0.750
- [valnir rok](https://store.steampowered.com/app/658980) : 0.747
- [the wild eight](https://store.steampowered.com/app/526160) : 0.745
- [chkn](https://store.steampowered.com/app/420930) : 0.742
- [animallica](https://store.steampowered.com/app/638850) : 0.730


# 未來方向
- 改善 SteamParser language參數失效問題，提升遊戲數與個別評論數，模型成果應該會更好
- 新增繁中模型(有些遊戲以華人為主)
- 優化文字預處理
- 依照評論的推薦度給予不同權重(因人廢言)
- 新增依照意境推薦遊戲的功能
