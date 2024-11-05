import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm
import numpy as np
import re

# 列出所有可用的字体
fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')
print("Available fonts:", fonts)

# 设置默认字体
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial', 'DejaVu Sans', 'Lucida Grande', 'Verdana']
# 假设的数据
# data = pd.read_csv('news.csv')
# count = data['类别'].value_counts()
# count_df = pd.DataFrame({'类别': count.index, '数量': count.values})
# print(count_df['数量'])
# 绘制饼图
# plt.figure(figsize=(8, 8))
# plt.pie(count_df['数量'], labels=count_df['类别'], autopct='%1.1f%%', startangle=140)
#
# # 添加标题
# plt.title('类别分布')
# plt.tight_layout()
# # 显示图形
# plt.show()
# # 将 '时间' 列转换为字符串类型
# data['时间'] = data['时间'].astype(int)
#
#
# # 过滤出 2023 年和 2024 年的数据
# data_2023 = data[data['时间'] == 2023]
# data_2024 = data[data['时间'] == 2024]
# # 统计每个类别在 2023 年和 2024 年的数量
# count_2023 = data_2023['类别'].value_counts()
# count_2024 = data_2024['类别'].value_counts()
# #
# # # 确保两个年份的类别顺序一致
# # categories = count_2023.index
# # # 将统计结果转换为 DataFrame
# count_2023_df = pd.DataFrame({'类别': count_2023.index, '数量': count_2023.values})
# count_2024_df = pd.DataFrame({'类别': count_2024.index, '数量': count_2024.values})
# print(count_2023_df)
# print(count_2024_df)
#
# # 合并两个年份的数据
# count_df = pd.merge(count_2023_df, count_2024_df, on='类别', suffixes=('_2023', '_2024'), how='outer')
#
# # 填充缺失值为 0
# count_df.fillna(0, inplace=True)
#
# # 设置柱状图的宽度
# bar_width = 0.35
#
# # 设置 x 轴的位置
# index = range(len(categories))
#
# # # 绘制 2023 年的数据
# plt.bar(index, count_df['数量_2023'], bar_width, label='2023', color='b')
#
# # 绘制 2024 年的数据
# plt.bar([i + bar_width for i in index], count_df['数量_2024'], bar_width, label='2024', color='r')
#
# # 设置 x 轴的标签
# plt.xticks([i + bar_width / 2 for i in index], categories, rotation=45)
#
# # 添加标题和标签
# plt.xlabel('类别')
# plt.ylabel('数量')
# plt.title('2023 和 2024 年数据对比')
#
# # 添加图例
# plt.legend()
#
# # 显示图形
# plt.tight_layout()
# plt.show()
# 准备数据：年份和每个类别的新闻数量
years = [2023, 2024]
politics = [5815, 7703]
economy = [2750, 5105]
society = [1849, 4157]
tech = [460, 1098]
entertainment = [137, 315]
sports = [110, 318]
health = [104, 257]
other = [214, 249]
jiaoyu = [4, 5]
yishu = [0, 1]

categories = [politics, economy, society, tech, entertainment, sports, health, other, jiaoyu, yishu]
labels = ['政治', '经济', '社会', '科技', '娱乐', '体育', '健康', '其他', '教育', '艺术']

plt.figure(figsize=(15, 10))
plt.stackplot(years, *categories, labels=labels)
plt.legend(loc='upper left')
plt.title('类别堆积面积图（2023-2024）')
plt.xlabel('年份')
plt.ylabel('数量')
plt.show()


# data = pd.read_csv('社交媒体微博数据集.csv')
# pattern = re.compile(r'(\d{4}/\d+)')
# pattern_ = re.compile(r'(\d{4}-\d{2})')
#
#
# def getym(string):
#     string = str(string)
#     match = pattern.match(string)
#     match_ = pattern_.match(string)
#     if match:
#         return match.group(1)
#     else:
#         return match_.group(1).replace("-", '/')
#
#
# data['发布时间'] = data['发布时间'].apply(getym)
# categories = data['类别'].unique()
# print(categories)
# count_dict = {}
# flag = True
# count_sum = None
# for categoriein in categories:
#     count_ = data[data['类别'] == categoriein]['发布时间'].value_counts()
#     temp = pd.DataFrame({'时间': count_.index, '数量': count_.values})
#     if flag:
#         count_sum = temp
#         flag = False
#     else:
#         count_sum = pd.merge(count_sum, temp, on='时间', suffixes=(categoriein, categoriein), how='outer')
#
# count_sum.fillna(0, inplace=True)
# count_sum.to_excel('微博折线图制作.xlsx',index=False)
# grouped = data.groupby('类别').sum()
#
# # 类别
# categories = grouped.index.tolist()
#
# # 数据
# likes = grouped['点赞数'].tolist()
# retweets = grouped['转发数'].tolist()
# comments = grouped['评论数'].tolist()
# for categorie in categories:
#     print(categorie)
# print("\n")
# for like in likes:
#     print(like)
# print("\n")
# for retweetin in retweets:
#     print(retweetin)
# print("\n")
# for comment in comments:
#     print(comment)
# # 设置柱状图的宽度
# bar_width = 0.25

# 设置x轴的位置
# r1 = np.arange(len(categories))
# r2 = [x + bar_width for x in r1]
# r3 = [x + bar_width for x in r2]
#
# # 绘制柱状图
# plt.bar(r1, likes, color='blue', width=bar_width, edgecolor='grey', label='点赞数')
# plt.bar(r2, retweets, color='green', width=bar_width, edgecolor='grey', label='转发数')
# plt.bar(r3, comments, color='red', width=bar_width, edgecolor='grey', label='评论数')
#
# # 添加x轴标签
# plt.xlabel('类别', fontweight='bold')
# plt.xticks([r + bar_width for r in range(len(categories))], categories)
#
# # 添加y轴标签
# plt.ylabel('数量', fontweight='bold')
#
# # 添加图例
# plt.legend()
#
# # 显示图形
# plt.show()

# string_s = """
# 2023-01: 21
# 2023-02: 14
# 2023-03: 10
# 2023-04: 1
# 2023-05: 3
# 2023-06: 1
# 2023-07: 0
# 2023-08: 0
# 2023-09: 2
# 2023-10: 1
# 2023-11: 93
# 2023-12: 69
# 2024-01: 138
# 2024-02: 131
# 2024-03: 159
# 2024-04: 157
# 2024-05: 152
# 2024-06: 106
# 2024-07: 123
# 2024-08: 110
# 2024-09: 106
# """

# data = pd.read_csv('weibo_qing.csv')
#
# categories = data['类别'].unique()
# print(categories)
# for categoriein in categories:
#     count_ = data[data['类别'] == categoriein]['情感'].value_counts()
#     print(count_.index)
#     print(count_.values)
#     print("\n")

# data = pd.read_csv('社交媒体微博数据集.csv')
# categories = data['类别'].unique()
# for i in categories:
#     print(i)
# count_dict = {}
# flag = True
# count_sum = None
# pre_name = ""
# for categoriein in categories:
#     count_ = data[data['类别'] == categoriein]['情感'].value_counts()
#     temp = pd.DataFrame({'情感': count_.index, '数量': count_.values})
#     if flag:
#         count_sum = temp
#         flag = False
#     else:
#         count_sum = pd.merge(count_sum, temp, on='情感', suffixes=(pre_name, categoriein), how='outer')
#     pre_name = categoriein
#
# count_sum.fillna(0, inplace=True)
# count_sum = count_sum.transpose()
# count_sum.to_excel('微博情感柱状图图制作.xlsx',index=False)