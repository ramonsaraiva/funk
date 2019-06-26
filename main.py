import csv

from text.processing import (
    deponctuate,
    tokenize,
    unaccent,
)


def main():
    songs = []
    with open('dataset/songs.csv', 'r') as dataset:
        dataset_reader = csv.reader(dataset, delimiter=',')
        for song in dataset_reader:
            song, author, feat, lyric_path = song
            songs.append((song, author, feat, lyric_path))

    song_sample = songs[2]
    *_, lyric_path = song_sample

    with open(f'dataset/lyrics/{lyric_path}', 'r', encoding='utf-8') as lyric_f:
        lyric = lyric_f.read()

    cleaned = tokenize(deponctuate(unaccent(lyric)))
    print(cleaned)


if __name__ == '__main__':
    main()