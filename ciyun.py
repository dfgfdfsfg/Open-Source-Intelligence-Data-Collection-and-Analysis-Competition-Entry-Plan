import re
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import colors
import csv
import pandas as pd

excelFilename = 'H列'


def wordFrequency():
    file_path = r"D:\86184\pachong\019+初赛环节3\019+初赛环节3+源数据\社交媒体微博数据集.csv"
    data = pd.read_csv(file_path)
    data_now = data['微博正文']
    data_now = data_now.dropna().to_string()

    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
    string_data = re.sub(pattern, '', data_now)

    seg_list_exact = jieba.cut(string_data, cut_all=False)
    object_list = []

    stopwords = set()
    with open('中文停用词表.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip())

    with open('cn_stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip())

    with open('hit_stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip())

    with open('scu_stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip())

    for word in seg_list_exact:

        if word not in stopwords:
            if len(word) > 2:
                object_list.append(word)

    word_counts = collections.Counter(object_list)
    word_counts_top = word_counts.most_common(1000)

    with open("word_counts.txt", "w") as file:
        for word in word_counts_top:
            file.write(str(word))
            file.write("\n")

    color_list = ['#0000FF', '#CC0033', '#333333']

    colormap = colors.ListedColormap(color_list)

    mask = np.array(Image.open('bj.png'))
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',
        mask=mask,
        max_words=300,
        max_font_size=80,
        background_color='white',
        colormap=colormap,
        random_state=18
    )

    wc.generate_from_frequencies(word_counts)
    image_colors = wordcloud.ImageColorGenerator(mask)
    wc.recolor(color_func=image_colors)
    wc.to_file('f.jpg')

    plt.imshow(wc)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    wordFrequency()
