import pandas as pd

data = pd.read_csv("官方新闻总数据集.csv")

categories = data['类别'].unique()

for category in categories:
    fen_df = data[data['类别'] == category]
    fen_df.to_csv(f"官方新闻数据集_{category}.csv", index=False)
