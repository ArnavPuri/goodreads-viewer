### Goodreads viewer

This repo analyses personal goodreads book data.


You can export your own library [Goodreads: How do I import or export my books?](https://help.goodreads.com/s/article/How-do-I-import-or-export-my-books-1553870934590)
and replace the csv file to experiment with the repository.

#### Load your books and analyze
Download goodreads webpage and store as `webpages/<userid>/<userid>-{1/2/3/etc}.htm`
```
book_viewer_lib.parse_and_store_books(<userid>, 5)
with open('<userid>.txt') as f:
    book_titles = f.readlines()
book_titles = [x.strip() for x in book_titles]
title_embeddings = book_viewer_lib.get_embeddings(book_titles)
book_viewer_lib.get_closest_books(book_titles, title_embeddings, 0)
```

Output:
```
Original book: Mindstorms: Children, Computers, And Powerful Ideas
=========
162 Hackers: Heroes of the Computer Revolution
350 A Thousand Brains: A New Theory of Intelligence
151 The Educated Mind: How Cognitive Tools Shape Our Understanding
106 The Innovators: How a Group of Hackers, Geniuses and Geeks Created the Digital Revolution
357 Thinking In Systems: A Primer
238 Impromptu: Amplifying Our Humanity Through AI
125 The Idea Factory: Bell Labs and the Great Age of American Innovation
107 The Dream Machine: J.C.R. Licklider and the Revolution That Made Computing Personal
209 The Self-Assembling Brain: How Neural Networks Grow Smarter
```

Installation using conda:

```
conda create -n goodreads-py12 python=3.12
conda activate goodreads-py12

pip install -r requirements.txt
```
