import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
plt.rcParams["font.family"] = "Meiryo"

st.title("ヒストグラムの作成")
st.subheader("1.データの読み込みと前処理")


"""
[独立行政法人 統計センターのデータセット](https://www.nstac.go.jp/use/literacy/ssdse/?doing_wp_cron=1701946791.2452630996704101562500#SSDSE-A)を使い、都道府県別の推定人口のヒストグラムを作成する。

```python
#データの読み込みと前処理
df = pd.read_csv("data/SSDSE-D-2021.csv", encoding="cp932", skiprows=1)
df = df.query("男女の別 =='0_総数' and 都道府県 != '全国'")
df = df[["都道府県","推定人口（10歳以上）"]]

#データの確認
df.head()
```

"""

#データの読み込みと前処理
df = pd.read_csv("pages/data/SSDSE-D-2021.csv", encoding="cp932", skiprows=1)
df = df.query("男女の別 =='0_総数' and 都道府県 != '全国'")
df = df[["都道府県","推定人口（10歳以上）"]]
st.write(df.head())


st.subheader("2.基本的なヒストグラムの作成")


"""
読み込んだデータを用いてヒストグラムを作成する
```python
fig = plt.figure()
ax = fig.add_subplot()
ax.hist(df["推定人口（10歳以上）"])
plt.show()
```
"""
fig = plt.figure()
ax = fig.add_subplot()
ax.hist(df["推定人口（10歳以上）"])
plt.show()
st.pyplot(fig)



st.subheader("3.ヒストグラムの設定の変更")

"""
ヒストグラムも、他のグラフと同様に.hist()メゾッドのオプションを設定することができる。  
ここからはダイスロールのシミュレーションを行い、その結果をヒストグラムで描画する。
サイドバーからシミュレーションの設定を変更することもできる
"""
#ハイパーパラメーターを設定
st.sidebar.markdown("# ダイスロールシミュレーションの設定")
n = st.sidebar.slider("試行回数を設定して下さい",1,1000,1000,1)
trial_label = [1,2,3,4,5,6,8,10,12,15,18,24,100]
trial = st.sidebar.selectbox("一度に投げるダイスの数",trial_label, index=2)
dice_num_label = [1,2,3,4,5,6,7,8,9,10,12,50,66,100]
dice_num = st.sidebar.selectbox("ダイスの目の最大数",dice_num_label, index=5)
result = np.array([])

#ハイパーパラメーターを元に試行を実行
for i in range(n):
    dices = np.zeros(trial)
    for dice in range(trial):
        x = np.random.randint(1,dice_num+1)
        dices[dice] = x
    dice_res = dices.sum()
    result = np.append(result, dice_res)


#各種統計量を計算
res_m = np.mean(result).round(2)
res_std = np.std(result).round(2)
res_med = np.median(result).round(2)
res_var = np.var(result).round(2)


#統計量の平均と分散を元に正規分布のデータを作成
x = np.arange(trial,dice_num*trial,0.1)
y = scipy.stats.norm.pdf(x,res_m, res_std)


#試行結果の描画
fig, ax1 = plt.subplots()


#選択式でグラフの描画設定を可変にする
ny = ["no","yes"]
yn = ["yes","no"]
setting = st.sidebar.radio("グラフの詳細設定を行いますか?",ny)
if setting == "yes":
    hist_c_r = st.sidebar.slider("Histgram RGB_red",0,255,0)
    hist_c_g = st.sidebar.slider("Histgram RGB_green",0,255,0)
    hist_c_b = st.sidebar.slider("Histgram RGB_blue",0,255,255)
    hist_color = (hist_c_r / 255, hist_c_g / 255, hist_c_b / 255)
    plot_c_r = st.sidebar.slider("lineplot RGB_red",0,255,255)
    plot_c_g = st.sidebar.slider("lineplot RGB_green",0,255,0)
    plot_c_b = st.sidebar.slider("lineplot RGB_blue",0,255,0)
    plot_color = (plot_c_r / 255, plot_c_g / 255, plot_c_b / 255)
    grid_setting_flag = st.sidebar.radio("グリッド線を表示する",ny)
    norm_plot_flag = st.sidebar.radio("正規分布のグラフを表示する",yn)


#初期描画設定
else:
    hist_color = (0,0,1)
    plot_color = (1,0,0)
    norm_plot_flag = "yes"
    grid_setting_flag = "no"


#各種統計量を表示
st.write("\n\n")
st.markdown(f"### 結果の基本統計量")
st.markdown(f"平均値:{res_m}")
st.markdown(f"中央値:{res_med}")
st.markdown(f"分散:{res_var}")
st.markdown(f"標準偏差:{res_std}")


#グラフをプロット
ax1.hist(result,bins=np.count_nonzero(np.unique(result)), label="出現数", alpha=0.7, color=hist_color)

#詳細設定でnoを選択しなかった場合、正規分布のグラフをプロットする
if norm_plot_flag == "yes" : 
    ax2 = ax1.twinx()
    ax2.plot(x,y,label="Norm", alpha=0.7, color=plot_color)
    ax2.set_ylabel(f'正規分布(μ={res_m},σ={res_var})', color=plot_color)
    ax2.set_ylim(bottom=0)

ax1.set_ylabel(f'出現回数(n={n})', color=hist_color)
ax1.set_ylim(bottom=0)
plt.title(f"{trial}d{dice_num}ダイスシミュレーション")
if grid_setting_flag == "yes": plt.grid(axis="both")
plt.show()
st.pyplot(fig)


"""
以下が、streamlit上で値を変更しながらシミュレーションとグラフ作成をできるようにしたコードである。
```python
#ハイパーパラメーターを設定
n = st.slider("試行回数を設定して下さい",1,1000,1000,1)
trial_label = [1,2,3,4,5,6,8,10,12,15,18,24,100]
trial = st.selectbox("一度に投げるダイスの数",trial_label, index=2)
dice_num_label = [1,2,3,4,5,6,7,8,9,10,12,50,66,100]
dice_num = st.selectbox("ダイスの目の最大数",dice_num_label, index=5)
result = np.array([])

#ハイパーパラメーターを元に試行を実行
for i in range(n):
    dices = np.zeros(trial)
    for dice in range(trial):
        x = np.random.randint(1,dice_num+1)
        dices[dice] = x
    dice_res = dices.sum()
    result = np.append(result, dice_res)


#各種統計量を計算
res_m = np.mean(result).round(2)
res_std = np.std(result).round(2)
res_med = np.median(result).round(2)
res_var = np.var(result).round(2)


#統計量の平均と分散を元に正規分布のデータを作成
x = np.arange(trial,dice_num*trial,0.1)
y = scipy.stats.norm.pdf(x,res_m, res_std)


#試行結果の描画
fig, ax1 = plt.subplots()


#選択式でグラフの描画設定を可変にする
ny = ["no","yes"]
yn = ["yes","no"]
setting = st.radio("グラフの詳細設定を行いますか?",ny)
if setting == "yes":
    hist_c_r = st.slider("Histgram RGB_red",0,255,0)
    hist_c_g = st.slider("Histgram RGB_green",0,255,0)
    hist_c_b = st.slider("Histgram RGB_blue",0,255,255)
    hist_color = (hist_c_r / 255, hist_c_g / 255, hist_c_b / 255)
    plot_c_r = st.slider("lineplot RGB_red",0,255,255)
    plot_c_g = st.slider("lineplot RGB_green",0,255,0)
    plot_c_b = st.slider("lineplot RGB_blue",0,255,0)
    plot_color = (plot_c_r / 255, plot_c_g / 255, plot_c_b / 255)
    grid_setting_flag = st.radio("グリッド線を表示する",ny)
    norm_plot_flag = st.radio("正規分布のグラフを表示する",yn)


#初期描画設定
else:
    hist_color = (0,0,1)
    plot_color = (1,0,0)
    norm_plot_flag = "yes"
    grid_setting_flag = "no"


#各種統計量を表示
st.write(f"平均値:{res_m}")
st.write(f"中央値:{res_med}")
st.write(f"分散:{res_var}")
st.write(f"標準偏差:{res_std}")


#グラフをプロット
ax1.hist(result,bins=np.count_nonzero(np.unique(result)), label="出現数", alpha=0.7, color=hist_color)

#詳細設定でnoを選択しなかった場合、正規分布のグラフをプロットする
if norm_plot_flag == "yes" : 
    ax2 = ax1.twinx()
    ax2.plot(x,y,label="Norm", alpha=0.7, color=plot_color)
    ax2.set_ylabel(f'正規分布(μ={res_m},σ={res_var})', color=plot_color)

ax1.set_ylabel(f'出現回数(n={n})', color=hist_color)
ax1.set_ylim(bottom=0)
ax2.set_ylim(bottom=0)
plt.title(f"{trial}d{dice_num}ダイスシミュレーション")
if grid_setting_flag == "yes": plt.grid(axis="both")
plt.show()
st.pyplot(fig)

```





"""