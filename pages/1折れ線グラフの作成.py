import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Meiryo"
import yfinance as yf
import pandas_datareader as pdr
yf.pdr_override()
import warnings
warnings.simplefilter('ignore')


# タイトル表示
st.title("折れ線グラフの作成")
st.subheader("1.折れ線グラフに使用するデータを取得する")


"""
```python
#株価取得に使用するパッケージのインポートと設定
import pandas as pd
import yfinance as yf
import pandas_datareader as pdr
yf.pdr_override()

#ゲーム会社の株情報取得
nintendo = pdr.data.DataReader("7974.T", start, end) #任天堂
sony = pdr.data.DataReader("6758.T", start, end) #ソニー
bandai = pdr.data.DataReader("7832.T", start, end) #バンダイナムコ
sega = pdr.data.DataReader("6460.T", start, end) #セガ

#データの確認
nintendo.head()
```
"""
# yfinance,pandas_datareaderで株情報取得したものを用意(軽量化のため)


# それぞれの会社の株情報取得
nintendo = pd.read_csv("pages/data/nintendo.csv")
sony = pd.read_csv("pages/data/sony.csv")
bandai = pd.read_csv("pages/data/bandai.csv")
sega = pd.read_csv("pages/data/sega.csv")
#dfの表示
st.write(nintendo.head())


st.write("\n")
st.write("\n")
st.write("\n")

st.subheader("2.簡単なグラフの作成")
"""
 pyplotインターフェースを使ってグラフを作成する
```python
#パッケージのインポートとフォント設定
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Meiryo"

#pyplotインターフェースを使って作成
plt.plot(nintendo["Close"])
plt.show()
```
"""
fig = plt.figure()
ax = fig.add_subplot(1,1,1,)
ax.plot(nintendo["Close"])
plt.show()
st.pyplot(fig)


"""
 次にオブジェクト指向インターフェースを使ってグラフを作成する  
オブジェクト指向インターフェースを使用する場合、複雑なグラフを作ったり、微調整することができる

```python

#pyplotインターフェースを使って作成
plt.plot(nintendo["Close"])
plt.show()
```

"""
fig = plt.figure()
ax = fig.add_subplot(1,1,1,)
ax.plot(nintendo["Close"])
plt.show()
st.pyplot(fig)

#改行
for _ in range(5):
    st.write("\n")

st.subheader("3.複雑なグラフの作成")

"""
 オブジェクト指向インターフェースを使い、複雑なグラフを作成する。  
.figure()関数でfigureインスタンスを呼び出し.add_subplot()メゾッドでAxesクラスのインスタンスを作成。定義された領域に作図メゾッドを使用してグラフを作成する。

```python
#描画領域とグラフエリアの作成
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

#グラフの描画
ax1.plot(nintendo["Close"])
ax2.plot(sony["Close"])
ax3.plot(bandai["Close"])
ax4.plot(sega["Close"])
plt.show()
```
"""
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.plot(nintendo["Close"])
ax2.plot(sony["Close"])
ax3.plot(bandai["Close"])
ax4.plot(sega["Close"])

plt.show()
st.pyplot(fig)

"""
 複数のグラフを一枚にまとめたければ、作画メゾッドを繰り返せば良い。  
また.plot()メゾッドのオプション引数を指定することによって、複雑な表現ができる。
```python
fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554")
ax.plot(sony["Close"], linestyle="--" ,marker="o",c="#003087")
ax.plot(bandai["Close"], linestyle=":", marker="*",c="#ff5c00")
ax.plot(sega["Close"],marker="s",c="#17569b")
plt.show()
```
"""
# それぞれの株価を重ねて表示
fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554")
ax.plot(sony["Close"], linestyle="--" ,marker="o",c="#003087")
ax.plot(bandai["Close"], linestyle=":", marker="*",c="#ff5c00")
ax.plot(sega["Close"],marker="s",c="#17569b")
plt.show()
st.pyplot(fig)


"""
 複数のグラフがある場合.legend()メゾッドを使えば、凡例を表示することができる

```python
fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554", label="任天堂") #ラベル設定を追加
ax.plot(sony["Close"],c="#003087", label="ソニー")
ax.plot(bandai["Close"],c="#ff5c00", label="バンダイナムコ")
ax.plot(sega["Close"],c="#17569b", label="セガ")
plt.legend(loc="upper right", shadow=True) #凡例の描画設定
plt.show()
```
"""
fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554", label="任天堂") #ラベル設定を追加
ax.plot(sony["Close"],c="#003087", label="ソニー")
ax.plot(bandai["Close"],c="#ff5c00", label="バンダイナムコ")
ax.plot(sega["Close"],c="#17569b", label="セガ")
plt.legend(loc="upper left", shadow=True)
plt.show()
st.pyplot(fig)

"""
 軸ラベルを加えたりメモリに装飾を加えたりするには、subplotオブジェクトにメゾッドを加える。
```python
fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554", label="任天堂")
ax.plot(sony["Close"],c="#003087", label="ソニー")
ax.plot(bandai["Close"],c="#ff5c00", label="バンダイナムコ")
ax.plot(sega["Close"],c="#17569b", label="セガ")
plt.legend(loc="upper left", shadow=True)
ax.set_xlabel("2017年から2022年までの株価の推移") #x軸ラベル
ax.set_ylabel("株価") #y軸ラベル
ax.grid() #グリッド線の追加
plt.show()
```
"""

fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554", label="任天堂")
ax.plot(sony["Close"],c="#003087", label="ソニー")
ax.plot(bandai["Close"],c="#ff5c00", label="バンダイナムコ")
ax.plot(sega["Close"],c="#17569b", label="セガ")
plt.legend(loc="upper left", shadow=True)
ax.set_xlabel("2017年から2022年までの株価の推移")
ax.set_ylabel("株価")
ax.grid()
plt.show()
st.pyplot(fig)

"""
 x軸のメモリが日付情報になっていないので、pandasからindexの型を時系列に変換し、最後にタイトルを設定する。
 

```python
#indexをdatetime型に変換する
nintendo.index = pd.to_datetime(nintendo)
sony.index = pd.to_datetime(sony)
bandai.index = pd.to_datetime(bandai)
sega.index = pd.to_datetime(sega)

fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554", label="任天堂")
ax.plot(sony["Close"],c="#003087", label="ソニー")
ax.plot(bandai["Close"],c="#ff5c00", label="バンダイナムコ")
ax.plot(sega["Close"],c="#17569b", label="セガ")
plt.legend(loc="upper left", shadow=True)
ax.set_xlabel("2017年から2022年までの株価の推移") #x軸ラベル
ax.set_ylabel("株価") #y軸ラベル
ax.grid() #グリッド線の追加
ax.set_title("主要ゲーム会社の株価価格の推移") #タイトルの設定
plt.show()
st.pyplot(fig)

"""
#整合性を合わせるためのindex設定
nintendo.set_index("Date", inplace=True)
sony.set_index("Date", inplace=True)
bandai.set_index("Date", inplace=True)
sega.set_index("Date", inplace=True)
nintendo.index = pd.to_datetime(nintendo.index)
sony.index = pd.to_datetime(sony.index)
bandai.index = pd.to_datetime(bandai.index)
sega.index = pd.to_datetime(sega.index)

fig = plt.figure()
ax = plt.subplot()
ax.plot(nintendo["Close"],c="#FF4554", label="任天堂")
ax.plot(sony["Close"],c="#003087", label="ソニー")
ax.plot(bandai["Close"],c="#ff5c00", label="バンダイナムコ")
ax.plot(sega["Close"],c="#17569b", label="セガ")
plt.legend(loc="upper left", shadow=True)
ax.set_xlabel("2017年から2022年までの株価の推移") #x軸ラベル
ax.set_ylabel("株価") #y軸ラベル
ax.grid() #グリッド線の追加
ax.set_title("主要ゲーム会社の株価価格の推移")
plt.show()
st.pyplot(fig)

