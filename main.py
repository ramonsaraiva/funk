import csv

from text.processing import (
    deponctuate,
    unaccent,
)


def main():
    songs = []
    with open('dataset/songs.csv', 'r') as dataset:
        dataset_reader = csv.reader(dataset, delimiter=',')
        for song in dataset_reader:
            song, author, feat, lyric_path = song
            songs.append((song, author, feat, lyric_path))

    song_sample = songs[1]
    *_, lyric_path = song_sample

    with open(f'dataset/lyrics/{lyric_path}', 'rb') as lyric_f:
        lyric_b = lyric_f.read()

    unaccented = unaccent(lyric_b.decode('utf-8'))
    deponctuated = deponctuate(unaccented)
    print(deponctuated)


if __name__ == '__main__':
    main()