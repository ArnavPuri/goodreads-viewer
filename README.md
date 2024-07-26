### Goodreads viewer

This repo analyses personal goodreads book data.


You can export your own library [Goodreads: How do I import or export my books?](https://help.goodreads.com/s/article/How-do-I-import-or-export-my-books-1553870934590)
and replace the csv file to experiment with the repository.

```
>> book_viewer_lib.get_closest_books(titles, embeddings, 5)

Original book: Something Incredibly Wonderful Happens: Frank Oppenheimer and the world he made up
=========
35 American Prometheus: The Triumph and Tragedy of J. Robert Oppenheimer
1 The Making of the Atomic Bomb
61 The Rise and Fall of the Third Reich: A History of Nazi Germany
315 Leonardo da Vinci
240 Great Founder Theory
359 Boom and Bust: A Global History of Financial Bubbles
291 Start-up Nation: The Story of Israel's Economic Miracle
160 The Art of War
15 Nixon Agonistes: The Crisis of the Self-Made Man
```

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
