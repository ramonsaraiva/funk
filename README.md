# funk

## Funk music is stuck on repeat

This is an application of Colin Morris' TED "Pop Music is Stuck on Repeat" theory to Brazilian funk/pop top hits.

## Dataset

I started with 30 top funk/pop songs from known listings in Brazil, just enough for a small proof of concept, I'll probably add more songs as time allows.

You can see the list of songs in [this csv](dataset/songs.csv). It contains the song name, author, feat, and the lyric filename that lives under [lyrics](dataset/lyrics).

## Text processing

There are 3 processor in the text processing pipeline, they're all pretty simple and implemented under [this module](text/processing.py).
I initially unaccent the whole text, then deponctuate and finally tokenize it.

This pipeline transforms something like:
```
Héllô!
There.
```

into

```
hello there
```

## Compression

Measuring a song repetitiveness is a simple as compressing it.

Repetitive lyrics are redundant and good compression algorithms can exploit redundancy at scale to shrink text more efficiently.

I used the Python's stdlib `zlib` library. [zlib](https://zlib.net/) supports one algorithm called DEFLATE, that is a variation of LZ77 (Lempel-Ziv 1977). This algorithm provides good compression on a wide variety of data with minimal use of system resources. This is also the algorithm used in the ZIP archive format.