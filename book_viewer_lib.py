"""Visualize goodreads book data."""

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from typing import Tuple, List

def load_goodreads_data(csv_path: str) -> pd.DataFrame:
    """Loads goodreads data."""
    return pd.read_csv('goodreads_library_export.csv')

def get_titles_and_embeddings(df: pd.DataFrame) -> Tuple:
    """Gets title and embeddings list."""
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    title_embeddings = []
    titles = []
    for title in df['Title']:
        title_embeddings.append(model.encode([title]))
        titles.append(title)
    return titles, title_embeddings

def get_closest_books(titles: List[str],
                      embeddings: List[str], book_index: int) -> None:
    """Prints closest books to book at book index."""
    distance = []
    for i, embedding in enumerate(embeddings):
        distance.append((i, abs(float(np.dot(embedding,
                                       embeddings[book_index].T)))))
    sorted_distance = sorted(distance, key=lambda tup: tup[1], reverse=True)
    print('Original book:', titles[book_index])
    print('=========')
    for i, distance in sorted_distance[1:10]:
        print(i, titles[i])
