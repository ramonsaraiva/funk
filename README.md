# funk

## Funk music is stuck on repeat

This is an application of Colin Morris' TED ("Pop Music is Stuck on Repeat")[https://www.youtube.com/watch?v=_tjFwcmHy5M] theory to Brazilian funk/pop top hits.

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

Measuring a song repetitiveness is as simple as compressing it. Repetitive lyrics are redundant and good compression algorithms can exploit redundancy at scale to shrink text more efficiently.

I used the Python's stdlib `zlib` library. [zlib](https://zlib.net/) supports one algorithm called DEFLATE, that is a variation of LZ77 (Lempel-Ziv 1977). This algorithm provides good compression on a wide variety of data with minimal use of system resources. This is also the algorithm used in the ZIP archive format.


## Initial results

This is the initial results ordered by compression ratio in a descending order.

| Song                    | Author                   | Size | Comp. size | Comp. ratio |  Space savings | 
|-------------------------|--------------------------|------|------------|-------------|----------------| 
| Amar? Amei              | MC Don Juan              | 2002 | 208        | 9.62        | 89.61%         | 
| Que tiro foi esse       | Jojo Maronttinni         | 1241 | 144        | 8.62        | 88.40%         | 
| Agora vai sentar        | MC's Jhowzinho e Kadinho | 1628 | 234        | 6.96        | 85.63%         | 
| Olha a explosão         | MC Kevinho               | 1320 | 199        | 6.63        | 84.92%         | 
| Parado no bailão        | MC L Da Vinte            | 1109 | 178        | 6.23        | 83.95%         | 
| Só quer vrau            | MC MM                    | 1706 | 287        | 5.94        | 83.18%         | 
| Quem tem o dom          | Jerry Smith              | 1871 | 315        | 5.94        | 83.16%         | 
| Cheguei                 | Ludmilla                 | 1531 | 259        | 5.91        | 83.08%         | 
| O bebê                  | MC Kevinho               | 1354 | 247        | 5.48        | 81.76%         | 
| Favela chegou           | Ludmilla                 | 1356 | 256        | 5.30        | 81.12%         | 
| Rabiola                 | MC Kevinho               | 1605 | 304        | 5.28        | 81.06%         | 
| Din Din Din             | Ludmilla                 | 1962 | 374        | 5.25        | 80.94%         | 
| Facilita                | MC Kevinho               | 1570 | 312        | 5.03        | 80.13%         | 
| Amor de verdade         | MC Kekel                 | 1995 | 402        | 4.96        | 79.85%         | 
| Agora é tudo meu        | Dennis DJ                | 1474 | 303        | 4.86        | 79.44%         | 
| Papum                   | MC Kevinho               | 1138 | 238        | 4.78        | 79.09%         | 
| Vamos pra gaiola        | MC Kevin                 | 1313 | 281        | 4.67        | 78.60%         | 
| Salvou meu dia          | MC Kevinho               | 1508 | 332        | 4.54        | 77.98%         | 
| Deu onda                | MC G15                   | 737  | 166        | 4.44        | 77.48%         | 
| Vai menina              | Pedro Sampaio            | 762  | 174        | 4.38        | 77.17%         | 
| Solteiro nunca está só  | MC Kekel                 | 830  | 194        | 4.28        | 76.63%         | 
| Ta tum tum              | MC Kevinho               | 1654 | 398        | 4.16        | 75.94%         | 
| Amor bandido            | Lexa                     | 1786 | 446        | 4.00        | 75.03%         | 
| Medley da gaiola        | MC Kevin                 | 2088 | 541        | 3.86        | 74.09%         | 
| O grave bater           | MC Kevinho               | 793  | 208        | 3.81        | 73.77%         | 
| Só você                 | Dennis DJ                | 1098 | 294        | 3.73        | 73.22%         | 
| Terremoto               | Anitta                   | 1646 | 457        | 3.60        | 72.24%         | 
| Vai malandra            | Anitta                   | 1877 | 540        | 3.48        | 71.23%         | 
| Você partiu meu coração | Nego do Borel            | 1491 | 478        | 3.12        | 67.94%         | 
| Bola rebola             | Tropkillaz               | 2201 | 722        | 3.05        | 67.20%         | 

The lowest compression ratio for these 30 sample songs is 3.05.


## Next steps

* Add more songs, at least 100
* Self-similarity matrix