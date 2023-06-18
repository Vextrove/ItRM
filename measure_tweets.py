import gzip
import os
from collections import Counter


def count_conjunctions(text):
    '''Counts occurrences of each conjunction in a given list of words'''
    conjunctions = Counter()
    trigger_words = open("conjunctions.txt", "r").read().split()

    for word in trigger_words:
        conjunctions[word] = 0

    for word in text:
        if word in trigger_words:
            conjunctions[word] += 1

    return conjunctions


def get_file_paths():
    """Obtains file paths of tweets"""
    file_paths = []
    for root, dirs, files in os.walk('./tweets'):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


def main():
    '''Runs the module with a test sentence containing a conjunction'''
    # print(count_conjunctions(text.split()))

    for file_path in get_file_paths():
        with gzip.open(file_path, 'rt') as tweets:
            print(tweets)
            for tweet in tweets.read():
                print(tweet)


if __name__ == "__main__":
    """Only runs the main function if this code is run directly rather than imported"""
    main()
