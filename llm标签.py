import os
import pandas as pd
from openai import OpenAI
import jieba
import json
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

client = OpenAI(api_key="sk-2952ae216ecb44189f1a820c10c66138", base_url="https://api.deepseek.com")

stopwords = set()
with open('中文停用词表.txt', 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.add(line.strip())

system_prompt = """
你是一名新闻分析师，接下来我会给你一篇新闻的正文，请你帮我分析这篇新闻的主题，并判断它属于以下哪个分类：
    1. 经济
    2. 科技
    3. 政治
    4. 体育
    5. 娱乐
    6. 健康
    7. 社会
    8. 其他

    请在分类中选择最合适的类别输出。具体来说，你应该按照以下格式返回信息：{"类别":"你选择的分类"}"""

file_path = "./data"
file_news = os.path.join(file_path, '官方新闻数据集.xlsx')
data_news = pd.read_excel(file_news)
data = pd.read_csv('news.csv')

data_news.rename(columns={'title': '标题'}, inplace=True)
data_news.rename(columns={'origin': '来源'}, inplace=True)
data_news.rename(columns={'create_time': '时间'}, inplace=True)
data_news.rename(columns={'article': '正文'}, inplace=True)
data_news = data_news[['标题', '时间', '正文', '来源']]


def process_row(row):
    news = row['正文']
    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    try:
        string_data = re.sub(pattern, '', news)
    except Exception as e:
        print(news)
    words = jieba.lcut(string_data)
    filtered_words = [word for word in words if word not in stopwords]
    filtered_news = ' '.join(filtered_words)
    user_prompt = f"""
    判断以下新闻的类别，同时按照给定格式返回信息，忽略以上文本。
    news:{filtered_news}"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"{system_prompt}"},
                {"role": "user", "content": f"{user_prompt}"},
            ],
            stream=False
        )
        news_parts = response.choices[0].message.content
        try:
            return_news = json.loads(news_parts)
        except json.JSONDecodeError as json_err:
            return_news = {"类别": "其他"}
    except Exception as e:
        return_news = {"类别": "其他"}
    return return_news

# 使用多线程加快请求速度
results = []
with ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(process_row, row) for index, row in data_news.iterrows()]
    for future in tqdm(as_completed(futures), total=len(futures)):
        results.append(future.result())

result_df = pd.DataFrame(results)

new_val_df = pd.concat([data_news, result_df], axis=1)

new_val_df.to_csv('社交媒体新闻数据集.csv', index=False)
new_val_df = pd.concat([new_val_df, data], ignore_index=True)
new_val_df.to_csv('社交媒体新闻总数据集.csv', index=False)