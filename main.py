import csv


def main():
    with open('dataset/songs.csv', 'r') as dataset:
        dataset_reader = csv.reader(dataset, delimiter=',')
        for song in dataset_reader:
            song, author, feat, lyric_path = song
            print(song, author, feat, lyric_path)


if __name__ == '__main__':
    main()