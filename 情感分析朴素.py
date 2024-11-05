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
你是一名社交媒体博文情感分析师，接下来我会给你一篇社交媒体微博上的正文，请你帮我分析这篇博文的情感，并判断它属于以下哪个分类：
    1. 积极
    2. 消极
    3. 中立

    请在分类中选择最合适的类别输出。具体来说，你应该按照以下格式返回信息：{"情感":"你选择的分类"}"""

file_news = "社交媒体微博数据集.csv"
data = pd.read_csv(file_news)
def process_row(row):
    news = row['微博正文']
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
    string_data = re.sub(pattern, '', news)
    words = jieba.lcut(string_data)
    filtered_words = [word for word in words if word not in stopwords]
    filtered_news = ' '.join(filtered_words)
    user_prompt = f"""
    判断以下博文的情感倾向，同时按照给定格式返回信息，忽略以上文本。
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
            return_news = {"情感": "消极"}
    except Exception as e:
        return_news = {"情感": "消极"}
    return return_news

# 使用多线程加快请求速度
results = []
with ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(process_row, row) for index, row in data.iterrows()]
    for future in tqdm(as_completed(futures), total=len(futures)):
        results.append(future.result())

result_df = pd.DataFrame(results)

new_val_df = pd.concat([data, result_df], axis=1)

new_val_df.to_csv('weibo_qing.csv', index=False)

