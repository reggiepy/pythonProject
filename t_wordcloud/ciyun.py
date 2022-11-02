# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/10/27 16:13
import numpy as np
from PIL import Image
from wordcloud import WordCloud

mask = np.array(Image.open("Alice.png"))

f = open('Alice.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()
wordcloud = WordCloud(background_color="white",
                      width=800,
                      height=600,
                      max_words=200,
                      max_font_size=80,
                      mask=mask,
                      contour_width=3,
                      contour_color='steelblue',
                      font_path="msyh.ttc"
                      ).generate(txt)
wordcloud.to_file('Alice_词云图.png')
