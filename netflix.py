import pandas as pd
import numpy as np


df = pd.read_csv('netflix1.csv')

print("=== Dataset Original ===")
print(df.info())

print(df.columns.tolist())
print(df.head())

df['rating'] = df['rating'].astype(str).str.strip()

age_ratings = ['TV-Y', 'TV-Y7', 'TV-Y7-FV', 'G', 'TV-G',
                'PG', 'TV-PG','PG-13', 'TV-14', 
                'R', 'TV-MA', 'NC-17', 
                'NR', 'UR']

df_sorted = df.copy()

df['rating'] = pd.Categorical(df['rating'], categories=age_ratings, ordered=True)

df = df.sort_values(by=['rating'])


df = df.drop_duplicates()

df['director'] = df['director'].replace('Not Given', 'Unknown')
df['country'] = df['country'].replace('Not Given', 'Unknown')

df = df.dropna(subset=['date_added'])


df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['duration_unit'] = df['duration'].str.extract(r'([0-9]+)')

kolom_teks = ['title', 'listed_in', 'type', 'rating']
for col in kolom_teks:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

df.set_index('show_id', inplace=True)
df.to_csv('Netflix_Cleaned.csv')

print("\n === Dataset after cleansing ===")
print(df.info())

print("=== Data diurutkan dari rating anak-anak ke dewasa ===")
print(df[['show_id', 'title', 'rating', 'type']].head(20))

