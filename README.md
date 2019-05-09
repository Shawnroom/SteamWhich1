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
接下來就可以開始玩啦！關於糟糕的遊戲，玩家們除了 bad之外還會用哪些形容詞呢？
```python
models.wv.similar_by_word('bad')

[('terrible', 0.746313214302063),
 ('awful', 0.6867302656173706),
 ('horrible', 0.683438777923584),
 ('poor', 0.659858226776123),
 ('shitty', 0.6323168277740479),
 ('crappy', 0.6310047507286072),
 ('good', 0.6165034174919128),
 ('badnnit', 0.5917258858680725),
 ('sucks', 0.5883899927139282),
 ('abysmal', 0.5872944593429565)]
```
