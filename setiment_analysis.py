# %%
import pandas as pd
from openai import OpenAI
import openai_api_key
import numpy as np

# %%
print(openai_api_key.API_KEY)
# %%

def prompt_comentario(comentario: str) -> str:
    prompt = f"""
    Responda com "bom", "ruim" ou "indefinido".Qual o sentimento do comentário abaixo?

    {comentario}
    """
    return prompt
# %%

print(prompt_comentario("maria joaquina"))

# %%

df = pd.read_csv('database\olist_order_reviews_dataset.csv')
df.head(5)

# %%

import random
def avalia_comentario(review) -> str:
    opcoes = ["bom", "ruim", "indefinido"]
    if review is not np.nan:
        return random.choice(opcoes)
    else:
        return None

# %%

reviews_sentiment = {"review_id": [], "sentiment": []}

for row in df.iterrows():
    reviews_sentiment["review_id"].append(row[0])
    reviews_sentiment["sentiment"].append(avalia_comentario(row[1][4]))

reviews_sentiment = pd.DataFrame(reviews_sentiment)
reviews_sentiment.to_csv('database/olist_orders_reviews_sentiment_dataset.csv', index=False)
# %%
