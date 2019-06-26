import csv

from compression.zlib import compress
from text.processing import (
    deponctuate,
    tokenize,
    unaccent,
)


def load_songs():
    with open('dataset/songs.csv', 'r', encoding='utf-8') as dataset:
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

        lyric_size = len(lyric_b)
        compressed_lyric_size = len(compressed_lyric_b)

        song_data.append({
            'song': song,
            'author': author,
            'feat': feat,
            'lyric_p': lyric_p,
            'tokens': nof_tokens,
            'size': lyric_size,
            'compressed_size': compressed_lyric_size,
            'compression_ratio': lyric_size / compressed_lyric_size,
            'space_savings': 1 - (compressed_lyric_size / lyric_size),
        })
    return song_data


def main():
    songs = load_songs()
    data = apply_compression(songs)
    sorted_by_ratio = sorted(
        data, key=lambda x: x['compression_ratio'], reverse=True)
    for song_data in sorted_by_ratio:
        print(','.join([
            song_data['song'],
            song_data['author'],
            str(song_data['size']),
            str(song_data['compressed_size']),
            f'{song_data["compression_ratio"]:.2f}',
            f'{song_data["space_savings"] * 100:.2f}%',
        ]))


if __name__ == '__main__':
    main()