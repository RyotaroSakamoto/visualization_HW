import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.rcParams["font.family"] = "Meiryo"
from PIL import Image

st.title("可視化の技術 課題")
file_path = "image/title_image.png"
img = Image.open(file_path)
st.image(img)
"""
制作者: 東京テクニカルカレッジ データサイエンス+AI科\n
坂本凌太朗

画像: [Stable Diffusion](https://dreamstudio.ai)
"""