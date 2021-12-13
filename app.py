import pyterrier as pt
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import lightgbm as lgb

if not pt.started():
    pt.init()


index_ref = './pt_bio_index_baseline_positions/data.properties'
index_pos = pt.IndexFactory.of(index_ref)
bm25_pos = pt.BatchRetrieve(index_pos, wmodel="BM25")

author_df = pd.read_csv('all_authors_v3.csv')
author_df = author_df.drop('Unnamed: 0', axis=1).reset_index().rename(columns={'index': 'docno'})
author_df['docno'] = author_df['docno'].astype(str)

while True:
    query = input(f"Input a query, or type done (i.e. lawyer): ")
    if query.lower() == 'done':
        break
    res_df = bm25_pos.search(query).merge(author_df, on="docno")[['handle', 'name', 'author_bio']][:5]
    if len(res_df) == 0:
        print('No results. Try again, or type done')
        continue
    else:
        print(f"\nQuery Results\n{'='*100}")
        for row in res_df.iterrows():
            print(f"Handle: @{row[1]['handle'].strip()}")
            print(f"Name: {row[1]['name']}")
            print(f"Bio:\n{row[1]['author_bio']}")
            print('-'*200)