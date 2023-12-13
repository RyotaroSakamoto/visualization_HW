import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.rcParams["font.family"] = "Meiryo"

st.title("棒グラフの作成")

st.subheader("1.グラフ作成のためのデータを取得する")

"""
 JPX日本取引所グループが公開している統計資料を使用する
[JPX その他統計資料](https://www.jpx.co.jp/markets/statistics-equities/misc/01.html)  
今回は17業種区分別の上場企業の分布を棒グラフを用いて可視化する。  
今回使用するデータは事前にエクセル上で前処理を行っている。
"""


st.subheader("2.データの読み込み")


"""
csvデータを読み込む
```python
#ライブラリの読み込み
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Meiryo"

#データの読み込み
df = pd.read_csv("data/上場企業.csv")

#データの確認
df.head()
```

"""
#データの読み込み
df = pd.read_csv("pages/data/上場企業.csv")

#データの確認
st.write(df.head())


st.subheader("2.基本的な棒グラフの作成")

"""
読み込んだデータを17業種区分ごとに集計し、グラフを作成する。
```python
17業種区分ごとの企業数をカウント
# class_count = df["17業種区分"].value_counts()

#棒グラフを作成
plt.bar(class_count.index, class_count)
plt.show()

"""
class_count = df["17業種区分"].value_counts()

#棒グラフを描画
fig = plt.figure()
ax = fig.add_subplot()
ax.bar(class_count.index, class_count)
plt.show()
st.pyplot(fig)


"""
このままだとラベルが重なって見づらい。.bar()ではなく.barh()を使用して横棒グラフを作成してみる。
```python
#横棒グラフを作成
plt.barh(class_count.index, class_count)
plt.show()
```
"""
fig = plt.figure()
ax = fig.add_subplot()
ax.barh(class_count.index, class_count)
plt.show()
st.pyplot(fig)

"""
数が多い方を上にしたいので、集計したリストを逆順にして再度グラフを作成。
```python
#リストを並べ替え
class_count.sort_values(inplace=True)
#横棒グラフを作成
plt.barh(class_count.index, class_count)
plt.show()
```
"""
class_count.sort_values(inplace=True)
fig = plt.figure()
ax = fig.add_subplot()
ax.barh(class_count.index, class_count)
plt.show()
st.pyplot(fig)


st.subheader("2.棒グラフの設定の変更")

"""
折れ線グラフと同じように、引数を指定することによってグラフの設定を変えることができる。

```python
#色を指定するリストを作成
c_list = ["gray"] * len(class_count)
c_list[-1] = "red"

#横棒グラフを作成
plt.barh(class_count.index, class_count, color=c_list) #色を指定する引数にリストを渡す
ax.set_xlabel("企業数") #x軸ラベルの追加
ax.set_title("17業種区分ごとの上場企業の分布") #グラフタイトルの設定
plt.show()
```
"""
c_list = ["gray"] * len(class_count)
c_list[-1] = "red"
class_count.sort_values(inplace=True)
fig = plt.figure()
ax = fig.add_subplot()
ax.barh(class_count.index, class_count,color=c_list)
ax.set_xlabel("企業数") #x軸ラベルの追加
ax.set_title("17業種区分ごとの上場企業の分布") #グラフタイトルの設定
plt.show()
st.pyplot(fig)

