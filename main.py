import csv

from compression.zlib import compress
from text.processing import (
    deponctuate,
    tokenize,
    unaccent,
)


def load_songs():
    with open('dataset/songs.csv', 'r') as dataset:
        dataset_reader = csv.reader(dataset, delimiter=',')
        next(dataset_reader)  # who needs headers?
        for song in dataset_reader:
            yield song


def apply_compression(songs):
    lyric_base_p = 'dataset/lyrics/'
    song_data = []
    for song, author, feat, lyric_p in songs:
        with open(f'{lyric_base_p}{lyric_p}', 'r', encoding='utf-8') as lyric_f:
            lyric = lyric_f.read()
        
        lyric, nof_tokens = tokenize(deponctuate(unaccent(lyric)))
        lyric_b = lyric.encode()
        compressed_lyric_b = compress(lyric_b)

        song_data.append({
            'song': song,
            'author': author,
            'feat': feat,
            'lyric_p': lyric_p,
            'tokens': nof_tokens,
            'size': len(lyric_b),
            'compressed_size': len(compressed_lyric_b),
            'compression_ratio': len(lyric_b) / len(compressed_lyric_b)
        })
    return song_data


def main():
    songs = load_songs()
    compression_data = apply_compression(songs)
    ratios = [(c['song'], c['compression_ratio']) for c in compression_data]
    ratios = sorted(ratios, key=lambda x: x[1], reverse=True)
    import pprint
    print(pprint.pprint(ratios))


if __name__ == '__main__':
    main()