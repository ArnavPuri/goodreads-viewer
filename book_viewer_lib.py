"""Visualize goodreads book data."""

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from typing import Tuple, List
from bs4 import BeautifulSoup
import csv

def load_goodreads_data(csv_path: str) -> pd.DataFrame:
    """Loads goodreads data."""
    return pd.read_csv('goodreads_library_export.csv')


def get_embeddings(titles: List) -> Tuple:
    """Gets title and embeddings list."""
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    title_embeddings = []
    for title in titles:
        title_embeddings.append(model.encode([title]))
    return title_embeddings

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
                      embeddings: List[str], book_index: int, num_closest_books: int) -> None:
    """Prints closest books to book at book index."""
    distance = []
    closest_books = []
    for i, embedding in enumerate(embeddings):
        distance.append((i, abs(float(np.dot(embedding,
                                       embeddings[book_index].T)))))
    sorted_distance = sorted(distance, key=lambda tup: tup[1], reverse=True)
    for i, distance in sorted_distance[1:1+num_closest_books]:
        closest_books.append((i, titles[i]))
    return closest_books


def get_books_in_html_page(file_path: str) -> List:
    titles = []
    # Read the local HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    td_elements = soup.find_all('td', class_='field title')
    for td in td_elements:
        a_tag = td.find('a')
        if a_tag and 'title' in a_tag.attrs:
            titles.append(a_tag['title'])

    return titles

def save_booklist_to_file(book_titles: List, book_file: str):
    # Write the list to the file
    with open(book_file, 'w') as file:
        for item in book_titles:
            file.write(f"{item}\n")

    print(f"List has been written to {book_file}")

def parse_and_store_books(name: str, num_files: int):
    book_titles = []
    for i in range(1, num_files+1):
        file_path = f'webpages/{name}/{name}-{i}.htm'
        book_titles.extend(get_books_in_html_page(file_path))
    save_booklist_to_file(book_titles, f'{name}.txt')